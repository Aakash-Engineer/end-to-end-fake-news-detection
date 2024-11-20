import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REPO_NAME = 'end-to-end-fake-news-detection'
AUTHOR = 'Aakash-Engineer'
AUTHOR_EMAIL = 'aakashpal1183@gmail.com'
SRC_REPO = 'src'

__version__ = '0.0.0'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="Fake News Detection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Aakash-Engineer/end-to-end-fake-news-detection',
    project_urls={
        'Bug Tracker': 'https://github.com/Aakash-Engineer/end-to-end-fake-news-detection/issues',
    },
    package_dir={"": 'src'},
    packages=setuptools.find_packages(where='src')
)