#!/usr/bin/env python
from __future__ import print_function, division, absolute_import

import os
import shutil
import sys
import subprocess as sp
from collections import defaultdict

MANIFEST = "manifest.toml"


def install(package):
    """Install a package through pip"""
    return sp.call([sys.executable, "-m", "pip", "install", package])


def load_manifest():
    try:
        import toml
    except ImportError:
        install('toml')
        import toml

    with open(MANIFEST) as f:
        return toml.load(f)


def delete_resources_for_disabled_features():
    manifest = load_manifest()
    for feature in manifest['features']:
        if not feature['enabled']:
            print("Removing resources for disabled feature {}...".format(feature['name']))
            for resource in feature['resources']:
                delete_resource(resource)
    print("Cleanup complete, removing manifest...")
    delete_resource(MANIFEST)


def delete_resource(resource):
    if os.path.isfile(resource):
        print("Removing file: {}".format(resource))
        os.remove(resource)
    elif os.path.isdir(resource):
        print("removing directory: {}".format(resource))
        shutil.rmtree(resource)


def init_git():
    sp.check_call(['git', 'init'])

    # instead of relying on .gitmodules file, parse it and use git cli to add modules
    # read .gitmodules file
    gitmodules = defaultdict(dict)
    outputs = sp.check_output(['git', 'config', '-f', '.gitmodules', '-z', '--get-regexp', r'^submodule\.'],
                              universal_newlines=True).split('\x00')
    for line in outputs:
        if not line:
            continue
        parts = line.split('\n')
        if len(parts) != 2:
            continue
        name, _, key = parts[0].lstrip('submodule.').rpartition('.')
        gitmodules[name][key] = parts[1]

    # make sure we have 'url' and 'path'
    def hasKeys(d, *args):
        for k in args:
            if k not in d:
                return False
        return True

    gitmodules = {name: props for name, props in gitmodules.items() if hasKeys(props, 'url', 'path')}

    # remove .gitmodules file otherwise it will have duplicate entry
    os.unlink('.gitmodules')

    # add submodule
    for name, props in gitmodules.items():
        add_cmd = ['git', 'submodule', 'add', '--name', name]
        if 'branch' in props:
            add_cmd += ['-b', props['branch']]
        add_cmd += ['--', props['url'], props['path']]
        sp.check_call(add_cmd, stdout=sp.PIPE, stderr=sp.PIPE)

    sp.check_call(['git', 'add', '--all', '.'])
    sp.check_call(['git', 'commit', '-m', 'Initial commit'])


if __name__ == "__main__":
    delete_resources_for_disabled_features()
    init_git()
