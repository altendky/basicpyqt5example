basicpyqt5example
======

|Travis build|_ |AppVeyor build|_

This project is meant to provide a working example project covering some basic good
practices.  There is usually room for preference but it's often good to have an example
to start from and then as you learn you can form your own opinions and adjust.

This project is a running PyQt5 application with:

* GUI's defined in and loaded from .ui files made in Qt Designer
* A setup.py to allow installation of the project and it's dependencies such as
  into a virtualenv.
* Tests (pretty pointless at present, but there) using:

  * `Tox`_
  * `Py.Test`_
  * `pytest-qt`_
* Builds and testing on (see badges above for direct build links):

  * AppVeyor_
  * Travis_
* `gitignoreio`_ for managing .gitignore

.. |Travis build| image:: https://travis-ci.org/altendky/basicpyqt5example.svg
   :alt: Travis build status
.. _Travis build: https://travis-ci.org/altendky/basicpyqt5example

.. |AppVeyor build| image:: https://ci.appveyor.com/api/projects/status/4684eguimdh31n2i?svg=true
   :alt: AppVeyor build status
.. _AppVeyor build: https://ci.appveyor.com/project/KyleAltendorf/basicpyqt5example

.. _Tox: https://tox.readthedocs.io/en/latest/
.. _Py.Test: https://docs.pytest.org/en/latest/
.. _pytest-qt: https://pypi.python.org/pypi/pytest-qt
.. _gitignoreio: https://pypi.python.org/pypi/gitignoreio
.. _AppVeyor: https://www.appveyor.com/
.. _Travis: https://travis-ci.org/
