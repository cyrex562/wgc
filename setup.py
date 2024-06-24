from setuptools import setup

setup(
    name="wgc",
    version="0.1.0",
    py_modules=["wgc"],
    install_requires=[
        "click","pyyaml","loguru","jsonpickle",
    ],
    entry_points={
        "console_scripts": [
            "wgc = wgc:cli",
        ],
    },
)