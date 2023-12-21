# Downloading the project

First step is where do we even get the files we need to start using the project.
As you're probably aware by now, C/C++ projects do not have a concise packaging
system [^1][^2] like [PyPI] is for python, so the starting point here is not that
straight-forward. The actual project that implemented this template should
document where they are officially packaging the project, usually on the
front-page of their git repository or documentation.

Regardless, here I will try to cover some of the common sources and conventions
where you can find the project.

[PyPI]: https://pypi.org/

---

## Where do I download the project from?
::::{tab-set}
:::{tab-item} As an end-user
For the most part you should look for a [packaged] source, even the project you
want to use is a library that you would be using in your own C/C++ project.

When importing the project within another CMake project, the recommended way is
[using `FetchContent`], which will internally use either the [packaged] or
[source] version.
:::
:::{tab-item} As an upstream developer
You are primarily interested in the [source] version. When working on multiple
projects, it is especially useful to know how to setup your [CMakeUserPreset] so
that you can easily switch between one project and another.
:::
:::{tab-item} As a downstream packager
You should be aware on how get the project from [source]. The original git
source is preferred since CMake does not bundle any additional metadata in its
archive.
:::
::::

## Packaged version

:::{admonition} Tl;dr
One of the:
```console
$ dnf install awesome-project-devel
$ apt install awesome-project-dev
$ brew install awesome-project
$ conda install awesome-project
$ pip install awesome-project
...
```
:::

From the OS distribution, you will find the project separated into runtime
packages that have the plain name of the project e.g. `awesome-project` and
development packages like `awesome-project-devel`, which you only need if the
project is library that you need to import. If you are not sure if the project
is packaged on your distribution, you can check [pkgs.org].

On other packaging systems like [conda] or [homebrew], you will get both
development and runtime packages at the same time. Just be careful with such
systems that the appropriate packages are being picked up instead of the system
installed ones.

For native Windows systems, I do not have any experience there, but I am open
to any contributions for this section.

These variants would typically have a specific configuration and feature subset
of the project. If you find it lacking, you can either raise an issue downstream
at the packagers (there are relevant links in [pkgs.org]), or consider building
from source.

## Source project

:::{admonition} Tl;dr
```console
$ git clone https://github.com/user/awesome-project
```
:::

:::{attention}
If you intend to import the project to be used inside another project, consider
[using `FetchContent`] instead. This part is specifically for using the built
binary in a production setup and for upstream development.
:::

You might already be aware of the homepage and/or git repository where the
project is located, at which point git cloning or downloading the relative
archive is straightforward. Unlike autotools, there is no distinction between
the source from git and archive, so you can start building right away.

If you are still uncertain where the project source is located, take a look at
[pkgs.org], or any other packaging system that you know that has it, like
[PyPI]. Even when you are certain about the project source, it can still be
helpful to check what sources these packaging systems use, as often times they
will show which source/variant are deprecated, e.g. [`pkgconf`] vs
[`pkg-config`], and various patches that the packagers applied to fix upstream
issues.

## Using `FetchContent`

[//]: # (TODO: Synchronize with configure/import.md https://github.com/sphinx-doc/sphinx/issues/11807)

:::{admonition} Tl;dr
```cmake
include(FetchContent)
FetchContent_Declare(awesome-project
        GIT_REPOSITORY https://github.com/user/awesome-project
        GIT_TAG main
        FIND_PACKAGE_ARGS CONFIG
)
FetchContent_MakeAvailable(awesome-project)
```
:::

:::{attention}
If you primarily want the compiled binary, then use the [source] version. This
part is specifically if you want to import the project to be used in another
one downstream, either as a library, precompiler or any other utility used for
building a compiled project.
:::

See the [importing dependencies] section.

## Other build-system

Good luck, you have reached the wild-west. You are mostly on your own now.

Some projects can have other ways of importing the project using [`pkgconf`],
however, for consuming CMake projects, it is greatly discouraged to rely on
these because it cannot contain the same amount of metadata, e.g. for
[c++ modules], it does not contain the compiler used for packaged compiled
library, that would tell the consumer if they need to re-compile the project or
not, but on the other-hand, such information is used when consuming CMake's
[`find_package`].

[packaged]: #packaged-version
[source]: #source-project
[using `FetchContent`]: #using-fetchcontent
[`pkgconf`]: https://github.com/pkgconf/pkgconf
[`pkg-config`]: https://gitlab.freedesktop.org/pkg-config/pkg-config
[c++ modules]: https://en.cppreference.com/w/cpp/language/modules
[conda]: https://conda.io/projects/conda/en/latest/index.html
[homebrew]: https://brew.sh
[pkgs.org]: https://pkgs.org

[CMakeUserPreset]: configure/index.md#cmakeuserpresetsjson
[configuration]: configure/index.md
[importing dependencies]: configure/import.md#importing-dependencies-in-a-cmake-project

[`find_package`]: inv:cmake:cmake:command#command:find_package

[^1]: There is a proposal within CMake to at least unify the dependency backend
      [^2] which would be a pre-requisite for having a unified packaging system
      using CMake. But still it is a long way until there can be a `pip`-like
      interface to install projects.
[^2]: <https://gitlab.kitware.com/cmake/cmake/-/issues/22686>
