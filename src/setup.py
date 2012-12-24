'''
Created on Jan 15, 2011

@author: vahid
'''

from setuptools import setup

import os
import re

# reading package version (same way sqlalchemy does)
with open(os.path.join(os.path.dirname(__file__),'mongodb_tool.py')) as v_file:
    module_version = re.compile(r".*__version__ = '(.*?)'",re.S).match(v_file.read()).group(1)


setup(
    name="Cherrypy-MongoDB",
    version=module_version,
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
