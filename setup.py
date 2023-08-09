# building our application as a package itself
from setuptools import find_packages, setup
from typing import List
import os


# Change the current working directory to the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Tony Akalonu',
    author_email='teejayakalonu002@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(os.path.join(script_directory, 'requirements.txt'))

)
