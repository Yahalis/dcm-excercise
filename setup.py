from setuptools import setup, find_packages

setup(name='dynamic_campaign',
      version='0.0.2',
      description='Dynamic campaign excercise',
      author='Yahali Sherman',
      author_email='yahalis@gmail.com',
      packages=find_packages(),
      install_requires=[
            'holidays'
      ],
      zip_safe=False)
