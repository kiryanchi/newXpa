import os


BASE_DIR = os.getcwd()
HOME_DIR = os.path.expanduser("~")
WORK_DIR = os.path.join(HOME_DIR, '.xpaworking')
# IMG_DIR - os.path.join(WORK_DIR, 'Image')


def SetLabelText(label, text):
    label.setText(text)
    label.adjustSize()


if __name__ == '__main__':
    print(BASE_DIR)
    print(HOME_DIR)
    print(os.path.join(HOME_DIR, 'test.xlsx'))