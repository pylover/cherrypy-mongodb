'''
Created on Jan 15, 2011

@author: vahid
'''

from setuptools import setup
from mongodb_tool import __version__ as module_version
__version__ = module_version

setup(
    name="Cherrypy-MongoDB",
    version=__version__,
    py_modules=['mongodb_tool'],
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
