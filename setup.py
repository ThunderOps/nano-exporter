"""
Raiblocks Prometheus exporter
"""

from setuptools import find_packages, setup

dependencies = ['prometheus-client', 'raiblocks']

setup(
    name='raiblocks-exporter',
    version='0.0.3',
    url='https://github.com/ThunderOps/raiblocks-exporter',
    download_url="https://github.com/ThunderOps/raiblocks-exporter",
    license="Apache License, Version 2.0",
    author='Steven Acreman',
    author_email='sacreman@gmail.com',
    description='Raiblocks Prometheus exporter',
    long_description='Raiblocks Prometheus exporter',
    keywords="Raiblocks Prometheus Exporter",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'raiblocks-exporter = raiblocks_exporter.raiblocks_exporter:main',
        ],
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
    ])
