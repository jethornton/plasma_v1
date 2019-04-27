from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow
from qtpy.QtCore import Slot
from qtpy.QtWidgets import QAbstractButton
from PyQt5.QtSql import QSqlDatabase

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

import os
current_path = os.path.dirname(os.path.realpath(__file__)) + '/'

import plasma_v1.tools as tools

class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(current_path + 'plasma.db')
        if db.open():
            print("Connection success !")
        else:
            print("Connection failed !\n{}".format(db.lastError().text()))
        tools.toolsSetup(self)

    @Slot(QAbstractButton)
    def on_mainNavBtns_buttonClicked(self, button):
        self.mainStkWidget.setCurrentIndex(button.property('page'))

    @Slot(QAbstractButton)
    def on_sideNavBtns_buttonClicked(self, button):
        self.sideStkWiget.setCurrentIndex(button.property('page'))

    @Slot(QAbstractButton)
    def on_droNavBtns_buttonClicked(self, button):
        self.droStkWidget.setCurrentIndex(button.property('page'))

    @Slot(QAbstractButton)
    def on_holeNavBtns_buttonClicked(self, button):
        self.holeOps1Stk.setCurrentIndex(button.property('page'))
        self.holeOps2Stk.setCurrentIndex(button.property('page'))

    @Slot(QAbstractButton)
    def on_notifyNavBtns_buttonClicked(self, button):
        self.notifyStkWidget.setCurrentIndex(button.property('page'))


    def on_exitAppBtn_clicked(self):
        self.app.quit()

