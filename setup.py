from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT= '-e .'

def get_requires(req_file:str)-> List[str]:
    '''
    this function return the all required packages from requirements.txt file
    '''
    file_obj = open(req_file)
    requirements = file_obj.readlines()
    requirements = [req.replace("\n", "") for req in requirements]
    
    # removing the setup file recalling
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name= "MLOPS_project",
    version= '0.001',
    author= "fardul islam digonto",
    author_email= "fardulislamdigonto799@gmail.com",
    requires=get_requires("requirements.txt")
)