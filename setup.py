from setuptools import setup
import os

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(name='configure_gpu',
      version='0.1',
      description='a package for allocating tensorflow gpu memory use in python',
      url='https://github.com/kongaevans/configure_gpu',
      long_description=str(README),
      long_description_content_type="text/markdown",
      author='Evans Kiplagat',
      author_email='evanskiplagat3@gmail.com',
      license='MIT',
      packages=['configure_gpu'],
      zip_safe=False)