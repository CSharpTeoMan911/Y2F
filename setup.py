from setuptools import setup, find_packages

setup(
    name='Y2F',
    version='1.2',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'Y2F=Y2F_PACKAGE.main:main_entry_point',
        ]
    },
    install_requires=[
        'pytube',
        'ffmpeg',
        'ffmpeg-python'
    ]
)
