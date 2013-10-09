# coding=utf-8
import os
import re
from setuptools import setup, find_packages


def read(*fname):
    with open(os.path.join(os.path.dirname(__file__), *fname)) as f:
        return f.read()


def get_version():
    for line in read('django-rest-favorites', '__init__.py').splitlines():
        m = re.match(r"__version__\s*=\s'(.*)'", line)
        if m:
            return m.groups()[0].strip()
    raise Exception('Cannot find version')


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