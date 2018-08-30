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


import inspect
def ui(path=None):
    def decorator(cls):
        if path is None:
            ui_path = pathlib.Path(inspect.getmodule(cls).__file__).with_suffix('.ui')
        else:
            ui_path = path

        Ui, UiBase = PyQt5.uic.loadUiType(ui_path)

        if cls.__bases__ != (object,):
            raise Exception('tsk-tsk, multiple inheritance')

        if type(cls) is not type:
            raise Exception('sorry, gotta have our own metaclass')

        cls.__bases__ += (UiBase,)

        original_init = cls.__init__

        def __init__(self, *args, **kwargs):
            super(cls, self).__init__()

            self.ui = Ui()
            self.ui.setupUi(self)

            original_init(self, *args, **kwargs)

        cls.__init__ = __init__

        return cls

    return decorator


@ui()
class MainWindow:
    def __init__(self):
        self.ui.actionSystem_Info.triggered.connect(
            drop_args(self.open_system_info),
        )
        self.system_info_dialogs = []

    def open_system_info(self):
        dialog = basicpyqt5example.systeminfo.SystemInfoDialog(self)
        dialog.finished.connect(drop_args(self.close_system_info, dialog))
        dialog.show()
        self.system_info_dialogs.append(dialog)

    def close_system_info(self, dialog):
        self.system_info_dialogs.remove(dialog)
        print(
            'removed {}, still have {}'.format(dialog, self.system_info_dialogs)
        )
