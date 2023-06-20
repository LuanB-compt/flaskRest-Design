from setuptools import find_packages, setup

setup(
    name="flask-api",
    version="1.0",
    description="",
    author="Luan Bruno Domingues de Oliveira",
    install_requires = [
        "setuptools"
    ],
    packages=find_packages(
        where='.',
        include='*'
    )
)