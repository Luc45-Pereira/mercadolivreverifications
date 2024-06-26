from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mercadolivresdk",
    version="0.0.3",
    author="Lucas Pereira de Lima",
    author_email="lucaspereiradelima94@gmail.com",
    description="biblioteca para integração com a API do Mercado Livre de forma facilitada",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Luc45-Pereira/mercadolivresdk",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests",
        "pydantic"
    ],
)
