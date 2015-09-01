
'''
Setup script.
To install lizard:
[sudo] python setup.py install
'''

from setuptools import setup, find_packages
import os

def install(appname):

    with open(os.path.join(os.path.dirname(__file__), 'README.md')) as fobj:
        readme = fobj.read()

    setup(
          name = appname,
          version = "0.0.1",
          description = '''A tool for testing if you are in the spam folder''',
          long_description =  readme,
          url = 'https://github.com/nerds-odd-e/google-spam-checker',
          download_url='https://pypi.python.org/spam-checker/',
          license='MIT',
          platforms='any',
          classifiers = ['Development Status :: 5 - Production/Stable',
                     'Intended Audience :: Developers',
                     'Intended Audience :: End Users/Desktop',
                     'License :: Freeware',
                     'Operating System :: POSIX',
                     'Operating System :: Microsoft :: Windows',
                     'Operating System :: MacOS :: MacOS X',
                     'Topic :: Software Development :: Quality Assurance',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3.2',
                     'Programming Language :: Python :: 3.3'],
          py_modules = ['spam_checker'],
          author = 'Terry Yin',
          author_email = 'terry@odd-e.com',
          scripts = ['spam-checker']
          )

if __name__ == "__main__":
    import sys
    install('spam-checker')
