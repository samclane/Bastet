from babel.messages import frontend as babel
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    required = f.read().splitlines()

setup(
    name="bastet",
    version="0.0.0",
    description="An open source application for controlling your LIFX brand lights",
    author="Sawyer McLane",
    author_email="samclane@gmail.com",
    license="MIT",
    packages=find_packages(),
    cmdclass={
        "compile_catalog": babel.compile_catalog,
        "extract_messages": babel.extract_messages,
        "init_catalog": babel.init_catalog,
        "update_catalog": babel.update_catalog,
    },
)
