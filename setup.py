from setuptools import setup

setup(name="darksky",
      version="2.0",
      description="A wrapper for the Dark Sky (formerly forecast.io) weather API.",
      url="https://github.com/raspberrycoulis/dark-sky-python",
      author="Wesley Archer",
      author_email="hello@wesleyarcher.com",
      license="MIT",
      packages=["darksky"],
      install_requires=["requests"])
