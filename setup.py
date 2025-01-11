from setuptools import setup, find_packages

setup(
    name="furigana_info",
    version="0.1.0",
    description="Library to fetch readings from furigana.info",
    author="asfrgrtgd",
    author_email="",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "requests>=2.0",
        "beautifulsoup4>=4.0"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)