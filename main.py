# Simple rsync type functionality based on comparison of file size only.

import os
import shutil

# Laptop
# source_root = "C:\\Users\\lawre\\Local\\MusicTest"
# dest_root = "C:\\Users\\lawre\\Local\\MusicTestSync"

# Test
#dest_root = "D:\\Music"
#source_root = "C:\\Users\\lawre\\OneDrive\\Music"

source_root = "C:\\Users\\Lawrence\\OneDrive\\Music"
dest_root = "K:\\Music"


def music_sync():
    # Check dirs present
    if not os.path.exists(source_root):
        print("Source directory not found")
        exit()
    if not os.path.exists(dest_root):
        print("Destination directory not found")
        exit()

    # Remove directories/files on destination that are not present on source
    items_removed = 0
    for (root, dirlist, filelist) in os.walk(dest_root, topdown=True):
        dirs = [n for n in dirlist]
        for i in dirs:
            dest_dir = root + "\\" + i
            source_dir = source_root + dest_dir[len(dest_root):len(dest_dir)]
            # Check if source dir exists
            if not os.path.exists(source_dir):
                print("Delete directory: " + dest_dir)
                shutil.rmtree(dest_dir)
                items_removed += 1
                # No need to check files - rmtree will have removed them
                continue
            files = os.scandir(dest_dir)
            for n in files:
                if n.is_file():
                    dest_filespec = dest_dir + "\\" + n.name
                    source_filespec = source_root + dest_filespec[len(dest_root):len(dest_filespec)]
#                    print(source_filespec)
                    if not os.path.exists(source_filespec):
                        print("Delete file: " + dest_filespec)
                        os.remove(dest_filespec)
                        items_removed += 1
    print(str(items_removed) + " files/folders removed on destination")

    # Copy any file either not present on dest or present but different size
    dir_count = 0
    diff_count = 0
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
                    dest_filespec = dest_root + source_filespec[len(source_root):len(source_filespec)]
                    update = False
                    if os.path.exists(dest_filespec):
                        dest_size = os.path.getsize(dest_filespec)
                        if source_size != dest_size:
                            reason = "changed"
                            update = True
                            diff_count += 1
                    else:
                        reason = "new"
                        update = True
                        diff_count += 1
                    if update:
                        print("Copy " + reason + " file: " + source_filespec)
                        shutil.copy(source_filespec, dest_filespec)
    print(str(dir_count) + " directories checked, " + str(diff_count) + " files updated")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    music_sync()

