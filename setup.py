from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str)-> List[str]:
    """This function will return the list of requirements"""
    requirements=[]
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("#")]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="ML-CI-CD-Pipeline",
    version="0.1.0",
    author="Vivek Deshmukh",
    author_email="vivek.deshmukh@live.com",
    description="A sample ML CI/CD pipeline project",
    packages=find_packages(),
    # install_requires=[
    #     "numpy",
    #     "pandas",
    #     "seaborn"   ],

    install_requires = get_requirements("requirements.txt")
)