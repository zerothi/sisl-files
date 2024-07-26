[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://www.mozilla.org/en-US/MPL/2.0/)


# sisl-files

This is a test-farm for files related to testing
[sisl](https://github.com/zerothi/sisl).


## Workflow

The workflow of this repository is, well, non-standard.

1. There are 2 branches which should be used.
   - `main` (complete test file storage)
   - `stripped` (actually used files in `sisl`)
2. If a new test needs to be added, one should:
   - add all files for a given test (as single commits, see further down)
     to the branch named `main`
   - create a PR against `main`.
   - then once that is in, one should cherry-pick onto `stripped`
     of the files from the tests that are
     to be used in the actual tests.
   - create a PR against `stripped` (with only the cherry-picked commits).

The main idea behind this is that the repository is heavily used
by CI executions, meaning there is a high bandwidth requirement.
Since this is an open-source project there are limitations as
to how much data there can be fetched every month.

This means that one will never do *any* commits in `stripped` (which
are test related).  
Only cherry-picks against `stripped` should be done.


### Adding a test

Adding a *new* test requires that we adhere to some standards.

This enables us to faster figure out *why* things have changed
over the course of new program versions. And it also
allows one to faster redo tests, or even delete tests
if they become obsolete.

Each test needs to retain a very strict layout:

1. It should have its own directory located in the
  code it represents. E.g. `<code-name>/<test-name>`.
2. Each test folder should contain a `README.md` file describing
  the following details:

  - system information (as much as possible)
  - which version of the code was used
  - date-stamp of the run
  - which additional files are required, and how to obtain them.
    This could encompass pseudo-potentials, or files otherwise
    shipped with the software (no need to fill with
    easily obtained files).
    Ideally, links to the files should be present, or a description
    on how to obtain them.
    (Please refer to each codes `<code-name>/README.md` which may contain
    this information).  
    Please see in the `static` folder whether some files can already
    be located.
  - A test which requires several runs should have sub-folders
    which should be thoroughly documented in the `README.md` file
    on their relation, order of execution, etc.
  - a small example of how to run the test should be given in the
    end

To add files in the repo, please do it like this:

    cd <test-name>
    git add README.md
    git commit -m "Added README.md for test=<test-name>"
    <path-to-git-root>/commit_single.sh

The above will ensure that *all* files are added as single commits,
with a predefined commit message.

> The reason for doing single-file commits is that it makes it
> trivial to update the `stripped` branch with single files to be tested
> against.
> Over the course of `sisl` development, it has been obvious that
> new file-support in `sisl` can trivially be tested by already
> having access to them through tests done.
> Hence the *2-fold* structure with *complete* tree of files, and
> a stripped version of the files that are actually tested.


### Cherry-picking from `main` to `stripped`

The workflow to add files from `main` to `stripped` would be
something like this:

There is a `<path-to-git-root>/cherry_pick.sh` which can
be used to shortcut the explanation below.

Do this:
1. Checkout `main`.
2. Navigate to the files you wish to move to the stripped
   folder.
3. Call the `cherry_pick.sh` command with the files as arguments.

      <path-to-git-root>/cherry_pick.sh siesta.out siesta.ORB_INDX

   the script will automatically sort the cherry-picks, and only
   take the *missing* cherry-picks that edits those files.


## Internal development

Basically there should never be anything required to be in the `stripped`
branch which isn't already in the `main` branch. So we will
only ever use `stripped` for cherry-picks. There should never be
any information there that is useful for anybody to see.  
One need not cherry-pick the readme files etc.
Only files that are to be *tested*!


## Usage

If you find the test-files useful for other kinds of tests.
Feel free to follow this repository.


## License

See `LICENSE` in the top folder.
We are using the MPL-2.0 license.
