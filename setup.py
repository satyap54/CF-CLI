from setuptools import setup


setup(
    name='cf',
    version='1.0',
    install_requires=[
        'Click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        cf =cli:main
    ''',    
)
