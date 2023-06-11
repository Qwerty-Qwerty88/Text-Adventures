from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 3 - Alpha",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Programming Language :: Python :: 3",
    "Topic :: Games/Entertainment"
]
 
setup(
    name="text_adventures",
    version="0.0.1",
    description="A Python library for easily making text adventure games.",
    long_description=open("README.md").read() + "\n\n" + open("CHANGELOG.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Qwerty-Qwerty88/Text-Adventures",  
    author="Qwerty Qwerty",
    author_email="personqwertyperson88@gmail.com",
    license="MIT", 
    classifiers=classifiers,
    packages=find_packages(),
    install_requires=['getkey']
)