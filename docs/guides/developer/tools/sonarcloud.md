# SonarCloud

Project link: [SonarCloud]

## Purpose

Perform static analysis and track code coverage.

:::{note}
Code coverage is not as customizable as with [codecov], however, it calculates
code coverage including the if-statement branching, while the latter only
calculates line coverage.
:::

## Configuration

See the `sonar-project.properties` file.

## Recommendation

Reuse the artifacts of the test/coverage, but currently it is unclear how to
design that.

[SonarCloud]: https://www.sonarsource.com/products/sonarcloud/

[codecov]: codecov.md
