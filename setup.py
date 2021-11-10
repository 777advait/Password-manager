import setuptools
from shutil import rmtree

setuptools.setup( 
    name='PyPassword', 
    version='1.0', 
    author='Advait Jadhav', 
    description='A CLI Password Manager that can save your passwords securely in images using Steganography. The program can also generate strong passwords for your use.', 
    packages=setuptools.find_packages(), 
    entry_points={ 
        'console_scripts': [ 
            'pypassword = PyPassword.__main__:main' 
        ] 
    }, 
    classifiers=[ 
        'Programming Language :: Python :: 3', 
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent', 
    ], 
)

dirs = ["build", "dist", "PyPassword.egg-info"]

for dir in dirs:
	rmtree(dir)