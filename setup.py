from setuptools import setup, find_packages

setup(
    name='crypto_pay_api_cryptobot',
    version='1.0.1',
    author='sshlg',
    author_email='sshlg93@gmail.com',
    description='A Python library for interacting with Crypto Pay API by CryptoBot',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ssheleg/crypto-pay-api-python',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests',
        'Flask', 
    ],
)