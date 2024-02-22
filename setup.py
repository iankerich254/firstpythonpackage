from setuptools import setup, find_packages

setup(
    name='firstpythonpackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/iankerich254/firstpythonpackage.git',
    author='<Ian Kerich>',
    author_email='<iankerich254@gmail.com>'
)