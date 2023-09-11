from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str] :
    '''
    This function will return the list of required library needs to be installed
    '''
    
    requirements = []
    
    with open('requirements.txt') as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements



setup(
    name = "End to End Machine Learning Project",
    version = "0.0.1",
    author = "Harish Gehlot",
    author_email="gehloth03@gmail.com",
    summary = "Practicing End to End Machine Learning Project using Github Actions",
    
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)