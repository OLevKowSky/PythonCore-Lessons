from setuptools import setup

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()


setup(
    name="our_project",
    version="0.0.1",
    author="developer",
    author_email="author@gmail.com",
    description='this is our very usefull program',
    long_description=long_description,
    url="my_site.com",
    project_urls={
        "Bugs": "project bug url"
    },
    classifiers=[
        "Python version :: Python :: 3",
        "License ::OSI Approved :: MIT License",
        "Operating System :: Linux"
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7"
)
