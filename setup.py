from setuptools import setup

with open('README.md', 'r') as f:
    long_desc = f.read()

setup(
    name='corona.py',
    packages=['corona'],
    version='0.0.1',
    license='MIT',
    description='An asynchronous wrapper for the corona.lmao.ninja API written in Python with Discord.py plugin.',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    author='NANI',
    author_email='nani@ksoft.si',
    url='https://github.com/AndyTempel/corona.py',
    keywords=['coronavirus', 'covid-19', 'corona-statistics'],
    install_requires=[
        'aiohttp',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
