from setuptools import setup, find_packages

setup(
    name="virtual_drag",
    version="0.1.0",
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        # Bağımlılıklarınızı buraya ekleyin
    ],
    entry_points={
       'console_scripts': [
            'virtual-drag=virtual_drag.main:main',
        ],
    },
    author="Abdulkerim Akan",
    author_email="kerimakan77@gmail.com",
    description="Virtual drag",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)