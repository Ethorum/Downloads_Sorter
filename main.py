import os
import shutil

#Directories
src_dir = "C:/Users/tibia/Desktop/test"  # Change src_dir to the directory you wish to sort
doc_dir = src_dir + "/Documents"
pic_dir = src_dir + "/Pictures"
soft_dir = src_dir + "/Software"
comp_dir = src_dir + "/Compressed"
vid_dir = src_dir + "/Video"
mus_dir = src_dir + "/Music"


# Checks if the folder exists and creates it if it does not
def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

create_folder(doc_dir)
create_folder(pic_dir)
create_folder(soft_dir)
create_folder(comp_dir)
create_folder(vid_dir)
create_folder(mus_dir)

def moveto(dst):
    return lambda src: shutil.move(src, dst)

action = {
    # Documents extensions
    'pdf': moveto(doc_dir),
    'docx': moveto(doc_dir),
    'txt': moveto(doc_dir),
    'xls': moveto(doc_dir),
    'xlsx': moveto(doc_dir),
    # Picture extensions
    'jpg': moveto(pic_dir),
    'jpeg': moveto(pic_dir),
    'png': moveto(pic_dir),
    'gif': moveto(pic_dir),
    # Software extensions
    'exe': moveto(soft_dir),
    'iso': moveto(soft_dir),
    'MSI': moveto(soft_dir),
    # Compressed extensions
    'zip': moveto(comp_dir),
    'rar': moveto(comp_dir),
    # Video extensions
    'mp4': moveto(vid_dir),
    'mov': moveto(vid_dir),
    'webm': moveto(vid_dir),
    'wmv': moveto(vid_dir),
    'flv': moveto(vid_dir),
    'avi': moveto(vid_dir),
    # Music and audio extensions
    'mp3': moveto(mus_dir),
    'wav': moveto(mus_dir),
    'wma': moveto(mus_dir),
    'aac': moveto(mus_dir),
    'm4a': moveto(mus_dir),
}

for filename in os.listdir(src_dir):
    ext = os.path.splitext(filename)[1][1:]
    if ext in action:
        action[ext](os.path.join(src_dir, filename))
