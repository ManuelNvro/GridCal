# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(933, 528)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.tab)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.frame_4 = QtWidgets.QFrame(self.splitter)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame = QtWidgets.QFrame(self.frame_4)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.open_button = QtWidgets.QPushButton(self.frame)
        self.open_button.setObjectName("open_button")
        self.horizontalLayout_5.addWidget(self.open_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.units_combobox = QtWidgets.QComboBox(self.frame)
        self.units_combobox.setObjectName("units_combobox")
        self.horizontalLayout_5.addWidget(self.units_combobox)
        self.verticalLayout_5.addWidget(self.frame)
        self.sources_list = QtWidgets.QListView(self.frame_4)
        self.sources_list.setObjectName("sources_list")
        self.verticalLayout_5.addWidget(self.sources_list)
        self.normalized_checkBox = QtWidgets.QCheckBox(self.frame_4)
        self.normalized_checkBox.setObjectName("normalized_checkBox")
        self.verticalLayout_5.addWidget(self.normalized_checkBox)
        self.frame_6 = QtWidgets.QFrame(self.splitter)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_10 = QtWidgets.QFrame(self.frame_6)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.autolink_button = QtWidgets.QPushButton(self.frame_10)
        self.autolink_button.setObjectName("autolink_button")
        self.horizontalLayout_7.addWidget(self.autolink_button)
        self.rnd_link_pushButton = QtWidgets.QPushButton(self.frame_10)
        self.rnd_link_pushButton.setObjectName("rnd_link_pushButton")
        self.horizontalLayout_7.addWidget(self.rnd_link_pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.assign_to_all_pushButton = QtWidgets.QPushButton(self.frame_10)
        self.assign_to_all_pushButton.setObjectName("assign_to_all_pushButton")
        self.horizontalLayout_7.addWidget(self.assign_to_all_pushButton)
        self.assign_to_selection_pushButton = QtWidgets.QPushButton(self.frame_10)
        self.assign_to_selection_pushButton.setObjectName("assign_to_selection_pushButton")
        self.horizontalLayout_7.addWidget(self.assign_to_selection_pushButton)
        self.clear_selection_button = QtWidgets.QPushButton(self.frame_10)
        self.clear_selection_button.setObjectName("clear_selection_button")
        self.horizontalLayout_7.addWidget(self.clear_selection_button)
        self.verticalLayout_3.addWidget(self.frame_10)
        self.assignation_table = QtWidgets.QTableView(self.frame_6)
        self.assignation_table.setObjectName("assignation_table")
        self.verticalLayout_3.addWidget(self.assignation_table)
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 3, 1, 1)
        self.set_multiplier_button = QtWidgets.QPushButton(self.frame_9)
        self.set_multiplier_button.setObjectName("set_multiplier_button")
        self.gridLayout.addWidget(self.set_multiplier_button, 0, 0, 1, 1)
        self.set_cosfi_button = QtWidgets.QPushButton(self.frame_9)
        self.set_cosfi_button.setObjectName("set_cosfi_button")
        self.gridLayout.addWidget(self.set_cosfi_button, 0, 1, 1, 1)
        self.multSpinBox = QtWidgets.QDoubleSpinBox(self.frame_9)
        self.multSpinBox.setMinimum(-99999.0)
        self.multSpinBox.setMaximum(99999.0)
        self.multSpinBox.setObjectName("multSpinBox")
        self.gridLayout.addWidget(self.multSpinBox, 0, 2, 1, 1)
        self.setQ_on_cosfi_checkbox = QtWidgets.QCheckBox(self.frame_9)
        self.setQ_on_cosfi_checkbox.setObjectName("setQ_on_cosfi_checkbox")
        self.gridLayout.addWidget(self.setQ_on_cosfi_checkbox, 0, 4, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_9)
        self.horizontalLayout_2.addWidget(self.splitter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.splitter_3 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.frame_8 = QtWidgets.QFrame(self.splitter_3)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tableView = QtWidgets.QTableView(self.frame_8)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_7.addWidget(self.tableView)
        self.PlotFrame = QtWidgets.QFrame(self.splitter_3)
        self.PlotFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PlotFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PlotFrame.setObjectName("PlotFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.PlotFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plotwidget = MatplotlibWidget(self.PlotFrame)
        self.plotwidget.setObjectName("plotwidget")
        self.horizontalLayout.addWidget(self.plotwidget)
        self.horizontalLayout_4.addWidget(self.splitter_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.doit_button = QtWidgets.QPushButton(self.frame_2)
        self.doit_button.setObjectName("doit_button")
        self.horizontalLayout_6.addWidget(self.doit_button)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.open_button.setText(_translate("Dialog", "Import"))
        self.label_5.setText(_translate("Dialog", "Units"))
        self.normalized_checkBox.setText(_translate("Dialog", "normalized"))
        self.autolink_button.setText(_translate("Dialog", "Auto-link"))
        self.rnd_link_pushButton.setText(_translate("Dialog", "Random-link"))
        self.assign_to_all_pushButton.setText(_translate("Dialog", "Assign to all"))
        self.assign_to_selection_pushButton.setText(_translate("Dialog", "Assign to selection"))
        self.clear_selection_button.setText(_translate("Dialog", "Clear selection"))
        self.set_multiplier_button.setText(_translate("Dialog", "Set multiplier"))
        self.set_cosfi_button.setText(_translate("Dialog", "Set cos(φ)"))
        self.setQ_on_cosfi_checkbox.setText(_translate("Dialog", "Set Q on Cos(φ)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Assignation"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Plot"))
        self.doit_button.setText(_translate("Dialog", "Do it"))

from .matplotlibwidget import MatplotlibWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

