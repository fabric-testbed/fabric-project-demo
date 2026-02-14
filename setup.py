from setuptools import setup, find_packages

setup(
    name="fabric-demo",
    version="0.1.0",
    description="A sample library for demonstrating private-to-public releases",
    author="FABRIC Testbed",
    author_email="admin@fabric-testbed.net",
    url="https://github.com/fabric-testbed/fabric-project-demo",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
