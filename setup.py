from setuptools import find_packages, setup

from typing import List

hyphen_dot = "-e ."
def get_requirements(file_path:str)-> list[str] :
    '''
    This function returns list of requirements
    '''
    requirements= []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n","") for req in requirements]
    
        if hyphen_dot in requirements:
            requirements.remove(hyphen_dot)
    return requirements


setup(
    name= "ML_Project",
    version = "0.0.1",
    author= "Aujasvi",
    author_email= "aujas.chaudhry@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')


)
