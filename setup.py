from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='PL_pkg',
    url='https://github.com/Elliot-Wadge/curve_fit_plus',
    author='Elliot Wadge',
    author_email='ewadge@sfu.ca',
    # Needed to actually package something
    packages=['PL_pkg'],
    # Needed for dependencies
    install_requires=['numpy','matplotlib'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='E',
    description='PL_class to assist with data analysis',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)