from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')
sys.argv.append('-p')
sys.argv.append('lxml')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True, 'includes': ["lxml", "lxml.etree", "lxml._elementpath"]}},
    console = [{'script': "main2.py"}],
    zipfile = None,
)