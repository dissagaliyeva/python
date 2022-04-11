from setuptools import setup, find_packages

# call setup function
setup(
    author='Dinara Issagaliyeva',
    description='A complete package for linear regression.',
    name='mysklearn',
    version='0.1.0',
    packages=find_packages(include=['mysklearn', 'mysklearn.*']),
    # install_requires=['pandas', 'scipy', 'matplotlib'],
    install_requires=[
        'pandas>=1.0',
        # 'matplotlib>=2.2.1,<3' # bigger than 2.2.1 but < 3
    ]
)

# run pip freeze > requirements.txt
# to get the current versions of each downloaded library

# run > python setup.py sdist bdist_wheel
# to build the project

# run > twine upload dist/*

