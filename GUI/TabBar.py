from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QTableWidget, QAbstractItemView, QHeaderView, QApplication, QShortcut, QWidget, \
    QVBoxLayout
from PyQt5 import QtCore


class MyTabBarList(QWidget):
    def __init__(self):
        super().__init__()
        self.TableWidget = MyTableWidgetInTabBar()
        # self.TableWidget.setEnabled(True)
        vbox = QVBoxLayout()
        vbox.addWidget(self.TableWidget)
        self.setLayout(vbox)


class MyTableWidgetInTabBar(QTableWidget):
    def __init__(self):
        super().__init__(0, 3)
        self.setAcceptDrops(True)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        # self.setDragDropMode(QAbstractItemView.InternalMove)
        # self.setDefaultDropAction(QtCore.Qt.CopyAction)
        # 테이블위젯의 헤더 크기를 조정
        self.setAlternatingRowColors(True)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setMinimumSize(QtCore.QSize(990, 630))
        self.verticalHeader().setDefaultSectionSize(170)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.setHorizontalHeaderLabels(['작업 전', '작업 후', '전주 번호'])
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        copyShortcut = QShortcut(QKeySequence.Copy, self)
        pasteShortcut = QShortcut(QKeySequence.Paste, self)

        copyShortcut.activated.connect(self.copy)
        pasteShortcut.activated.connect(self.paste)

    def scaleup(self):
        pass

    def scaledown(self):
        pass

    def copy(self):
        selectedRangeList = self.selectedRanges()
        if not selectedRangeList:
            return

        r = self.currentRow()
        c = self.currentColumn()
        selectedPoint = self.cellWidget(r, c)
        image = selectedPoint.imgpath

        QApplication.clipboard().setText(image)

    def paste(self):
        image = QApplication.clipboard().text()
        r = self.currentRow()
        c = self.currentColumn()
        widget = TableWidget(image)
        self.setCellWidget(r, c, widget)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        global NOT_SAVE
        e.setDropAction(QtCore.Qt.CopyAction)
        e.accept()
        if e.mimeData().hasUrls and FILE_NAME != "default":
            url = e.mimeData().urls()[0]
            url = str(url.toLocalFile())
            if url.split('.')[-1] == 'JPG' or url.split('.')[-1] == 'jpg':
                widget = TableWidget(url)
                row = self.currentRow()
                col = self.currentColumn()
                self.setCellWidget(row, col, widget)
                NOT_SAVE = True


class TableItem(QWidget):
    def __init__(self, imgpath, pixmap=None):
        super().__init__()
        tab_idx = myWindow.sheetlist.currentIndex()
        self.imgpath = imgpath
        self.lbl = QLabel()
        self.img = TableWidgetPixmap(imgpath) if pixmap is None else pixmap
        self.img = self.img.scaled(myWindow.sheetlist.widget(tab_idx).table.width() // 3 - 30, 140 + 10)
        self.lbl.setPixmap(self.img)
        self.widget_layout = QHBoxLayout()
        self.widget_layout.addWidget(self.lbl)
        self.widget_layout.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(self.widget_layout)
