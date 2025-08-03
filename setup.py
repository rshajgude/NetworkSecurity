from setuptools import find_packages, setup

from typing import List

def get_requirements()->List[str]:
    """
    This will return all req libraries from requiremenrs file
    """
    requirement_list:list[str]=[]
    try:
        with open('requirements.txt', 'r') as file :
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                # Ignore blank lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
                    
    except Exception as e:
        print("Not able to locate or load requirments.txt file")
    
    return requirement_list


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Raj",
    author_email="rshajgude@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)