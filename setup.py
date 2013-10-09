# coding=utf-8
import os
from setuptools import setup, find_packages


def read(*fname):
    with open(os.path.join(os.path.dirname(__file__), *fname)) as f:
        return f.read()


def get_version():
    return "0.0.1"

setup(
    name='django-rest-favorites',
    version=get_version(),
    author=u'sercanu',
    author_email='sercanulucan.dev@gmail.com',
    keywords='django rest',
    url='https://github.com/sercanu/django-rest-favorites',
    packages=find_packages(),
    include_package_data=True,
    description='Django rest farmework sample',
    long_description=read('README.rst'),
    zip_safe=True,
)