from setuptools import setup, find_packages
import os

APP = ['src/main.py']
DATA_FILES = [
    ('resources', ['src/resources/background.jpg', 'src/resources/obstacle.png', 'src/resources/player.png', 'src/resources/projectile.png']),
    ('', ['motorbike.ico', 'identifier.sqlite']),
]
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'motorbike.ico',
    'packages': ['pygame'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
