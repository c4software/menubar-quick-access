from setuptools import setup

APP = ['menu_status.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': [],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
