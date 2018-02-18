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


import sys

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
