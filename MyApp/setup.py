"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True,
           'iconfile': 'myapp.icns'}

setup(
    app=APP,
    name='罗子豪的小程序',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    py_modules=['MyApp']
)
