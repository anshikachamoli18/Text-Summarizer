import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

__version__="0.0.0"

REPO_NAME='Text-Summarizer'
AUTHOR_USER_NAME="anshikachamoli18"
SRC_REPO='textsummarizer'
AUTHOR_EMAIL="anshikachamoli2004@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A package to summarize text",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"}
        ,
        package_dir={"": "src"},
        packages=setuptools.find_packages(where="src")
)
