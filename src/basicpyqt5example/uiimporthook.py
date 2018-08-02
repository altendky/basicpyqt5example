import pathlib
import sys

import PyQt5.uic


class UiFinder:
    def find_spec(self, fullname, path, target=None):
        suffix = '_ui'

        if target is not None or not fullname.endswith(suffix):
            return

        _, _, base = fullname.rpartition('.')
        base = base[:-len(suffix)]

        path, = path
        path = pathlib.Path(path)
        py_path = path / (base + suffix + '.py')
        ui_path = path / (base + '.ui')

        with open(py_path, 'w') as py:
            PyQt5.uic.compileUi(ui_path, py, indent=4)


def install_ui_finder():
    sys.meta_path.insert(0, UiFinder())
