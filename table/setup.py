import io
import os
import re
from setuptools import setup, find_packages


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


long_description = read('README.rst', mode='rt')

setup(
    name='table_test',
    version=find_version('src/table_test/version.py'),
    packages=find_packages('src', exclude=['contrib', 'docs', 'test*']),
    author='Sixty North AS',
    author_email='austin@sixty-north.com',
    description='Testing out PyQt5',
    license='MIT',
    keywords='',
    url='http://github.com/sixty-north/qt-test',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
    ],
    platforms='any',
    include_package_data=True,
    package_dir={'table_test': 'src/table_test'},
    package_data={'table_test': ['ui/*.ui']},
    install_requires=[
        'PyQt5',
    ],
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax, for
    # example: $ pip install -e .[dev,test]
    extras_require={
        # 'dev': ['check-manifest', 'wheel'],
        # 'doc': ['sphinx', 'cartouche'],
        'test': ['hypothesis', 'pytest'],
    },
    entry_points={
        # 'console_scripts': [
        #    'table_test = table_test.cli:main',
        # ],
    },
    long_description=long_description,
)
