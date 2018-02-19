basicpyqt5example
======

|Travis|_ |AppVeyor|_ |codecov|_

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
* `gitignoreio`_ for managing .gitignore

.. |Travis| image:: https://travis-ci.org/altendky/altendpyqt5.svg
   :alt: Travis build status
.. _Travis: https://travis-ci.org/altendky/altendpyqt5

.. |AppVeyor| image:: https://ci.appveyor.com/api/projects/status/565xmcrd3rl7ark7?svg=true
   :alt: AppVeyor build status
.. _AppVeyor: https://ci.appveyor.com/project/KyleAltendorf/altendpyqt5

.. |codecov| image:: https://codecov.io/gh/altendky/altendpyqt5/branch/develop/graph/badge.svg
   :alt: codecov coverage status
.. _codecov: https://codecov.io/gh/altendky/altendpyqt5

.. _Tox: https://tox.readthedocs.io/en/latest/
.. _Py.Test: https://docs.pytest.org/en/latest/
.. _pytest-qt: https://pypi.python.org/pypi/pytest-qt
.. _gitignoreio: https://pypi.python.org/pypi/gitignoreio
