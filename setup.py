from setuptools import setup

setup(
    name='stet',
    version='0.1',
    description='A git-powered blog',
    long_description=open('README.md').read(),
    author='Stas Malolepszy',
    author_email='stas@mozilla.com',
    url='http://github.com/stasm/stet',
    license='BSD',
    packages=['stet'],
    classifiers=[
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
