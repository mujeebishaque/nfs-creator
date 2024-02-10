from setuptools import setup, find_packages

setup(
    name='nfs_creator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
    ],
)

# command to build the python dist: python setup.py sdist bdist_wheel
# command to install the package: pip install dist/nfs_creator-0.1-py3-none-any.whl