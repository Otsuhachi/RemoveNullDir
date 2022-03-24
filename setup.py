from setuptools import find_packages, setup

with open('LICENSE', 'r', encoding='utf-8') as f:
    lcs = f.read()
setup(
    name='otsurmnulldir',
    version='1.0.0',
    url='https://github.com/Otsuhachi/RemoveNullDir',
    description='Recursively delete empty folders from 1 to <max_depth> hierarchy, with the current directory as 0 hierarchy.',
    author='Otsuhachi',
    author_email='agequodagis.tufuiegoeris@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Natural Language :: Japanese',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'License :: OSI Approved :: MIT License',
    ],
    license=lcs,
    keywords='Python remove directory',
    entry_points={
        'console_scripts': [
            'rmnulldir = otsurmnulldir.remove_null_dir:main',
        ],
    },
)
