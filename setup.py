from setuptools import setup, find_packages

"""
    Step 1. build with: py setup.py sdist
    Step 2. for publishing to pypi:
        twine upload --repository pypi dist/*
        username: __token__
        password: [PYPI_TOKEN]
"""

setup(
    name='word-translator-py',
    version='0.0.7',
    author='Guillermo Rodolfo Ellison',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    py_modules=['setup', 'word_translator_client', 'translation_as_console_table']
)
