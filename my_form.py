# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'my_form.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(724, 756)
        font = QFont()
        font.setFamily(u".Apple SD Gothic NeoI")
        Dialog.setFont(font)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scaledown_btn = QPushButton(Dialog)
        self.scaledown_btn.setObjectName(u"scaledown_btn")
        self.scaledown_btn.setEnabled(False)
        self.scaledown_btn.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.scaledown_btn, 0, 11, 1, 1)

        self.scaleup_btn = QPushButton(Dialog)
        self.scaleup_btn.setObjectName(u"scaleup_btn")
        self.scaleup_btn.setEnabled(False)
        self.scaleup_btn.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.scaleup_btn, 0, 10, 1, 1)

        self.filesave_btn = QPushButton(Dialog)
        self.filesave_btn.setObjectName(u"filesave_btn")
        self.filesave_btn.setEnabled(False)

        self.gridLayout.addWidget(self.filesave_btn, 5, 12, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.sheetlist = QTabWidget(Dialog)
        self.sheetlist.setObjectName(u"sheetlist")
        self.sheetlist.setLayoutDirection(Qt.LeftToRight)
        self.sheetlist.setMovable(True)

        self.gridLayout_2.addWidget(self.sheetlist, 1, 0, 1, 1)

        self.xpaload_btn = QPushButton(Dialog)
        self.xpaload_btn.setObjectName(u"xpaload_btn")
        self.xpaload_btn.setEnabled(False)
        self.xpaload_btn.setCheckable(False)

        self.gridLayout_2.addWidget(self.xpaload_btn, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 2, 1, 1, 12)

        self.fileopen_lbl = QLabel(Dialog)
        self.fileopen_lbl.setObjectName(u"fileopen_lbl")

        self.gridLayout.addWidget(self.fileopen_lbl, 0, 3, 1, 7)

        self.reload_btn = QPushButton(Dialog)
        self.reload_btn.setObjectName(u"reload_btn")
        self.reload_btn.setEnabled(False)
        self.reload_btn.setMinimumSize(QSize(0, 25))
        self.reload_btn.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.reload_btn, 4, 2, 1, 11)

        self.delete_btn = QPushButton(Dialog)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setEnabled(False)

        self.gridLayout.addWidget(self.delete_btn, 4, 1, 1, 1)

        self.progress_bar = QProgressBar(Dialog)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setMinimumSize(QSize(200, 20))
        self.progress_bar.setMaximumSize(QSize(200, 20))
        self.progress_bar.setMaximum(1)
        self.progress_bar.setValue(0)
        self.progress_bar.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.progress_bar, 6, 12, 1, 1)

        self.fileopen_btn = QPushButton(Dialog)
        self.fileopen_btn.setObjectName(u"fileopen_btn")
        self.fileopen_btn.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.fileopen_btn, 0, 1, 1, 1)

        self.deleteall_btn = QPushButton(Dialog)
        self.deleteall_btn.setObjectName(u"deleteall_btn")
        self.deleteall_btn.setEnabled(False)

        self.gridLayout.addWidget(self.deleteall_btn, 0, 2, 1, 1)

        self.xpasave_btn = QPushButton(Dialog)
        self.xpasave_btn.setObjectName(u"xpasave_btn")
        self.xpasave_btn.setEnabled(False)

        self.gridLayout.addWidget(self.xpasave_btn, 0, 12, 1, 1)

        self.aleart = QLabel(Dialog)
        self.aleart.setObjectName(u"aleart")
        self.aleart.setMinimumSize(QSize(500, 20))
        self.aleart.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.aleart.setFont(font1)
        self.aleart.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.aleart, 5, 1, 1, 11)

        self.progress_lbl = QLabel(Dialog)
        self.progress_lbl.setObjectName(u"progress_lbl")
        self.progress_lbl.setMinimumSize(QSize(300, 20))
        self.progress_lbl.setMaximumSize(QSize(16777215, 20))
        self.progress_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.progress_lbl, 6, 1, 1, 11)


        self.retranslateUi(Dialog)

        self.sheetlist.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\uc5d1\uc140 \uc790\ub3d9 \uc791\uc5c5 \ud504\ub85c\uadf8\ub7a8", None))
        self.scaledown_btn.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.scaleup_btn.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.filesave_btn.setText(QCoreApplication.translate("Dialog", u"\uc5d1\uc140\uc5d0 \uc0ac\uc9c4\ub123\uae30", None))
        self.xpaload_btn.setText(QCoreApplication.translate("Dialog", u"\uc791\uc5c5 \ubd88\ub7ec\uc624\uae30 (L)", None))
#if QT_CONFIG(shortcut)
        self.xpaload_btn.setShortcut(QCoreApplication.translate("Dialog", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.fileopen_lbl.setText(QCoreApplication.translate("Dialog", u"\uc120\ud0dd\ub41c \uc5d1\uc140 \ud30c\uc77c\uc774 \uc5c6\uc2b5\ub2c8\ub2e4.", None))
        self.reload_btn.setText(QCoreApplication.translate("Dialog", u"\uc0ac\uc9c4 \uc0c8\ub85c\uace0\uce68 (R)", None))
#if QT_CONFIG(shortcut)
        self.reload_btn.setShortcut(QCoreApplication.translate("Dialog", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.delete_btn.setText(QCoreApplication.translate("Dialog", u"\uc0ac\uc9c4 \uc0ad\uc81c (Del)", None))
#if QT_CONFIG(shortcut)
        self.delete_btn.setShortcut(QCoreApplication.translate("Dialog", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.progress_bar.setFormat(QCoreApplication.translate("Dialog", u"\uc644\ub8cc", None))
        self.fileopen_btn.setText(QCoreApplication.translate("Dialog", u"\uc5d1\uc140 \ud30c\uc77c \ubd88\ub7ec\uc624\uae30 (O)", None))
#if QT_CONFIG(shortcut)
        self.fileopen_btn.setShortcut(QCoreApplication.translate("Dialog", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.deleteall_btn.setText(QCoreApplication.translate("Dialog", u"\uc0ac\uc9c4 \uc804\uccb4 \uc0ad\uc81c", None))
        self.xpasave_btn.setText(QCoreApplication.translate("Dialog", u"\uc791\uc5c5 \uc800\uc7a5 (S)", None))
#if QT_CONFIG(shortcut)
        self.xpasave_btn.setShortcut(QCoreApplication.translate("Dialog", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.aleart.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" color:#ff0000;\">\u203b\uacbd\uace0\u203b \uc791\uc5c5\uc911\uc778 \uc5d1\uc140\uc740 \ub048 \uc0c1\ud0dc\uc5d0\uc11c \uc9c4\ud589\ud574\uc57c\ud568</span></p></body></html>", None))
        self.progress_lbl.setText(QCoreApplication.translate("Dialog", u"\uc9c4\ud589\uc0c1\ud669", None))
    # retranslateUi

