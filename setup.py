from setuptools import setup, find_packages

setup(
    name="numbers2words",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Giridharan Ponpandi",
    description="Convert numbers to words in Tamil, and English with Indian grouping and international grouping",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/GiridharanPonpandi/numbers2words.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
