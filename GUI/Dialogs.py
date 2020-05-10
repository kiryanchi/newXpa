from UI.Dialog.XpaNewDialog import Ui_XpaNewDialog
from PyQt5.QtWidgets import QDialog, QFileDialog
from Core.Base import *
from Core.FileIO.XpaNew import MakeXpaNew
from GUI.MessageBox import *
from GUI.CenteralWidget import MyCenteralWidget
import openpyxl
import os


class XpaNewActionDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_XpaNewDialog()
        self.ui.setupUi(self)
        self.ui.LoadExcel_btn.clicked.connect(self.LoadExcel)
        self.ui.Ok_btn.clicked.connect(self.accept)
        self.ui.No_btn.clicked.connect(self.close)
        self.wb = None
        self.file_path = None

    def LoadExcel(self):
        # fname : 전체 주소
        self.file_path, _ = QFileDialog.getOpenFileName(self, '엑셀 파일 선택', BASE_DIR, "Excel File (*.xlsx)")

        if self.file_path:
            # file_name : 파일 이름 *.xlsx
            file_name = os.path.basename(self.file_path)
            try:
                wb = openpyxl.load_workbook(self.file_path)
            except FileNotFoundError:
                msgBox = CriticalMsgBox('엑셀 파일 열기에 실패했습니다')
                msgBox.exec_()
            else:
                sheet_name_list = wb.sheetnames
                if '표지' in sheet_name_list:
                    sheet = wb['표지']
                    working = sheet['A11'].value
                    SetLabelText(self.ui.Working_lbl, working)
                else:
                    SetLabelText(self.ui.Working_lbl, '공사명을 확인할 수 없습니다')
                self.ui.Comment_txtedit.setEnabled(True)
                self.ui.Ok_btn.setEnabled(True)
                SetLabelText(self.ui.FileName_lbl, file_name)

    def ExcelInfo(self):
        filepath = self.file_path
        comment = self.ui.Comment_txtedit.toPlainText()

        return filepath, comment

    def closeEvent(self, event):
        print('hello')
