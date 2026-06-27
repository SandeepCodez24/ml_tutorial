from setuptools import find_packages, setup
from typing import List



def get_requirements(file_path: str)-> List[str]:
    # This function returns the list of requirement packages for install_requires.
    requirements: List[str] = []
    with open(file_path) as file_obj:
        for line in file_obj:
            requirement = line.strip()
            if not requirement or requirement.startswith('#'):
                continue
            if requirement.startswith('-e '):
                continue
            if '#' in requirement:
                requirement = requirement.split('#', 1)[0].strip()
                if not requirement:
                    continue
            requirements.append(requirement)
    return requirements


setup(

name='ml_project',
version='0.0.1',
author='sandeep',
author_email='sandeepcodez24@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

) #meta data of entire project