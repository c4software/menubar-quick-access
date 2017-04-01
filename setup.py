from setuptools import setup

APP_NAME = "MenuBar Quick Access"
APP = ['menu_status.py']
DATA_FILES = ["menu_contents.json"]
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "Quick Access StatusBar Menu",
        'CFBundleIdentifier': "com.vbrosseau.menubar-quick-access",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
        'NSHumanReadableCopyright': u"Valentin Brosseau"
    },
    'iconfile': 'app.icns',
    'packages': [],
}

setup(
    name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)
