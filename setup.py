from setuptools import setup, find_packages

# build with: py setup.py sdist
setup(
    name='word-translator-py',
    version='0.0.4',
    author='Guillermo Rodolfo Ellison',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    py_modules=['setup', 'word_translator_client']
)
