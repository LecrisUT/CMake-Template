# Testing the project

:::{admonition} Tl;dr
```console
$ ctest --test-dir ./build-dir
```
:::

Similar to the build step, this step is straightforward as the option above
shows. Here are also a few tips:

## Using presets

Similar to the `buildPreset` you often have `testPreset` that you can execute
as:
```console
$ ctest --preset default
```

You can find a list of them using:
```console
$ cmake --list-preset=test
```

## Listing the tests

You can list tests instead of running them by passing the [`-N`] flag

```console
$ ctest --test-dir ./build-dir -N
```

The tests are often grouped by labels, which you can list using
[`--print-labels`]
```console
$ ctest --test-dir ./build-dir --print-labels
```

These can be combined with [filter tests], to show what tests would be executed.

:::{note}
Some testing backends like [catch] might not have the list of tests available
straightaway, but they should be available after the build stage.
:::

## Filter tests

You have two main methods of filtering tests, by the name using [`-R`]/[`-E`],
or by the label [`-L`]/[`-LE`]. These are parsed as regex that include/exclude
the tests with name or label that match the regex. So for example, if you want
to run only unit tests, this might look like:
```console
$ ctest --test-dir ./build-dir -L "^unit$"
```

## Running in parallel

Use the [`-j`] option with the number of tests to be run in parallel, often
times just `$(nproc)`.

```console
$ ctest --test-dir ./build-dir -j $(nproc)
```

:::{note}
The parallelization of the tests themselves, e.g. due to MPI or OpenMP should
be already handled by ctest when passing [`-j`].
:::

Alternatively, set the [`CTEST_PARALLEL_LEVEL`] environment variable.

[filter tests]: #filter-tests

[`-R`]: inv:cmake:std:cmdoption#ctest.--tests-regex
[`-E`]: inv:cmake:std:cmdoption#ctest.--exclude-regex
[`-L`]: inv:cmake:std:cmdoption#ctest.--label-regex
[`-LE`]: inv:cmake:std:cmdoption#ctest.--label-exclude
[`-j`]: inv:cmake:std:cmdoption#ctest.--parallel
[`-N`]: inv:cmake:std:cmdoption#ctest.--show-only
[`--print-labels`]: inv:cmake:std:cmdoption#ctest.--print-labels
[`configurePreset`]: configure.md#cmake-presets
[`CTEST_PARALLEL_LEVEL`]: inv:cmake:cmake:envvar#envvar:CTEST_PARALLEL_LEVEL

[catch]: https://github.com/catchorg/Catch2
