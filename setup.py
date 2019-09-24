from setuptools import setup

setup(
    name='tigercopter',
    version='0.1dev',
    packages=['tigercopter',],
    license='MIT',
    long_description=open('README.txt').read(),
    install_requires=[
        'https://github.com/m0rdras/DJITelloPy/archive/v_1.5.tar.gz'
    ]
)
