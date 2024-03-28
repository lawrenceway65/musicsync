# Simple rsync type functionality based on comparison of file size only.

import os
import shutil

# source_root = "C:\\Users\\lawre\\Local\\MusicTest"
source_root = "C:\\Users\\lawre\\OneDrive\\Music"
# dest_root = "C:\\Users\\lawre\\Local\\MusicTestSync"
dest_root = "D:\\Music"


def music_sync():
    dir_count = 0
    diff_count = 0
    # Use a breakpoint in the code line below to debug your script.
    for (root, dirlist, filelist) in os.walk(source_root, topdown=True):
        dirs = [n for n in dirlist]
        for i in dirs:
            dir_count += 1
            source_dir = root + "\\" + i
            dest_dir = dest_root + source_dir[len(source_root):len(source_dir)]
            # Check if dest dir exists
            if not os.path.exists(dest_dir):
                print("Create directory: " + dest_dir)
                os.mkdir(dest_dir)
            files = os.scandir(source_dir)
            for n in files:
                if n.is_file():
                    source_filespec = source_dir + "\\" + n.name
                    source_size = os.path.getsize(source_filespec)
#                    print(source_filespec)
                    leaf = source_filespec[len(source_root):len(source_filespec)]
#                    print(leaf)
                    dest_filespec = dest_root + leaf
#                    print(dest_filespec)
                    update = False
                    if os.path.exists(dest_filespec):
                        dest_size = os.path.getsize(dest_filespec)
#                        print(str(dest_size) + "\t" + str(dest_size))
                        if source_size != dest_size:
                            print(source_filespec + ": No size match")
                            update = True
                            diff_count += 1
                    else:
                        print(source_filespec + ": No file")
                        update = True
                        diff_count += 1
#                    if update:
#                        print("Copy file: " + source_filespec)
                        shutil.copy(source_filespec, dest_filespec)
    print(str(dir_count) + " directories checked, " + str(diff_count) + " files updated")

# Changes : create directories, reverse check
#        files = [n for n in filelist]
#        for i in files:
#            print(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    music_sync()

