from setuptools import setup, find_packages

setup(
    name="freostudio_fibo",
    version="0.0.1",
    description=(
        "freso-studio，test packaging fibo"
    ),
    long_description=open("README.rst").read(),
    author="freostudio",
    author_email="1600690028@qq.com",
    maintainer="freostudio",
    maintainer_email="1600690028@qq.com",
    packages=find_packages(),
    url="https://github.com/freostudio/fibo",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)