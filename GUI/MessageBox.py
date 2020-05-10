from PyQt5.QtWidgets import QMessageBox


class MyMessageBox(QMessageBox):
    def __init__(self, title, text):
        super().__init__()
        self.setWindowTitle(title)
        self.setText(text)
        self.setIcon(QMessageBox.NoIcon)


class InformationMsgBox(MyMessageBox):
    def __init__(self, text, title='정보'):
        super().__init__(title, text)
        self.setIcon(QMessageBox.Information)
        self.setStandardButtons(QMessageBox.Ok)


class CriticalMsgBox(MyMessageBox):
    def __init__(self, text, title='경고'):
        super().__init__(title, text)
        self.setIcon(QMessageBox.Critical)
        self.setStandardButtons(QMessageBox.Ok)


class WarningMsgBox(MyMessageBox):
    def __init__(self, text, title='주의'):
        super().__init__(title, text)
        self.setIcon(QMessageBox.Warning)
        self.setStandardButtons(QMessageBox.Ok)


class QuestionMsgBox(MyMessageBox):
    def __init__(self, text, title='의문(?)'):
        super().__init__(title, text)
        self.setIcon(QMessageBox.Question)
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.No)