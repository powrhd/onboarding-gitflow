# Onboarding repo
This is a repository for new developers to get started on the workflows used in the organization.

## Installation
Create a conda environment with your preferred Python version (>3). Inside the conda environment, install the dependencies with
```
pip install -r requirements.txt
```

## Running tests
The onboarding repo uses `pytest`() as Python test framework. Run the tests by
```
cd src
python -m pytest
```

## Continuous integration
The tests are run through [a continuous integration workflow](.github/workflows/ci.yml) on different operating systems with different Python versions, upon a Pull Request and changes in main.