'''
The setup.py  file is an essential part of the packaging and distributing Python projects. It is used by setuptools( or distutils in older Python versions) to define the configuration of your project, such as its metadata, dependencies, and more.
'''

from setuptools import find_packages, setup
# find_packages:- This function will scan through all folders and where ever there will be a __init__ file , it will consider that particular folder as a package.
# setup is responsible to provide all the information regarding the projects over here.
from typing import List

def get_requirements()->List[str]:
    # This function will return the list of requirements.
    # Whenever we are creating the entire Python package , it is also necessary to install all the requirements, all the packages that are available inside the requirements.

    requirement_lst:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            print(lines)
            # Process each line
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e.
                if requirement and requirement != '-e .' :
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

# print(get_requirements())


# Setup metadata
setup(
    name="NetworkSecurity",
    version = "0.0.1",
    author = "Aryan Kumar",
    author_email = "giet.aryan227@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)
