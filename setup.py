#Building application as a package itself

from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    req = []
    with open(file_path) as f:
        req = f.readlines()
        req = [r.replace("\n","") for r in req]
        if '-e .' in req:
            req.remove('-e .')
    f.close()        
    return req        


setup(
    name='mlproject',
    version='0.0.1',
    author='Plavak',
    author_email='plavakdas@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
