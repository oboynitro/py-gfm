from setuptools import setup, find_packages

setup(
    name='py-gfm',
    version='1.0.0',
    description='An implementation of Github-Flavored Markdown written as an '
                'extension to the Python Markdown library.',
    author='Dart Team, Alexandre Macabies',
    author_email='misc@dartlang.org',
    url='https://github.com/zopieux/py-gfm',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['markdown~=3.0'],
    data_files=[('', ['LICENSE'])],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Text Processing :: Markup',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
