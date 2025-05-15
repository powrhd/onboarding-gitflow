# Onboarding repo
This is a repository for new developers to get started on the workflows used in the organization.

## Installation
Create a conda environment with your preferred Python version (>3). Inside the conda environment, install the dependencies with
```
pip install -r requirements.txt
```

## Development process
In order to make any changes to the repo, please follow this development workflow:
1. Create a branch
1. Make changes in the branch
1. When committing, make sure your pre-commit hooks are active (see below) and that the tests run successfully (see below)
1. After completing your line of changes, open a Pull Request with a meaningful description; you may link issues to the Pull Request (and automatically close them upon merge)
1. Resolve any merge conflicts
1. Make sure all checks complete successfully in your PR (ie., CI, precommit, Sonarcloud, Code Coverage)
1. Ask a coworker to review your Pull Request (this may not always be feasible, as some developers may be the only ones working on the project; however, if possible, PR's should be reviewed within 48 hours of requesting review)
1. "Squash and Merge" the PR to condense the number of commits on the main branch
1. Make sure the checks run successfully on main, after the merge
1. Delete your branch

## Pre-commit hooks
Use [pre-commit hooks](https://pre-commit.com/) to automatically format and lint your code upon any commits. The hooks run when you commit, and will fail if they apply changes to your file ([black](https://black.readthedocs.io/en/stable/)) or find issues ([flake8](https://flake8.pycqa.org/en/latest/)). You then need to resolve the issues, stage the files for commit again, and commit. Once everything is compliant with the hooks, the commit will succeed and you can push to the remote.

To enable pre-commit hooks, you have to run once in your repository, in your terminal:
```
pre-commit install
```
This will enable the hooks in the `.git` folder and after that they are active. Keep in mind that this only happens locally and you need to redo this for any new repo.

## Running tests
The onboarding repo uses `pytest`(https://docs.pytest.org/en/stable/) as Python test framework. Run the tests by
```
cd src
python -m pytest
```

## Continuous integration
The tests are run through [a continuous integration workflow](.github/workflows/ci.yml) on different operating systems with different Python versions, upon a Pull Request and changes in main.