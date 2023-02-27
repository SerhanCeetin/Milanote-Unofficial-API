import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="milanote-unofficial-api",
    packages=setuptools.find_packages(),
    version="1.0.0",
    license="MIT",
    description="The Unofficial Milanote API in Python.",
    author="Serhan Çetin",
    author_email="ceetinserhan@gmail.com",
    url="https://github.com/SerhanCeetin/Milanote-Unofficial-API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    download_url="https://github.com/SerhanCeetin/Milanote-Unofficial-API/tarball/master",
    keywords=["milanote", "python3", "api", "unofficial", "milanote-api", "milanote api"],
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Home Automation",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)