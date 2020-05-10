from PyQt5.QtWidgets import QAction


class MyAction(QAction):
    def __init__(self, status, shortcut, tip):
        super().__init__(status)
        self.setShortcut(shortcut)
        self.setStatusTip(tip)


class XpaNewAction(MyAction):
    def __init__(self):
        super().__init__('새 작업 (N)', 'Ctrl+N', '새 작업을 만듭니다.')


class XpaSaveAction(MyAction):
    def __init__(self):
        super().__init__('작업 과정 저장 (S)', 'Ctrl+S', '작업 과정을 xpa 파일로 저장합니다.')


class XpaSaveAnotherAction(MyAction):
    def __init__(self):
        super().__init__('다른 이름으로 저장', 'Ctrl+Shift+S', '작업 과정을 새로운 xpa 파일로 저장합니다.')


class XpaLoadAction(MyAction):
    def __init__(self):
        super().__init__('작업 과정 불러오기 (', 'Ctrl+O', '작업 과정을 불러옵니다.')


class ExitAction(MyAction):
    def __init__(self):
        super().__init__('종료 (Q)', 'Ctrl+Q', '프로그램을 종료합니다.')