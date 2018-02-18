import setuptools

setuptools.setup(
    name='basicpyqt5example',
    author="Kyle Altendorf",
    classifiers=[
        ' :: '.join([
            'License',
            'OSI Approved',
            'GNU General Public License v3 or later (GPLv3+)',
        ]),
        'Intended Audience :: Developers',
    ],
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    entry_points={
        'gui_scripts': [
            'basicpyqt5example = basicpyqt5example.__main__:main',
        ],
    },
    install_requires=[
        'pyqt5',
    ],
    extras_require={
        'dev': [
            'gitignoreio',
        ],
    },
)
