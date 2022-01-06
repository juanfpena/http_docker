from setuptools import setup, find_packages

setup(
    name="custom",
    version="0.1.0",
    author="Carlos Gitto & Juan Peña",
    author_email="carlosgitto98@gmail.com & juanfacundopena@gmail.com",
    packages=[
        "custom",
        "custom.functions",
        "custom.SQL_models"
    ],
    description="useful functions and engine",
    long_description=open("README.md").read(),
    install_requires=open("requirements.txt").read().split("\n"),
)
