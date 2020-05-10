# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CenteralWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CenteralWidget(object):
    def setupUi(self, CenteralWidget):
        CenteralWidget.setObjectName("CenteralWidget")
        CenteralWidget.resize(630, 666)
        self.gridLayout_2 = QtWidgets.QGridLayout(CenteralWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ImageRemoveAll_btn = QtWidgets.QPushButton(CenteralWidget)
        self.ImageRemoveAll_btn.setMinimumSize(QtCore.QSize(200, 0))
        self.ImageRemoveAll_btn.setObjectName("ImageRemoveAll_btn")
        self.gridLayout_2.addWidget(self.ImageRemoveAll_btn, 1, 2, 1, 1)
        self.SheetList = QtWidgets.QTabWidget(CenteralWidget)
        self.SheetList.setMinimumSize(QtCore.QSize(0, 500))
        self.SheetList.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SheetList.setAutoFillBackground(False)
        self.SheetList.setTabsClosable(False)
        self.SheetList.setObjectName("SheetList")
        self.gridLayout_2.addWidget(self.SheetList, 0, 0, 1, 3)
        self.ImageRemove_btn = QtWidgets.QPushButton(CenteralWidget)
        self.ImageRemove_btn.setMinimumSize(QtCore.QSize(200, 0))
        self.ImageRemove_btn.setObjectName("ImageRemove_btn")
        self.gridLayout_2.addWidget(self.ImageRemove_btn, 1, 1, 1, 1)
        self.ImgaeReload_btn = QtWidgets.QPushButton(CenteralWidget)
        self.ImgaeReload_btn.setMinimumSize(QtCore.QSize(200, 0))
        self.ImgaeReload_btn.setObjectName("ImgaeReload_btn")
        self.gridLayout_2.addWidget(self.ImgaeReload_btn, 1, 0, 1, 1)

        self.retranslateUi(CenteralWidget)
        QtCore.QMetaObject.connectSlotsByName(CenteralWidget)

    def retranslateUi(self, CenteralWidget):
        _translate = QtCore.QCoreApplication.translate
        CenteralWidget.setWindowTitle(_translate("CenteralWidget", "Form"))
        self.ImageRemoveAll_btn.setText(_translate("CenteralWidget", "사진 전체 제거"))
        self.ImageRemove_btn.setText(_translate("CenteralWidget", "사진 제거"))
        self.ImgaeReload_btn.setText(_translate("CenteralWidget", "사진 새로고침"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CenteralWidget = QtWidgets.QWidget()
    ui = Ui_CenteralWidget()
    ui.setupUi(CenteralWidget)
    CenteralWidget.show()
    sys.exit(app.exec_())
