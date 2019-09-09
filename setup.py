# coding: utf-8

"""
    Zuora API Reference
    OpenAPI spec version: 2019-03-20
    Contact: docs@zuora.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "zuora-client"
VERSION = "2.0.3-orm"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]


setup(
    name=NAME,
    version=VERSION,
    description="Zuora API Reference",
    author_email="docs@zuora.com",
    url="",
    keywords=["Swagger", "Zuora API Reference"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
)
