"""
setup.py is the main file to define this
package
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="memory-pyofiler",
    version="0.0.1",
    author="Ryan Siu",
    author_email="findme@ryansiulw.com",
    description="Prometheus-based memory profiler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RyanSiu1995/memory-pyofiler",
    project_urls={
        "Bug Tracker": "https://github.com/RyanSiu1995/memory-pyofiler/issues",
    },
    install_requires=[
        "prometheus-client",
        "objgraph",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
