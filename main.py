import os
import shutil

src_dir = "C:/Users/tibia\Desktop/test"
doc_dir = src_dir + "\Documents"
pic_dir = src_dir + "\Pictures"
soft_dir = src_dir + "\Software"


def moveto(dst):
    return lambda src: shutil.move(src, dst)

action = {
    'pdf': moveto(doc_dir),
    'docx': moveto(doc_dir),
    'txt': moveto(doc_dir),
    'exe': moveto(soft_dir),
    'jpg': moveto(pic_dir),
    'png': moveto(pic_dir),
}

for filename in os.listdir(src_dir):
    ext = os.path.splitext(filename)[1][1:]
    if ext in action:
        action[ext](os.path.join(src_dir, filename))
