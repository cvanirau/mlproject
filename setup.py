# will find out all the packages avilable in entire ML directory
from setuptools import find_packages,setup 

from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()  # reading lines in the file 
        # after reading it will detect '\n' we have to replace it with blank
        requirements=[req.replace("\n","") for req in requirements] 

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

# all the parameters that is basically required
setup(
name='mlproject',
version='1.0',
author='Rahul Ranjan',
author_email='rahulranjan3110@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)