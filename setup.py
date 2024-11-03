from setuptools import setup, find_packages

setup(
    name="tamil_tts",
    version="0.1",
    packages=find_packages(),
    description="A Tamil Text-to-Speech generation package",
    install_requires=[
        "transformers",
        "torch",
    ],
    author="Thirumalai G",
    author_email="thirutechdeveloper@example.com",
    url="https://github.com/Thirumalai-Tech-Developer/Text_To_Audio",
    include_package_data=False,
    package_data={
        "": ["config/*.json", "config/*.safetensors"]
    }
)
