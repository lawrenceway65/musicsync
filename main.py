# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import shutil

# source_dir = "C:\\Users\\lawre\\Local\\MusicTest"
source_dir = "C:\\Users\\lawre\\OneDrive\\Music"
# dest_dir = "C:\\Users\\lawre\\Local\\MusicTestSync"
dest_dir = "D:\\Music"

def music_sync():
    dir_count = 0
    diff_count = 0
    # Use a breakpoint in the code line below to debug your script.
    for (root, dirlist, filelist) in os.walk(source_dir, topdown=True):
        dirs = [n for n in dirlist]
        for i in dirs:
            dir_count += 1
            current_dir = root + "\\" + i
            files = os.scandir(current_dir)
            for n in files:
                if n.is_file():
                    source_filespec = current_dir + "\\" + n.name
                    source_size = os.path.getsize(source_filespec)
#                    print(source_filespec)
                    leaf = source_filespec[len(source_dir):len(source_filespec)]
#                    print(leaf)
                    dest_filespec = dest_dir + leaf
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
#                        shutil.copy(source_filespec, dest_filespec)
    print(str(dir_count) + " directories checked, " + str(diff_count) + " differences")

# Changes : create directories, reverse check
#        files = [n for n in filelist]
#        for i in files:
#            print(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    music_sync()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
