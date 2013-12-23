import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as rst:
    README = rst.read()
with open(os.path.join(here, 'CHANGES.rst')) as rst:
    CHANGES = rst.read()

requires = [
    'pyramid',
    'pyramid_jinja2',
    'waitress',
    'pyspkac',
    ]

setup(name='spackdemo',
      version='0.0',
      description='spackdemo',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi pyramid certificate authentication spkac',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='spackdemo',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = spackdemo:main
      """,
      )
