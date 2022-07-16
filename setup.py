from setuptools import setup, find_packages

setup(
    name='montecarlo',
    version='1.0.0',
    url='https://github.com/domdecanio/montecarlo',
    author='Dominick DeCanio',
    author_email='domdecanio@gmail.com',
    description='Features 3 classes to create and analyze Monte Carlo simulations.',
    packages=['montecarlo'],    
    install_requires=['numpy >= 1.11.1', 'pandas >= 1.4.2', 'matplotlib >= 1.5.1'],
)