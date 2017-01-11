"""Install setup."""
import setuptools

setuptools.setup(
    name="samr_proteomics",
    version="0.0.1",
    url="git@github.com:xguse/samr_proteomics.git",

    author="Gus Dunn",
    author_email="w.gus.dunn@gmail.com",

    description="A short description of the project.",
    # long_description=open('README.rst').read(),

    packages=setuptools.find_packages('src'),
    package_dir={"": "src"},


    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    entry_points={
    "console_scripts": [
        "samr_proteomics = samr_proteomics.cli.main:run",
        ]
    },
)
