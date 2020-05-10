# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XpaNewDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_XpaNewDialog(object):
    def setupUi(self, XpaNewDialog):
        XpaNewDialog.setObjectName("XpaNewDialog")
        XpaNewDialog.resize(436, 231)
        XpaNewDialog.setMinimumSize(QtCore.QSize(436, 231))
        XpaNewDialog.setMaximumSize(QtCore.QSize(10000, 10000))
        self.verticalLayout = QtWidgets.QVBoxLayout(XpaNewDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.GridLayout = QtWidgets.QGridLayout()
        self.GridLayout.setObjectName("GridLayout")
        self.FileName_lbl = QtWidgets.QLabel(XpaNewDialog)
        self.FileName_lbl.setMinimumSize(QtCore.QSize(250, 0))
        self.FileName_lbl.setMaximumSize(QtCore.QSize(250, 16777215))
        self.FileName_lbl.setObjectName("FileName_lbl")
        self.GridLayout.addWidget(self.FileName_lbl, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(XpaNewDialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.GridLayout.addWidget(self.frame_2, 5, 0, 1, 2)
        self.frame = QtWidgets.QFrame(XpaNewDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.GridLayout.addWidget(self.frame, 3, 0, 1, 2)
        self.Working_lbl = QtWidgets.QLabel(XpaNewDialog)
        self.Working_lbl.setMinimumSize(QtCore.QSize(0, 50))
        self.Working_lbl.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Working_lbl.setObjectName("Working_lbl")
        self.GridLayout.addWidget(self.Working_lbl, 4, 0, 1, 2)
        self.Comment_lbl = QtWidgets.QLabel(XpaNewDialog)
        self.Comment_lbl.setMinimumSize(QtCore.QSize(0, 25))
        self.Comment_lbl.setMaximumSize(QtCore.QSize(16777215, 25))
        self.Comment_lbl.setObjectName("Comment_lbl")
        self.GridLayout.addWidget(self.Comment_lbl, 6, 0, 1, 1)
        self.LoadExcel_btn = QtWidgets.QPushButton(XpaNewDialog)
        self.LoadExcel_btn.setMinimumSize(QtCore.QSize(160, 0))
        self.LoadExcel_btn.setMaximumSize(QtCore.QSize(160, 16777215))
        self.LoadExcel_btn.setObjectName("LoadExcel_btn")
        self.GridLayout.addWidget(self.LoadExcel_btn, 0, 0, 1, 1)
        self.Comment_txtedit = QtWidgets.QTextEdit(XpaNewDialog)
        self.Comment_txtedit.setEnabled(False)
        self.Comment_txtedit.setObjectName("Comment_txtedit")
        self.GridLayout.addWidget(self.Comment_txtedit, 6, 1, 1, 1)
        self.verticalLayout.addLayout(self.GridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Ok_btn = QtWidgets.QPushButton(XpaNewDialog)
        self.Ok_btn.setEnabled(False)
        self.Ok_btn.setMinimumSize(QtCore.QSize(150, 0))
        self.Ok_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.Ok_btn.setObjectName("Ok_btn")
        self.horizontalLayout.addWidget(self.Ok_btn)
        self.No_btn = QtWidgets.QPushButton(XpaNewDialog)
        self.No_btn.setMinimumSize(QtCore.QSize(150, 0))
        self.No_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.No_btn.setObjectName("No_btn")
        self.horizontalLayout.addWidget(self.No_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(XpaNewDialog)
        QtCore.QMetaObject.connectSlotsByName(XpaNewDialog)

    def retranslateUi(self, XpaNewDialog):
        _translate = QtCore.QCoreApplication.translate
        XpaNewDialog.setWindowTitle(_translate("XpaNewDialog", "새 작업환경 만들기"))
        self.FileName_lbl.setText(_translate("XpaNewDialog", "선택된 파일이 없습니다"))
        self.Working_lbl.setText(_translate("XpaNewDialog", "공사명(\'표지\' A11)"))
        self.Comment_lbl.setText(_translate("XpaNewDialog", "간단한 코멘트"))
        self.LoadExcel_btn.setText(_translate("XpaNewDialog", "엑셀 파일 불러오기"))
        self.Ok_btn.setText(_translate("XpaNewDialog", "확인"))
        self.No_btn.setText(_translate("XpaNewDialog", "닫기"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    XpaNewDialog = QtWidgets.QDialog()
    ui = Ui_XpaNewDialog()
    ui.setupUi(XpaNewDialog)
    XpaNewDialog.show()
    sys.exit(app.exec_())
