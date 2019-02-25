"""Config file."""
from setuptools import setup

setup(
    name='python3-authjwt',
    version='0.0.1',
    description='Flask JWT auth security for Appengine',
    url='https://github.com/claudiokc/python3-authjwt',
    author='Claudio J. Cáceres',
    author_email='catocaceres@hotmail.com',
    license='MIT',
    packages=['python3-authjwt'],
    install_requires=['PyJWT', 'google-cloud-datastore'],
    zip_safe=False
)
