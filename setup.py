from setuptools import find_packages, setup

setup(
    name='kivymd',
    version='0.1.0,dev0',
    description='icon font from KivyMD project',
    packages=find_packages(include=["kivymd"], ),
    package_dir={"kivymd": "kivymd", },
    package_data={
        "kivymd": [
            "fonts/*.ttf",
        ]
    },
)
