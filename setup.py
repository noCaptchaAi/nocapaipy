from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='nocapaipy',
      version='0.1',
      description='An api wrapper for the captcha solver, Nocaptchaai.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/noCaptchaAi/nocapaipy',
      author='Bernward Sanchez',
      author_email='contact@bern.codes',
      license='MIT',
      packages=['nocapaipy'],
      zip_safe=False)
