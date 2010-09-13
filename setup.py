from setuptools import setup, find_packages

VERSION = (0, 2)
VERSION_STR = ".".join(map(str, VERSION))
 
setup(
    name='django-urldecorators',
    version=VERSION_STR,
    description='Django-urldecorators is a reusable Django application which allows apply '
                'view decorators and middleware components depending on requested url.',    
    author='Miloslav Pojman',
    author_email='miloslav.pojman@gmail.com',
    url='http://github.com/mila/django-urldecorators/tree/master',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
