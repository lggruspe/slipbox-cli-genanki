from pathlib import Path
import setuptools

setuptools.setup(
    name="slipbox-cli-genanki",
    version="0.0.0",
    author="Levi Gruspe",
    author_email="mail.levig@gmail.com",
    description="Slipbox CLI command for converting notes to Anki flashcards",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/lggruspe/slipbox-cli-genanki",
    packages=setuptools.find_packages(),
    package_data={
        "slipbox-cli-genanki": ["py.typed"],
    },
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=["genanki==0.11.0", "genbu==0.2.1", "slipbox>0.16.0"],
    python_requires=">=3.8",
)
