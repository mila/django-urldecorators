
import codecs
from setuptools import setup, find_packages


VERSION = (0, 4)
VERSION_STR = ".".join(map(str, VERSION))


url='http://github.com/mila/django-urldecorators/tree/master'

try:
    long_description = codecs.open('README.rst', "r", "utf-8").read()
except IOError:
    long_description = "See %s" % url


setup(
    name='django-urldecorators',
    version=VERSION_STR,
    description='Django-urldecorators is a reusable Django application which allows apply '
                'view decorators and middleware components depending on requested url.',
    author='Miloslav Pojman',
    author_email='miloslav.pojman@gmail.com',
    url=url,
    packages=find_packages(),
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
