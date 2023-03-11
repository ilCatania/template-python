import re

SLUG_VALIDATOR = (
    r"^[a-z][a-z0-9\-]+[a-z0-9]$",
    "letters, numbers and hyphens (-)",
)
"""
Slug validator used for both organization and repository names. They must:
- start with a lowercase letter
- have only lowercase letters, numbers or hyphens (-)
- end with a lowercase letter or number
"""
MODULE_NAME_VALIDATOR = (
    r"^[a-z][a-z0-9_]+[a-z0-9]$",
    "letters, numbers and underscores (_)",
)
"""
Python module names should adhere to
[PEP8](https://peps.python.org/pep-0008/#package-and-module-names), but to be
safe we will be a bit more stringent here, using the same requirement as repo
names with underscores (_) instead of hyphens (-).
"""


validators = [
    ("repository name", "{{ cookiecutter.repo_name }}", SLUG_VALIDATOR),
    ("reposiory organization", "{{ cookiecutter.repo_org }}", SLUG_VALIDATOR),
    (
        "python module name",
        "{{ cookiecutter.module_name }}",
        MODULE_NAME_VALIDATOR,
    ),
]

for (
    field_name,
    field_value,
    (valid_regex, valid_description),
) in validators:
    if not re.match(valid_regex, field_value):
        raise ValueError(
            f"Invalid {field_name}: {field_value}, "
            f"only {valid_description} allowed!"
        )
