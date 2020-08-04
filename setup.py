import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DiffPriv",
    version="0.0.1",
    author="Quantalabs",
    description="A Differential Privacy Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Quantalabs/DiffPriv",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8.1',
)