from setuptools import setup, find_packages

setup(
    name="python_expression_runner",
    version="0.1.0",
    description="A symbolic computation library for Python expression evaluation.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Eli",
    author_email="wangyongqing@wangyongqing@dzensaas.com",
    url="https://github.com/FXFOP/python_expression_runner",
    packages=find_packages(),
    install_requires=["sympy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
