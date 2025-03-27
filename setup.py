from setuptools import setup, find_packages

setup(
    name='your_python_app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'your-command = your_module:main_function',
        ],
    },
)
