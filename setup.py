import setuptools

with open("VERSION", 'r') as f:
    version = f.read().strip()

with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
   name='streamdeck-commands-over-network',
   version=version,
   description='Send StreamDeck commands to other computers over an internet connection.',
   author='Etgar Kaspi',
   author_email='etgarkaspi@gmail.com',
   url='https://github.com/HunterAP23/streamdeck_commands-over-network',
   package_dir={'': 'src'},
   packages=setuptools.find_packages(where='src'),
   install_requires=[],
   license="MIT",
   long_description=long_description,
   long_description_content_type="text/markdown",
   include_package_data=True,
)
