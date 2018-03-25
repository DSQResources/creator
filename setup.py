from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = ''.join(f.readlines())

setup(
    name='dsq-creator',
    version='0.1',
    keywords='github repositories sieve projects community',
    description='Script to automatically create repositories from specification of question',
    long_description=long_description,
    author='Marek Suchánek',
    author_email='marek.suchanek@fit.cvut.cz',
    license='MIT',
    url='https://github.com/DSQResources/creator',
    zip_safe=False,
    packages=find_packages(),
    package_data={
        'repocribro': [
            'templates/*.md',
            'templates/resources/*.md',
        ]
    },
    entry_points={
        'console_scripts': [
            'dsq-creator = creator:cli',
        ],
    },
    install_requires=[
        'configparser',
        'click',
        'jinja2',
        'requests',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Communications',
        'Topic :: Internet',
        'Topic :: Software Development',
        'Topic :: Software Development :: Version Control',
    ],
)