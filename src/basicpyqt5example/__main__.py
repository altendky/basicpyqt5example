# See file COPYING in this source tree
__copyright__ = 'Kyle Altendorf'
__license__ = 'GPLv3+'

#   This file is part of Basic PyQt5 Example.
#
#   Basic PyQt5 Example is free software: you can redistribute it and/or
#   modify it under the terms of the GNU General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Basic PyQt5 Example is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Basic PyQt5 Example.  If not, see
#   <http://www.gnu.org/licenses/>.


import logging
import pathlib
import sys
import tempfile
import traceback

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
# Consider if you want a fresh file each time or a running log.
# mode='w' -> fresh file
# mode='a' (or no mode specified) -> running log
logs_to_try = (
    'log',
    pathlib.Path.home()/'log',
    'temp',
)
for log in logs_to_try:
    if log == 'temp':
        log = tempfile.NamedTemporaryFile(
            prefix='log-{}-'.format(__file__),
            delete=False,
        )
        log.close()
        log = log.name

    try:
        file_handler = logging.FileHandler(log, mode='w', encoding='utf-8')
        break
    except PermissionError:
        continue

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


def excepthook(excType=None, excValue=None, tracebackobj=None):
    logger.critical(''.join(traceback.format_exception(
        etype=excType,
        value=excValue,
        tb=tracebackobj,
    )).strip())


sys.excepthook = excepthook
logger.critical('Logging sys.excepthook installed')
logger.critical('Import in progress for {}'.format(pathlib.Path(__file__).resolve()))
logger.critical('sys.argv: {}'.format(sys.argv))


# Uncomment to test that you can at least see this in the logfile
# raise Exception('you should see this')



import PyQt5.QtWidgets

import basicpyqt5example.mainwindow


def main():
    app = PyQt5.QtWidgets.QApplication(sys.argv)

    main_window = basicpyqt5example.mainwindow.MainWindow()
    main_window.ui.show()

    app.exec()

    return 0


if __name__ == '__main__':
    sys.exit(main())
