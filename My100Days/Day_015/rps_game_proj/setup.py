from setuptools import setup, find_packages

setup(
    name = "rps15",  
    author='Rebecca Pike',
    packages=find_packages(where='src'),
    package_dir={'':'src'},
    install_requires=['pandas']
)