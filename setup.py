from setuptools import setup, find_packages

VERSION = '0.0.3' 
DESCRIPTION = 'The unofficial python api for whatsapp'
LONG_DESCRIPTION = 'This package is a python wrapper for chat-api.com whatsapp API, which allows you to control all aspects of your whatsapp account using python.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="whatsapp-api", 
        version=VERSION,
        author="Ayush Goyal",
        author_email="ayushgoyal.iitkgp@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['requests', 'defcon-utils'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['whatsapp', 'python'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)