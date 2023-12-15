# Modern CMake example project

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
