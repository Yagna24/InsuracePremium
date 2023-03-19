from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    
    with open('requirements.txt', 'r') as r_file:
        requirement_list = r_file.readlines()
    
    remove_package = "-e ."
    print('requirement_list',requirement_list)
    requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]     
    if remove_package in requirement_list : 
        requirement_list.remove(remove_package)
    
    
    return requirement_list


setup(name='InsurancePremium',
    version='0.0.1',
    description='Insurance_usingIndusTools',
    author='yagnaa',
    author_email='yagnathakkar1224@gmail.com',
#   url='https://github.com/Yagna24/InsuracePremium/',
    packages = find_packages(),
    install_requires = get_requirements()
    )