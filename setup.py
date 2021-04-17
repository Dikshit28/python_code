from distutils.core import setup  # Need this to handle modules
import py2exe
import pkg_resources
from subprocess import call

setup(
    options={'py2exe': {'bundle_files': 1, 'compressed': True}},
    console=[{'script': "Updateallpythonlibrariesatonce.py"}],
    zipfile=None,
)
# NOT WORKING AS OF NOW
