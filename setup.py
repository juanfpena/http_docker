from setuptools import setup

setup(
    name="models & functions & CLI",
    version="0.1.0",
    author="Carlos Gitto & Juan Peña",
    author_email="carlosgitto98@gmail.com & juanfacundopena@gmail.com",
    packages=[
        "SQL_models",
        "functions",
        "CLI_command"
    ],
    description="CLI commands to interact with database",
    long_description=open("README.md").read(),
    install_requires=open("requirements.txt").read().split("\n"),
)