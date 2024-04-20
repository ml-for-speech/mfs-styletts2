from setuptools import setup, find_packages

with open("README.md", "r") as f:
    longdesc = f.read()
setup(
    name="mfs-styletts2",
    version="1.0.0",
    author="ML for Speech",
    description="Unofficial pip package for StyleTTS 2",
    long_description=longdesc,
    long_description_content_type="text/markdown",
    url="https://github.com/ml-for-speech/mfs-styletts2",
    packages=find_packages(),
    install_requires=[
        "SoundFile",
        "torchaudio",
        "munch",
        "torch",
        "pydub",
        "pyyaml",
        "librosa",
        "matplotlib",
        "accelerate",
        "transformers",
        "einops",
        "einops-exts",
        "tqdm",
        "typing",
        "typing-extensions",
        "gradio",
        "openphonemizer",
        "cached-path",
        "txtsplit",
        "flask-cors",
    ],
)
