from setuptools import setup, find_packages

setup(
    name='honest-validation-toolkit',
    version='0.1.0',
    packages=['honest_validation'],
    install_requires=['numpy', 'pandas'],
    author='Lucas (EventHorizon-IA)',
    description='Lightweight Python library for rigorous time-series validation.',
    long_description="Lightweight Python library for rigorous time-series validation.",
    url='https://github.com/EventHorizon-ia/honest-validation-toolkit',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
