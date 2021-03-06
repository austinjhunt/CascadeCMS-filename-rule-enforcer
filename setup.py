import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-cascade8-filename-enforcer", # Replace with your own username
    version="0.0.3",
    author="Austin Hunt",
    author_email="huntaj@cofc.edu",
    description="A Python package utilizing the Cascade CMS 8 REST API to enforce file name rules, namely 1) all lowercase, 2) spaces replaced with hyphens, 3) no trailing spaces",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/austinjhunt/CascadeCMS-filename-rule-enforcer",
    project_urls={
        "Bug Tracker": "https://github.com/austinjhunt/CascadeCMS-filename-rule-enforcer/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "requests"
    ]
)