import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="saveAmebloContents", 
    version="0.0.1",
    author="Satoshi Watanabe",
    author_email="sassy.watanabe@gmail.com",
    description="save ameba blog contents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sassy/saveAmebloContents",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['saveAmebloContents = saveAmebloContents.main:main']
    },
    python_requires='>=3.6',
)