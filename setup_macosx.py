"""
This is a setup.py script generated by py2applet

No guarantees for working!

Usage:
    python setup_macosx.py py2app
"""

from setuptools import setup
import os
from glob import glob

APP = ['WikidPad.py']
OPTIONS = {'argv_emulation': True, 'iconfile': '/Applications/WikidPad-2/WikidPad.icns'}

DATA_FILES = [('icons', glob(os.path.join('icons', '*.*'))),
#                 ('lib', glob('sql_mar.*')),
          ('extensions', glob('extensions/*.*')),
          ('extensions/wikidPadParser', glob('extensions/wikidPadParser/*.*')),
          ('', ['WikidPad.xrc', 'readme_Wic.txt', 'gadfly.zip',
              'langlist.txt', 'appbase.css'] + glob('WikidPad_*.po')),
          ('WikidPadHelp', glob(os.path.join('WikidPadHelp', '*.wiki'))),
          (os.path.join('WikidPadHelp', 'data'),
              glob(os.path.join('WikidPadHelp', 'data', '*.*'))),
          (os.path.join('WikidPadHelp', 'files'),
              glob(os.path.join('WikidPadHelp', 'files', '*.*'))),
          ('export', [])]

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    package_dir={'': 'lib'},
    packages= ['pwiki', 'pwiki.wikidata', 'pwiki.wikidata.compact_sqlite',
              'pwiki.wikidata.original_gadfly',
              'pwiki.wikidata.original_sqlite', 'pwiki.timeView',
              'pwiki.rtlibRepl'],
# py_modules=['encodings.utf_8', 'encodings.latin_1'],
)
