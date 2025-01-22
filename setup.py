import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="logo2cc",
    version="0.1.0",
    author="Piyush Acharya",
    author_email="verisimilitude11@outlook.com",
    description="Convert images to black and white (no gray) to use as custom logos on Stripe credit cards.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VerisimilitudeX/logo2cc",
    packages=setuptools.find_packages(),
    install_requires=[
        "Pillow"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)