from setuptools import setup, find_packages
import codecs
from os import path

here = path.abspath(path.dirname(__file__))


def long_description():
    with codecs.open('README.rst', encoding='utf8') as f:
        return f.read()

setup(
    name='rsttst',
    version='0.1.5',

    description='rsttst makes your reStructuredText testable',
    long_description=long_description(),

    # The project's main homepage.
    url='https://github.com/willemt/rsttst',
    author='willemt',
    author_email='himself@willemthiart.com',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System :: Logging',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='development logging',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['pygments', 'docutils'],
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [
            'rsttst = rsttst.__main__:main',
        ],
    },
)
