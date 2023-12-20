# Building the project

:::{admonition} Tl;dr
```console
$ cmake --build ./build-dir
```
:::

At this point the build process is more-or-less up to the actual project, and
you simply run the build as shown above. Here are also a few tips:

## Using presets

If you have used a [`configurePreset`] in the previous section, you may not be
aware of the build directory. Often times, the project also provides a
`buildPreset` with the same name, so you can simply run:
```console
$ cmake --build --preset default
```

You can find a list of them using:
```console
$ cmake --list-preset=build
```

## Running in parallel

Use the [`-j`] option, either by itself (the build system decides) or pass
`$(nproc)` as its value.

```console
$ cmake --build ./build-dir -j
```

Alternatively, set the [`CMAKE_BUILD_PARALLEL_LEVEL`] environment variable.

[`-j`]: inv:cmake:std:cmdoption#cmake--build.--parallel
[`configurePreset`]: configure.md#cmake-presets
[`CMAKE_BUILD_PARALLEL_LEVEL`]: inv:cmake:cmake:envvar#envvar:CMAKE_BUILD_PARALLEL_LEVEL
