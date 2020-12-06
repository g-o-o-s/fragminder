
from setuptools import setup

setup(
    name="fragminder", 
    version="0.0.1",
    author="Travis Mick",
    author_email="root@lo.calho.st",
    description="Discord bot for reminding CS:GO players to take StatTrak screenshots",
    url="https://github.com/tmick0/fragminder",
    packages=['fragminder'],
    python_requires='>=3.6',
    install_requires=['requests>=2.25,<3', 'discord>=1.0,<2', 'aiosqlite>=0.16,<0.17'],
    entry_points={"console_scripts": ["fragminder=fragminder.main:main"]}
)
