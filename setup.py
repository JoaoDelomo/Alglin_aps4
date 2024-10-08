from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.project_name }}",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pygame',  # Dependências do projeto
        # Adicione outras dependências aqui
    ],
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_name }} = {{ cookiecutter.project_name }}.main:main',
        ],
    },
)
