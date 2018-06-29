from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="masonite-py2js",
    version="0.0.1",
    author="Christopher Byrd",
    author_email="christopher.byrd2013@gmail.com",
    description=(
        "Python to Javascript variable converter " "for the Masonite framework."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChrisByrd14/masonite_py_to_js",
    packages=["py2js", "py2js.transformers"],
    install_requires=["masonite>=2.0.4"],
    classifiers=(
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Natural Language :: English",
    ),
)
