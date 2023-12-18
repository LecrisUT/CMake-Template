# Who is the user?

## Not the end-user

The end-user of the project should not have to build the project directly using
CMake, not even if the project is a library that is meant to be used by other
downstream projects. For these situations the user should have access to
packaged versions of the project (Fedora, PyPI, homebrew package etc.) See
the [developer guide] on how to set it up.

[developer guide]: ../developer/index.md

## User interacting with CMake

For the context of this guide, we are focusing on the user who would actually
have to interact with CMake. Each kind of users will have different level of
familiarity with CMake and needs for using it. Throughout this guide there will
be relevant notes that are particularly important to a subset of people, e.g.:

[//]: # (TODO: Is it possible to link the tab-item back to this page?)

> #### How do I configure the project?
> ::::{tab-set}
> :::{tab-item} As an end-user
> Here is the most basic instructions
> :::
> :::{tab-item} As an upstream developer
> Here is how you can make your life easier
> :::
> :::{tab-item} As a downstream packager
> Beware of the packaging guidelines
> :::
> ::::

### End-user

Ok, I've lied, there are situations when the end-user would need to build the
project from source, e.g. when the packaged project does not include the
features you need. Nevertheless, even here the user will have a bare minimum
interaction with CMake, and it is assumed they will not have to interact with it
(at least in the context of building your project) after this.

### Upstream developer

Here the upstream developer refers to the day-to-day developer of the current
project that uses this guide's template. Other developers that would be
importing the current project are considered to be an [end user].

This type of developer would not be handling the build-system, the project CI,
or any other bells-and-whistles that are implemented with this template.
Instead, their main goal is to maintain the main C/C++ (or other language) code.

### Packager

The final type of user of this guide is the rarest, of them all, and they should
be having the most experience with CMake itself. Nevertheless, there are a few
nuances that they should be aware of regarding the modern CMake design
implemented here.

Even so, in this guide, I will not be assuming any prior CMake expertise, even
when the sections are aimed primarily for this group of people, and hopefully at
the end of this guide, you should be able to interact with any CMake project
old-or-new, in any packaging environment. I will not be explaining much of the
CMake inner-workings more than it is relevant, and if you are interested in that
check the [developer guide] as well.

[end user]: #end-user
[developer]: #upstream-developer
[packager]: #packager
