from setuptools import setup, find_packages
 
setup(
    name='django-urldecorators',
    version='0.1',
    description='Django-urldecorators is a reusable Django application which allows apply '
                'view decorators and middleware components depending on requested url.',    
    author='Miloslav Pojman',
    author_email='miloslav.pojman@gmail.com',
    url='http://github.com/mila/django-urldecorators/tree/master',
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
