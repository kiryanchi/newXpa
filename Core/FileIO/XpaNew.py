import shutil
from Core.Base import *
import os


def MakeXpaNew(filepath, comment=''):
    file_name = "working.xlsx"
    comment_name = "comment.txt"
    # ~/filename 폴더를 만듬 ( 임시폴더 )
    if not os.path.isdir(WORK_DIR):
        os.mkdir(WORK_DIR)
    save_path = os.path.join(WORK_DIR, file_name)
    print(save_path)
    shutil.copyfile(filepath, save_path)
    with open(os.path.join(WORK_DIR, comment_name), "w") as f:
        f.write(comment)