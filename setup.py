import sys
import py3minifier
from setuptools import setup
from distutils.command.install import INSTALL_SCHEMES

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']


cmdclass = {'build_py': build_py}

setup(
    name="py3minifier",
    version=py3minifier.__version__,
    description="Python 3 code minifier, obfuscator, and compressor",
    author=py3minifier.__author__,
    cmdclass=cmdclass,
    author_email="support@kortical.com",
    url="https://github.com/kortical/py3minifier",
    license="LICENSE :: OSI APPROVED :: GNU AFFERO GENERAL PUBLIC LICENSE V3",
    packages=['py3minifier'],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    provides=['py3minifier'],
    entry_points = {
        'console_scripts': [
            'py3minifier = py3minifier.__main__:main'
        ],
    },
    test_suite = "tests",
)
