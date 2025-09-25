from {{cookiecutter.project_slug}}.main import greet

def test_greet():
    """Test the greet function."""
    assert greet("Python") == "Hello, Python!"
