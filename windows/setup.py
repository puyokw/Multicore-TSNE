import numpy
from setuptools import setup
from distutils.command.install import install as DistutilsInstall
import sys
import os

'''
    Just because I wanted .so file to be built same way for python and torch
    we exec cmake from cmd here.
'''


class MyInstall(DistutilsInstall):
    def run(self):
        os.system(
            'cp ../multicore_tsne/Release/tsne_multicore.dll python/tsne_multicore.dll')
        DistutilsInstall.run(self)


setup(
    name="MulticoreTSNE",
    version="0.1",
    description='Multicore version of t-SNE algorithm.',
    author="Dmitry Ulyanov (based on L. Van der Maaten's code)",
    author_email='dmitry.ulyanov.msu@gmail.com',
    url='https://github.com/DmitryUlyanov/Multicore-TSNE',
    install_requires=[
        'numpy',
        'psutil',
        'cffi',
    ],

    packages=['MulticoreTSNE'],
    package_dir={'MulticoreTSNE': 'python'},
    package_data={'MulticoreTSNE': ['tsne_multicore.dll']},
    include_package_data=True,

    cmdclass={"install": MyInstall},
)
