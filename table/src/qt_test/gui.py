import pkg_resources
import sys

from PyQt5 import uic
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import QApplication, QTableView

from .user import User, UserStore


class UserTableModel(QAbstractTableModel):
    def __init__(self, store):
        super().__init__()
        self._store = store

    def rowCount(self, parent=None):
        if not parent.isValid():
            return len(self._store)
        else:
            return 0

    def columnCount(self, parent=None):
        if not parent.isValid():
            return 3
        else:
            return 0

    def data(self, index, role=Qt.DisplayRole):
        user = sorted(self._store.users())[index.row()]
        attr = {
            0: 'first_name',
            1: 'last_name',
            2: 'uid'
        }[index.column()]
        return getattr(user, attr)


def create_user_store():
    store = UserStore()
    store.add(User('Bubba', 'Gump', 1234))
    store.add(User('James', 'Kirk', 2345))
    store.add(User('Lother', 'Hillman', 3456))
    return store


def setup_table(store, table_view):
    model = UserTableModel(store)
    table_view.setModel(model)


def main():
    app = QApplication(sys.argv)
    mainwindow = uic.loadUi(
        pkg_resources.resource_filename(
            'qt_test', 'ui/mainwindow.ui'))
    table_view = mainwindow.findChild(
        QTableView,
        'tableView')

    store = create_user_store()
    setup_table(store, table_view)
    mainwindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
