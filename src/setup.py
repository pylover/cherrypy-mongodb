'''
Created on Jan 15, 2011

@author: vahid
'''

from setuptools import setup, find_packages

__version__ = '0.1'

setup(
    name="Cherrypy-MongoDB",
    version=__version__,
    packages=find_packages(),
    install_requires=['pymongo>=2.2'],
    include_package_data=True,
    exclude_package_data={
        '':['.svn', '*/.svn']},
    author="Vahid Mardani",
    author_email="vahid.mardani@gmail.com",
    description="MongoDb Tool For Cherrypy",
    zip_safe=False,
    keywords="Cherrypy MongoDB Tool PyMongo",
    url="https://github.com/pylover/cherrypy-mongodb",
    long_description="MongoDb Tool For Cherrypy",
    classifiers=[
        "Development Status :: 0.0.5 - Pre Alpha"],
)
