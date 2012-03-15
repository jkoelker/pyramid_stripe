from setuptools import setup, find_packages

version = '0.1'

setup(name='pyramid_stripe',
      version=version,
      description="Stripe helpers for pyramid",
      long_description=open("README.rst").read(),
      keywords='',
      author='Jason K\xc3\xb6lker',
      author_email='jason@koelker.net',
      url='https://github.com/jkoelker/pyramid_stripe',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "pyramid>=1.3a",
          "stripe",
      ],
      entry_points="""
      [paste.app_factory]
      main = pyramid_stripe:main
      """,
      )
