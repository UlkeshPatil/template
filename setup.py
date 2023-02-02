from setuptools import setup, find_packages

def get_requirements():
    with open('requirements.txt') as req:
        return [line.strip() for line in req if line.strip() and line.strip() != '-e .']

setup(
    name='template',
    version='0.0.1',
    author='ulkesh',
    author_email='ulkesh13@gmail.com',
    url='',
    packages=find_packages(),
    install_requires=get_requirements(),
)
