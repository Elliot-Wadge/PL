from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Pl_class',
    url='https://github.com/Elliot-Wadge/curve_fit_plus',
    author='Elliot Wadge',
    author_email='ewadge@sfu.ca',
    # Needed to actually package something
    packages=['pl_class'],
    # Needed for dependencies
    install_requires=['numpy','matplotlib'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='E',
    description='a curve fitting routine to do a repetitive fitting routine, also a pl_class to assist in PL analysis',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)