from setuptools import find_packages, setup
from typing import List


hypen_e_dot = '-e .'
def get_requirements(file_path:str)-> List[str]:
   '''this function will return the list of requirements '''
   with open(file_path, 'r') as f:
      req_list = [line.strip() for line in f.readlines()]
      if hypen_e_dot in req_list:
         req_list.remove(hypen_e_dot)
   return req_list
   
   
   
setup(
   name = 'mlproject',
   version = '0.1.0',
   author = 'Likith P',
   author_email = 'likithprasanna@gmail.com',
   packages = find_packages(),
   install_requires = get_requirements('requirements.txt')
)