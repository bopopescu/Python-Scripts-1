__author__ = 'pnagwekar'
import os
mpath=os.get_exec_path(env=None)
mpath.insert(2,'/home/pnagwekar')
print ("Your current path is set to = ", mpath)

'''
os.getcwd() — get the current working directory path as a string — pwd
os.listdir() — get the contents of the current working directory as a list of strings — ls
os.walk("starting_directory_path")— returns a generator with name and path info for directories and files in the the current directory and all subdirectories— no exact short CLI equivalent, but ls -R provides subdirectory names and the names of files within subdirectories
os.chdir("/absolute/or/relative/path") — change the current working directory — cd
os.path.join()—create a path for later use — no short CLI equivalent
os.makedirs("dir1/dir2") — make directory —mkdir -p
shutil.copy2("source_file_path", "destination_directory_path") — copy a file or directory — cp
shutil.move("source_file_path", "destination_directory_path") — move a file or directory — mv
os.remove("my_file_path") — remove a file — rm
shutil.rmtree("my_directory_path")— remove a directory and all files and directories in it —rm -rf

'''