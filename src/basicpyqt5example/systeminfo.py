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

import PyQt5.QtCore
import PyQt5.uic
import sip

import basicpyqt5example.systeminfo_ui


system_info = f'''\
sys.version: {sys.version}
sys.platform: {sys.platform}
QT_VERSION_STR: {PyQt5.QtCore.QT_VERSION_STR}
PYQT_VERSION_STR: {PyQt5.QtCore.PYQT_VERSION_STR}
SIP_VERSION_STR: {sip.SIP_VERSION_STR}'''


class SystemInfoDialog(PyQt5.QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = basicpyqt5example.systeminfo_ui.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.label.setText(system_info)
