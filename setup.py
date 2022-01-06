from setuptools import setup

setup(
    name="custom",
    version="0.1.0",
    author="Carlos Gitto & Juan Peña",
    author_email="carlosgitto98@gmail.com & juanfacundopena@gmail.com",
    packages=[
        "custom"
    ],
    description="useful functions and engine",
    long_description=open("README.md").read(),
    install_requires=open("requirements.txt").read().split("\n"),
)