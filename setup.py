from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='babyshark',
      version='0.3',
      description="Collection of annoying children's songs generators",
      long_description=long_description,
      url='http://github.com/dbenner/babyshark',
      author='David Ben-Ner',
      author_email='',
      license='GPL',
      packages=['songs'],
      )