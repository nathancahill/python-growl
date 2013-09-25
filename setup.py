from distutils.core import setup

setup(
    name='Growl',
    version='0.7.1',
    author='Nathan Cahill',
    author_email='nathan@nathancahill.com',
    packages=['growl'],
    url='http://pypi.python.org/pypi/Growl/',
    license='LICENSE.txt',
    description='Python interface for the Growl (GNTP) protocol.',
    long_description=open('README.txt').read(),
)
