from setuptools import setup

setup(
    name='dsss_hw5',
    version='0.1.0',    
    description='Homework 5 Python package',
    url='https://github.com/luis1230majo/dsss_hw5.git',
    author='Luis Cervantes',
    author_email='luis.b.cervantes@fau.de',
    license='Apache License 2.0',
    packages=['dsss_hw5'],
    install_requires=['mpi4py>=2.0',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache License',  
        'Operating System :: POSIX :: Windows',        
        'Programming Language :: Python :: 3.8.8',
    ],
)