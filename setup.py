from setuptools import setup, find_packages

setup(
    name='sparkdea',
    version='0.0.1',
    license='Apache License 2.0',
    author="Matthew Mutiso",
    author_email='',
    packages=["sparkdea"],
    package_dir={'': '.'},
    url='https://github.com/mmutiso/dea',
    keywords='spark pyspark dataframe hdfs hadoop data-science',
    install_requires=[
          'pyspark',
      ],

)