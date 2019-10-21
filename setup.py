from setuptools import setup, find_packages

setup(
    name='max-files-per-commit-hook',
    version='0.0.1',
    url='https://github.com/truckpad/max-files-per-commit-hook',
    license='MIT',
    license_file='LICENSE',
    author='TruckPad Dev Team',
    author_email='devs@truckpad.com.br',
    description='Hook to limit max files on a single commit',
    install_requires=['gitpython'],
    packages=find_packages('.'),
    entry_points={
        'console_scripts': [
            'max-files-per-commit = max_files_per_commit_hook.hook:main',
        ],
    },
)
