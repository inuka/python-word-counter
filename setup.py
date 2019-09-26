from setuptools import setup, find_packages


setup(
i    name='word_counter',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='',
    description='A simple word counter.',
    long_description=open('README.md').read(),
    zip_safe=False,
)
