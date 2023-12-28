from setuptools import setup, find_packages

# build with: py setup.py sdist
setup(
    name='word_translator_py',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['setup', 'word_translator_client']
)
