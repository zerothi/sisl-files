# sisl-files
Test files and other large files part of the sisl-suite

This repository is mainly intended as a submodule for sisl
to be able to test files in the `pytest` scheme.  
Because I try to keep the sisl repository to a minimum it is necessary
to host such _large_ files in other repositories so they are not part
of the standard distribution.

## Structure of test files

To make it simpler to sustain a framework for keeping files, files should be
stored in the following way:

1. Test-files should be self-contained with the input that created the test.

   > This ensures that one can redo tests, and/or rerun them for later versions.
   > Say, when the output style has changed.

   Files that should be intentionally left out of test folders:
   - pseudo potential files that are easily located elsewhere

     > These files should be placed at the top-level in `pseudo/<code>` directory
     > so one does not have to re-package them everytime.
     > Once present in the `pseudo/<code>` folder, one can create symlinks in the
     > folder where it is used.

2. Each test should be placed in a separate folder where the test output should be used.
   For instance, `siesta` runs should be placed in `tests/sisl/io/siesta/<test-name>`.

   When the test also creates output for other programs (say it produces Wannier90 output),
   one should create another `tests/sisl/io/wannier90/<test-name>` (note the same name!)
   and provide symlinks where necessary.

3. Each test folder should contain a `README.md` describing the details of the test.

   1. Name of test
   2. What it is meant to test (special flags, etc.)
   3. How it should be runned.
   4. Every change of files should be documented here, why, how, and what changed.
      This also means that the first set of files should be documented, and which
      version of the programs created them.

4. If a test has multiple consecutive runs in order for it to complete, then sub-folders
   should be used in that folder:

   ```shell
   ../<test-name>/elec1/
   ../<test-name>/elec2/
   ../<test-name>/transiesta/
   ../<test-name>/transiesta/tbtrans
   ```
   this should reflect their order of execution.

5. This repo has 2 branches, `full` and `main`.
   The `full` repo should contain *all* output files from a test.
   And the `main` repo should only contain the files used in the actual
   tests.

   Thoughts:
   > It might be nice that every output file has a separate commit.
   > This would mean that one could very easily move it to the `main`
   > repo by a simple cherry-pick.


## Limits of file sizes

The GitHub repositories are limited to contain files of 100 MB, so it is imperative
to keep files to a minimum size. This should be considered at all times.

## git lfs

This repository makes use of Git LFS command to make large file storage better.

