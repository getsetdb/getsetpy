from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='getsetpy',
    version='1.2.1',
    url='https://github.com/getsetdb/getsetpy',
    license='MIT',
    author='manan',
    author_email='manan.yadav02@gmail.com',
    description='official Python connector for GetSetDB',
    packages=find_packages(exclude=['docs', 'tests']),
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='getsetpy getsetdb connector database',
    classifiers=[
        'Topic :: Database',
        'Topic :: Database :: Front-Ends',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
