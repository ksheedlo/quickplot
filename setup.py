# Try getting setup from setuptools first, then distutils.core.
# http://goo.gl/BC32zk (StackOverflow)
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Scientific/Engineering :: Visualization'
    ]

setup(
    name = "quickplot",
    packages = ['quickplot'],
    version = "0.1.2",
    description = "The batteries-included plotting wrapper for matplotlib",
    author = "Ken Sheedlo",
    author_email = "ovrkenthousand@gmail.com",
    url = "https://github.com/ksheedlo/quickplot",
    download_url = "https://github.com/ksheedlo/quickplot/archive/master.zip",
    classifiers = classifiers,
    dependency_links = ['https://github.com/matplotlib/matplotlib/tarball/v1.3.x#egg=matplotlib-1.3.0'],
    install_requires = [
        "numpy >= 1.5.0",
        "matplotlib >= 1.3.0"
        ]
    )
