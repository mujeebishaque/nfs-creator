from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
)

# command to build the python dist: python setup.py sdist bdist_wheel