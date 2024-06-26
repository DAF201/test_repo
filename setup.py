import setuptools

setuptools.setup(
    name='pkg',
    version='0.0.1',
    description='N/A',
    author='N/A',
    author_email='N/A@N/A.com',
    url='https://github.com/DAF201/test_repo',
    download_url='https://github.com/DAF201/test_repo',
    install_requires=[],
    packages=['pkg'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
    ],
    entry_points={
        'console_scripts': [
            'pkg=pkg.main:main',
        ],
    },
    python_requires=">=3",
)
