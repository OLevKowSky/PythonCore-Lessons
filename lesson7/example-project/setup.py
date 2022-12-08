from setuptools import setup, find_packages


setup(
    name="example project",
    version="0.0.1",
    packages = find_packages(include=["example-project"]),

    install_requires = [
        "Django",
        "Pillow",
        "pandas==1.1"
        "pytest>=2.2"
    ],

    extra_require = {
        "interactive": ["matplotlib>1"]
    },

    entry_points={
        "main_page": ["hello.example.com"]
    },

    setup_requires = ["pytest-runner", "flake8"],
    test_require = ["pytest"],

    package_data = {"example-project": ["data\schema.json"]}
)