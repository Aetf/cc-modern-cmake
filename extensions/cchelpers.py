from __future__ import print_function, division, absolute_import

from jinja2.ext import Extension
from jinja2 import nodes
from datetime import datetime


def obfuscate_email(email):
    if '@' not in email:
        return email

    parts = email.split('@')
    parts[-1] = parts[-1].replace('.', ' dot ')
    return ' at '.join(parts)


class HelperFilters(Extension):
    def __init__(self, environment):
        super(HelperFilters, self).__init__(environment)
        environment.filters["obs_email"] = obfuscate_email


class CopyrightTag(Extension):
    tags = set(['copyright'])

    def __init__(self, environment):
        super(CopyrightTag, self).__init__(environment)

    def parse(self, parser):
        # the first token is the token that started the tag.  In our case
        # we only listen to ``'copyright'`` so this will be a name token with
        # `copyright` as value.  We get the line number so that we can give
        # that line number to the nodes we create by hand.
        lineno = next(parser.stream).lineno

        callmethod = self.call_method('_copyright', [nodes.ContextReference()], lineno=lineno)
        return nodes.Output([callmethod], lineno=lineno)

    def _copyright(self, context):
        year = datetime.now().year
        name = context['cookiecutter']['full_name']
        email = obfuscate_email(context['cookiecutter']['email'])
        return 'Copyright (c) {year} {name} <{email}>'.format(year=year, name=name, email=email)


__all__ = ["HelperFilters", "CopyrightTag"]
