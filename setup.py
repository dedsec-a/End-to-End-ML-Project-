
from typing import List

from setuptools import find_packages, setup

def get_requirements(file_path):
    with open(file_path) as file:
        requirements = file.read().splitlines()
        # Remove '-e .' if it's included in requirements.txt
        requirements = [req for req in requirements if req != "-e ."]
    return requirements

setup(
    name='End_to_End_ML_Projects',  # Removed spaces for compatibility
    version='0.0.1',
    author="Harsh Kumar",
    author_email="replytobambam@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # Reads requirements from file
)
