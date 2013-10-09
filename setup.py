#!/usr/bin/env python
from setuptools import setup, find_packages


def get_version():
    return "0.0.1"


setup(name='django-oscar',
      version=get_version().replace(' ', '-'),
      url='https://github.com/sercanu/django-rest-favorites',
      author="sercan",
      author_email="",
      description="",
      keywords="Django",
      license='BSD',
      platforms=['linux'],
      packages=find_packages(exclude=["sandbox*", "tests*"]),
      include_package_data=True,
      install_requires=[
          'Django==1.5.4',
          'django-braces==1.2.2',
          'django-model-utils==1.5.0',
          'logutils==0.3.3',
          'djangorestframework==2.3.8',
          'markdown==2.3.1',
          'django-filter==0.7',
          'coverage==3.6',
          'django-discover-runner==1.0',
          'Sphinx==1.2b1',
          'dj-database-url==0.2.2',
          'dj-static==0.0.5',
          'static==0.4',
      ],
      # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Topic :: Other/Nonlisted Topic']
      )
