from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["requests>=2.21.0"]

setup(
    name="pr2up",
    version="0.1",
    author="GfnPro",
    author_email="blxcksxvxgesmile@gmail.com",
    description="API pr2up.com",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/scvgde/pr2up_api",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)