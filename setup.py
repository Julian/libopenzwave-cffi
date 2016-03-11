import os

from setuptools import find_packages, setup

try:
    import __pypy__
except ImportError:
    cffi_requirement = ["cffi>=1.0.0"]
else:
    cffi_requirement = []


with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    long_description = readme.read()

classifiers = [
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy"
]

setup(
    name="libopenzwave-cffi",
    packages=find_packages(),
    setup_requires=["vcversioner", cffi_requirement],
    cffi_modules=["libopenzwave/build.py:ffi"],
    vcversioner={"version_module_paths": ["libopenzwave/_version.py"]},
    author="Julian Berman",
    author_email="Julian@GrayVines.com",
    classifiers=classifiers,
    description="CFFI bindings for OpenZWave",
    license="MIT",
    long_description=long_description,
    url="https://github.com/Julian/libopenzwave-cffi",
)
