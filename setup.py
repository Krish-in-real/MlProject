from setuptools import find_packages,setup
from typing import List

HUPHEN_E_DOT = '-e.'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path)as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if HUPHEN_E_DOT in requirements:
            requirements.remove(HUPHEN_E_DOT)

setup(
name = 'MlProjest',
version = '0.0.1',
author='Krish',
author_email='Krishinreal@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),

)