import shutil
from pathlib import Path

project_dir = Path().resolve()  # generated project directory

# {% if cookiecutter.include_unit_test_example == 'no' %}
# delete example unit test file and related code
project_dir.joinpath("tests/__files/example_test_file.txt").unlink()
shutil.rmtree(project_dir / "tests/unit")
# {% endif %}
