from setuptools import setup, find_packages

setup(
    name="anondrop",
    version="0.1.2",
    author="BubblePlayz",
    author_email="mylaptop4768@gmail.com",
    description="A package for uploading and deleting files using AnonDrop API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/BubblePlayzTHEREAL/AnonDrop",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests",
    ],
)
