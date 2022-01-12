import setuptools

setuptools.setup(
    name="cara_sample_module",
    version="0.0.1",
    author="BroutonLab",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    author_email="hello@caracal.ai",
    package_dir={"": "implementation"},
    packages=setuptools.find_packages(where="implementation"),
    install_requires=[
        "git+https://github.com/caracalai/caracal.git"
    ],
    python_requires=">=3.7",
)
