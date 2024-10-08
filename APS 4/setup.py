from setuptools import setup, find_packages

setup(
    name="APS_4",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pygame',
        'numpy',
        'arrow==1.3.0',
        'binaryornot==0.4.4',
        'certifi==2024.8.30',
        'chardet==5.2.0',
        'charset-normalizer==3.3.2',
        'click==8.1.7',
        'cookiecutter==2.6.0',
        'idna==3.10',
        'Jinja2==3.1.4',
        'markdown-it-py==3.0.0',
        'MarkupSafe==3.0.0',
        'mdurl==0.1.2',
        'Pygments==2.18.0',
        'python-dateutil==2.9.0.post0',
        'python-slugify==8.0.4',
        'PyYAML==6.0.2',
        'requests==2.32.3',
        'rich==13.9.2',
        'six==1.16.0',
        'text-unidecode==1.3',
        'types-python-dateutil==2.9.0.20241003',
        'urllib3==2.2.3'
    ],
    entry_points={
        'console_scripts': [
            'aps_4 = aps_4.main:main',
        ],
    },
)
