from setuptools import find_packages,setup

def get_package(file_path):

    requirement = []
    with open(file_path) as f:
        requirement = f.readlines()
        requirement = [i.replace('\n','') for i in requirement]

        if '-e .' in  requirement:
            requirement.remove('-e .')
    return requirement

    

setup(
    name="Diabetes predictor",
    version='0.0.1',
    author='Tafique Hossain Khan',
    author_email='tafiquehossain2003@gmail.com',
    package_data=find_packages(),
    install_requirement = get_package("requirement.txt")
)