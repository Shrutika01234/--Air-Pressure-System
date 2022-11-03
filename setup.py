from pkg_resources import Requirement
from setuptools import find_packages, setup
from typing import List

def get_requirments()->List[str]:
    """
    This function will return list of requirment

    """
    requirement_list:list[str] = []

    """
    write a code to read requirments.txt file and append each frequirment in requirement_list variable
    """
    return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="Shrutika",
    author_email="shrutika01234@gmail.com",
    packages=find_packages(),
    install_requires=get_requirments(),#["pymongo==4.2.0"]
)