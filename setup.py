
import codecs
from setuptools import setup


url='http://github.com/mila/django-urldecorators/tree/master'

try:
    long_description = codecs.open('README.rst', "r", "utf-8").read()
except IOError:
    long_description = "See %s" % url


setup(
    name='django-urldecorators',
    version='0.6',
    description='Django-urldecorators is a reusable Django application which allows apply '
                'view decorators and middleware components depending on requested url.',
    author='Miloslav Pojman',
    author_email='miloslav.pojman@gmail.com',
    url=url,
    packages=['urldecorators', 'urldecorators.tests'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    long_description=long_description,
)
