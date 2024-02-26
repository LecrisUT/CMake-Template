# Modern CMake example project

[![CI Status][ci-badge]][ci-link]
[![Codecov Status][codecov-badge]][codecov-link]
[![SonarCloud Status][sonarcloud-badge]][sonarcloud-link]

[![Documentation Status][rtd-badge]][rtd-link]
![CMake Status][cmake-badge]

[ci-badge]: https://github.com/LecrisUT/CMake-Template/actions/workflows/ci.yaml/badge.svg?branch=main&event=push
[rtd-badge]: https://readthedocs.org/projects/lecrisut-cmake-template/badge/?version=latest
[codecov-badge]: https://codecov.io/gh/LecrisUT/CMake-Template/graph/badge.svg?token=YAEN2SWB10
[sonarcloud-badge]: https://sonarcloud.io/api/project_badges/measure?project=LecrisUT_CMake-Template&metric=alert_status
[cmake-badge]: https://img.shields.io/badge/CMake-3.25-blue?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGRhdGEtbmFtZT0iTGF5ZXIgMiIgdmlld0JveD0iMCAwIDU0NS41IDU0NS45Ij48cGF0aCBkPSJNNTQ2IDUzNCAyODIgOWwzOSA0MzQgMjI1IDkxeiIgZGF0YS1uYW1lPSJyZWQgcmlnaHQiIHN0eWxlPSJmaWxsOiNmMzI3MzU7c3Ryb2tlLXdpZHRoOjAiLz48cGF0aCBkPSJNNTI1IDU0NiAxNzAgNDAzIDEgNTQ2aDUyNHoiIGRhdGEtbmFtZT0iZ3JlZW4gYm90dG9tIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOjA7ZmlsbDojM2VhZTJiIi8+PHBhdGggZD0iTTI2MyAwIDAgNTIybDI4OC0yNDRMMjYzIDB6IiBkYXRhLW5hbWU9ImJsdWUgbGVmdCIgc3R5bGU9ImZpbGw6IzAwNjhjNztzdHJva2Utd2lkdGg6MCIvPjxwYXRoIGQ9Im0yOTEgMjk5LTEwNSA4OSAxMTcgNDgtMTItMTM3eiIgZGF0YS1uYW1lPSJncmF5IGNlbnRlciIgc3R5bGU9ImZpbGw6I2RjZTNlYztzdHJva2Utd2lkdGg6MCIvPjwvc3ZnPg==

[ci-link]: https://github.com/LecrisUT/CMake-Template/actions?query=branch%3Amain+event%3Apush
[rtd-link]: https://lecrisut-cmake-template.readthedocs.io/en/latest/?badge=latest
[codecov-link]: https://codecov.io/gh/LecrisUT/CMake-Template
[sonarcloud-link]: https://sonarcloud.io/summary/new_code?id=LecrisUT_CMake-Template

<!-- SPHINX-START -->

An example CMake project highlighting various modern practices. Feel free to
use this project as a template for bootstrapping or modernizing your own CMake
project.

## Installation

This project contains a simple hello-world example, so you can clone, build and
run to see the template in action. E.g. after cloning this repository you can
run:

```console
$ cmake -B ./build
$ cmake --build ./build
$ ./build/hello
Hello, world!
```

## What's in this template

### Modern CMake design

This modern design ensures:

- The project can be configured and built easily by a user using
  [`cmake-presets`][cmake-presets].
- It can import other CMake projects seamlessly regardless if it's installed
  on the system, downloaded from the internet or even if the project is not
  built in CMake.
- It can be imported and used by other CMake projects, including being
  partially imported, e.g. to run CTest on the copy of the project already
  installed.
- The project is easily navigable in a logical structure, such that a user
  without any CMake experience can guess on the capabilities of the project.
- The CMake components can be documented using a [`sphinx`][sphinx]
  documentation engine.

### Modern CI tools

The CI tools available are constantly evolving, but broadly they cover:

- GitHub Actions workflows for:
  - Enforcing coding standards
  - CI testing the project against multiple distros and compilers
  - CD to easily publish new releases
  - Hardening workflow permissions
  - Maintain a reusable format that can be imported by other projects
- [`pre-commit`][pre-commit] for managing most coding standards
- [`sphinx`][sphinx] documentation
- Static code analysis

### Packaging and downstream tools

In this template we focus on packaging to Fedora due to their vast CI tools:

- [`packit`][packit]: Used for testing the packaging on [copr], run additional
  tests on [testing-farm], and make pull-requests downstream (e.g. on [Fedora])
- [`tmt`][tmt] and [testing-farm]: Used to test your project as if it has been
  installed and run locally

<!-- SPHINX-END -->

## License

This template project is licensed under MIT license. Please update the
[`LICENSE`](LICENSE) file after using this template. You may re-license your
project as you wish after using this template.

[cmake-presets]: https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html
[copr]: https://copr.fedorainfracloud.org/
[fedora]: https://src.fedoraproject.org/
[packit]: https://packit.dev
[pre-commit]: https://pre-commit.com/
[sphinx]: https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html
[testing-farm]: https://docs.testing-farm.io/Testing%20Farm/0.1/index.html
[tmt]: https://tmt.readthedocs.io/en/stable/
