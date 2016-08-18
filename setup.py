from setuptools import setup

setup(
    name='quicklauncher',
    description='quicklauncher is a simple menu to find and launch Maya commands and user scripts.',
    version='3.0.0',
    license='The MIT License',
    author='Cesar Saez',
    author_email='cesarte@gmail.com',
    url='https://www.github.com/csaez/quicklauncher',
    py_modules=["quicklauncher"],
    test_suite='tests',
    tests_require=["mock"],
)
