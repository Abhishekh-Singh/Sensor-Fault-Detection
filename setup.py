from setuptools import setup,find_packages
from typing import List

def get_requirements()->List[str]:

    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
        return requirements

    

setup(
    name = "sensor",
    version = "0.0.1",
    author = "Abhishek Singh",
    author_email = "singh.abhishekh20@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements(), #["pymongo==4.2.0"],
)