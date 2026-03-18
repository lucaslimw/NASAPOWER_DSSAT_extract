from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='nasapower_dssat',
      version='0.1',
      description='A package to extract NASA POWER data for DSSAT',
      author='Lívia B. Pereira',
      long_description=readme,
      long_description_content_type='text/markdown',
      author_email='livia.pereira@usp.br',
      keywords="nasa power, dssat, climate data, agriculture",
      packages=['nasapower_dssat'],
      install_requires=['pandas', 'requests'],)