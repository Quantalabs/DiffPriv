import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DiffPriv",
    version="v1.0.3",
    author="Quantalabs",
    description="A Differential Privacy Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Quantalabs/DiffPriv",
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["diffpriv=DiffPriv.cli:run"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=' >= 3.8.1',
)
