Cookiecutter Modern CMake
===============

[![See Build Status on Travis CI][travis_badge]][travis]
[![Github - Last tag][lasttag_badge]][lasttag]

[Cookiecutter] template for a modern CMake project.

A modern cmake template

Getting Started
------------
Install [Cookiecutter] and generate a new cmake project:

```no-highlight
$ pip install cookiecutter
$ cookiecutter https://github.com/Aetf/cc-modern-cmake
```

Cookiecutter prompts you for information regarding your plugin:

```no-highlight
full_name [Your name]:
email [Your address email (eq. you@example.com)]:
github_username [Your github username]:
project_name [Name of the project]:
project_slug [name-of-the-project]:
project_namespace [nameoftheproject]:
project_short_description [A short description of the project]:
release_date [2018-08-14]:
version [0.1.0]:
Select with_qt:
1 - False
2 - True
Choose from 1, 2 [1]:
Removing resources for disabled feature qt...
Removing file: tests/catch2_qt.h
Cleanup complete, removing manifest...
Removing file: manifest.toml
```

There you go - you just created a minimal cmake project with a small library and an executable:

```no-highlight
project/
├── CHANGELOG.md
├── CMakeLists.txt
├── LICENSE
├── README.md
├── VERSION
├── cmake
├── include
├── src
├── tasks.py
├── tests
└── thirdparty
```

Features
--------

- Modern CMake build system
- Test suite using [Catch2]
- Working example code for both a shared and static library, as well as an app executable

License
-------
This project is licensed under the terms of the [BSD 2-Clause License](/LICENSE)

[travis_badge]: https://travis-ci.org/Aetf/cc-modern-cmake.svg?branch=master
[travis]: https://travis-ci.org/Aetf/cc-modern-cmake (See Build Status on Travis CI)
[lasttag_badge]: https://img.shields.io/github/tag/Aetf/cc-modern-cmake.svg
[lasttag]: https://github.com/Aetf/cc-modern-cmake/tags (Github - Last tag)
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[CMake]: https://cmake.org
[Catch2]: https://github.com/catchorg/Catch2
