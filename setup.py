from setuptools import setup

setup(name='cbpi4_pixtendv2s',
      version='0.0.1',
      description='CraftBeerPi4 Plugin for PiXtendV2S',
      author='the-beerengineer',
      author_email='accounts+github@hschlaak.de',
      url='https://github.com/the-beerengineer/cbpi4_pixtendv2s',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4_pixtendv2s': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4_pixtendv2s', 'pixtendv2s'],
     )