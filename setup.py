from setuptools import setup

APP_NAME = "MenuBar Quick Access"
APP = ['menu_status.py']
DATA_FILES = ["menu_contents.json"]
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'iconfile': 'app.icns',
    'CFBundleName': APP_NAME,
    'CFBundleDisplayName': APP_NAME,
    'CFBundleGetInfoString': "Making Sandwiches",
    'CFBundleIdentifier': "com.vbrosseau.menubar-quick-access",
    'CFBundleVersion': "0.1.0",
    'CFBundleShortVersionString': "0.1.0",
    'NSHumanReadableCopyright': u"Valentin Brosseau"
    'packages': [],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)
