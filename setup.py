from setuptools import setup


setup(
    name = 'aulaglobal-massdownloader',
    packages = ['aulaglobal-massdownloader'],
    version = '1.0',
    description = 'Tiny Python script for automatic download of files hosted in UC3M Moodle web portal AulaGlobal2.',
    author='Jorge R. Canseco',
    author_email='jorrodri@inf.uc3m.es',
    url='https://github.com/jorgerodcan/aulaglobal2-massdownloader',

    classifiers = [
        'Development Status :: 4 - Beta ',
        'Programming Language :: Python ',
        'Programming Language :: Python :: 2.7 '
        'Programming Language :: Python :: 3 ',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2) ',
        'Operating System :: POSIX :: Linux ',
        'Operating System :: MacOS :: MacOS X '],
    install_requires = ['requests', 'beautifulsoup4', 'Unidecode'],

)
#dependency_links=['git+https://github.com/kennethreitz/requests',
#                      'git+https://github.com/kelp404/bs4',
#                      'git+https://github.com/iki/unidecode']
