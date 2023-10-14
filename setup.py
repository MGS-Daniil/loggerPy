from setuptools import setup, find_packages

setup(
    name="MGS-Daniil",
    version="0.0.1",
    author="Daniil Chernyak",
    author_email="chernyak.daniil.2010@gmail.com",
    url="https://www.youtube.com/channel/UCWNjclaL2HQ5gDVayqhNEfw",
    description="logging package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["click", "pytz"],
    entry_points={"console_scripts": ["MGS-Daniil = src.main:main"]},
)
