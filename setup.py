import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
    "torch",
    "opencv-python",
    "scikit-image"
]

setuptools.setup(
    name="torch_videovision",
    version="0.0.1",
    author="hassony2",
    author_email="author@example.com",  # TODO
    description="This package implements several basic data-augmentation transforms for pytorch video inputs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hassony2/torch_videovision",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements
)
