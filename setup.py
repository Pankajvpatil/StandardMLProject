from setuptools import setup, find_packages

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path):
    with open(file_path) as f:
        requirements = f.read().splitlines()
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="StandardMLProject",
    version="0.1.0",
    packages=find_packages(),
    author="Pankaj Patil",
    author_email="pankajv.patil@gmail.com",
    install_requires=get_requirements("requirements.txt")
)


