from setuptools import setup

# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()

# specify requirements of your package here
REQUIREMENTS = []

# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Operating System :: Unix',
    'Environment :: GPU :: NVIDIA CUDA :: 10.0',
    'Environment :: GPU :: NVIDIA CUDA :: 10.1',
    'Environment :: GPU :: NVIDIA CUDA :: 10.2',
    'Environment :: GPU :: NVIDIA CUDA :: 11.0',
    'Environment :: GPU :: NVIDIA CUDA :: 11.1',
    'Environment :: GPU :: NVIDIA CUDA :: 11.2',
    'Environment :: GPU :: NVIDIA CUDA :: 11.3',
    'Environment :: GPU :: NVIDIA CUDA :: 11.4',
    'Environment :: GPU :: NVIDIA CUDA :: 11.5',
    'Programming Language :: Python :: 3.10'
]

# calling the setup function
setup(name='ai-utils',
      version='0.0.1',
      description='A utility tool for the ai team',
      long_description=long_description,
      url='https://github.com/PomVom',
      author='Sharon Cooper',
      author_email='sharon.cooper@pomvom.com',
      license='MIT',
      packages=['geo'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='utils'
      )
