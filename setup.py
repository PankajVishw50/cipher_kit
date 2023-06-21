from setuptools import setup

with open("app/Readme.md", "r") as file:
    long_description = file.read()

setup(
    name="cipher_kit",
    version="0.0.2",
    description="Module which helps in encryption and decryption",
    author="Pankaj",
    author_email="pankaj.vishw.dev@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PankajVishw50/cipher_kit",
    py_modules=["cipher_kit"],
    package_dir={"": "app"},
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License"

    ],
    extra_requires={
        "dev": [
            "pytest>=7.0.0",
        ]
    }

)