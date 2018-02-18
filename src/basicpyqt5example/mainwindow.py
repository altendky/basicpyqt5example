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


import pathlib

import PyQt5.uic

import basicpyqt5example.systeminfo


def drop_args(target, *args, **kwargs):
    def f(*_, **kw):
        kw.update(kwargs)
        target(*args, **kw)

    return f


class MainWindow:
    def __init__(self):
        self.ui = PyQt5.uic.loadUi(
            pathlib.Path(__file__).parents[0] / 'mainwindow.ui',
        )

        self.ui.actionSystem_Info.triggered.connect(
            drop_args(self.open_system_info),
        )
        self.system_info_dialogs = []

    def open_system_info(self):
        dialog = basicpyqt5example.systeminfo.SystemInfoDialog()
        dialog.ui.finished.connect(drop_args(self.close_system_info, dialog))
        dialog.ui.show()
        self.system_info_dialogs.append(dialog)

    def close_system_info(self, dialog):
        self.system_info_dialogs.remove(dialog)
        print(
            'removed {}, still have {}'.format(dialog, self.system_info_dialogs)
        )
