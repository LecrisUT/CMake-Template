# GitHub Workflows

## Purpose

This is the primary CI interface.

## Configuration

See the `.github/workflows` files.

## Recommendation

Organize the CI jobs in small reusable units such that they can be called on:
push/pull, schedule, and release. This workflow design also allows to reuse the
workflow defined in another project, e.g. you can use the workflows defined in
this template directly.

### Reusable workflows

The main workflow logic are located in `step_<Workflow>.yaml`, which contain
only the `on:workflow_call` interface.

### Main workflows

The main triggering workflows are located in `ci.yaml` and `release.yaml`,
containing the main `on:push/pull/schedule` logic, and the calls to the reusable
workflows.

### Experimental jobs

In order to properly support experimental jobs, you can use [`alls-green`]
action to get the status of the overall CI, without the failure status of the
experimental jobs.

In order to mask the overall status of the CI on the git commits, you can use
[`steps.[*].continue-on-error`] as done in this template. This should not be
used outside of the main branch's git commits.

### Naming

The `name` field of the workflows, as well as the `name` field in the job's name
should be as simple as possible in order to be readable in the checks window.
Don't be shy of using emojis.

Also, setup the `run-name` field to show how and why the CI were triggered.

### Typical workflows

A typical project's workflow should contain:
- pre-commit checks: calls [pre-commit]
- main tests: runs the main ctest
- doc tests: runs other sphinx builders, e.g. `linkcheck`, `html -W`
- static-analysis: in this template it is [sonarcloud]
- code coverage: re-runs each subset of tests with coverage
- release workflow: re-runs the CI tests, and publishes the release to GitHub
  and to other downstream packaging

[pre-commit]: pre-commit.md
[sonarcloud]: TBD

[`alls-green`]: https://github.com/re-actors/alls-green
[`steps.[*].continue-on-error`]: https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepscontinue-on-error
