# {{ cookiecutter.repo_name }}

{{ cookiecutter.project_description }}

## Installation

Install _{{ cookiecutter.repo_name }}_ with `pip`:

```console
$ pip install {{cookiecutter.repo_name}}
```

then check that your installation is correct by importing the main module:

```console
$ python -c 'import {{ cookiecutter.module_name }}'
```


## Development

After creating your own virtual environment, install
_{{ cookiecutter.repo_name }}_ for development by using editable mode and the
appropriate extras:

```console
$ python -m venv venv
$ source venv/bin/activate
$ pip install -e .[dev,tests]
```
