import os

from setuptools import setup

__version__ = os.environ.get("GIT_DESCRIBE_TAG", "0.0.0")

setup(
    name="roq",
    version=__version__,
    author="Hans Erik Thrane",
    author_email="thraneh@gmail.com",
    url="https://roq-trading.com/",
    description="Roq Python Samples",
    long_description="",
    ext_modules=ext_modules,
    extras_require={
        "test": "pytest",
    },
    zip_safe=False,
    python_requires=">=3.10",
)
