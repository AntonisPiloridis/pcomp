from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='pcomp',
  version='1.0.1',
  description='Possible combinations - Python Library',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Antonis Piloridis',
  author_email='antonispiloridis@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='combinations', 
  packages=find_packages(),
  install_requires=[''] 
)