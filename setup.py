from setuptools import setup

setup(
    name="pybreaker",
    version="1.0.2",
    description="Python implementation of the Circuit Breaker pattern",
    long_description=open("README.rst", "r").read(),
    keywords=["design", "pattern", "circuit", "breaker", "integration"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
    ],
    platforms=["Any"],
    license="BSD",
    author="Daniel Fernandes Martins",
    author_email="daniel.tritone@gmail.com",
    url="http://github.com/danielfm/pybreaker",
    package_dir={"": "src"},
    py_modules=["pybreaker"],
    include_package_data=True,
    install_requires=["typing_extensions>=3.10.0; python_version < '3.8'"],
    zip_safe=False,
    python_requires=">=3.7",
    test_suite="tests",
    tests_require=["mock", "fakeredis==2.14.1", "redis==4.5.5", "tornado"],
)
