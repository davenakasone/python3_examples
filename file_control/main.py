"""
besides creating, reading, and writting, you will want to organzie files
shutil  or 'shell utilities' has many function to help

be careful with move   ...it can overwrite and won't give file an extension when it is unsure

os is for single and empty
shutil is for doing some serious work...deleting entire file and all its contents
os.unlink(path)     will delete file at path
os.rmdir(path)      will delete folder at path  (must be empty)
shutil.rmtree(path)    this will take out entire folder at path and everythig in it   can be dangerous
"""
import os
import send2trash
import shutil
from pathlib import Path
import time

print('\n1') # 1 basic copy
current_path = Path('new_torrent.txt') # tell it where the file is
desired_path = Path('destination') # tell it where you want it to go
shutil.copy(current_path,desired_path) # file copied 
print(f"looks like {current_path.name} was copied to {shutil.copy(current_path,desired_path)}")
time.sleep(2)

print('\n2') # 2 copy with a rename
base = Path.cwd() # or home ... just depends where you deploy this
shutil.copy(base/'new_torrent.txt', base/'destination/legal_file.txt')
print(f'copied and renamed')

print('\n3') # 3 move the entire file
target = Path(Path.cwd()/'torrents')
dest = Path(Path.cwd()/'torrents_backup')
if os.path.exists(dest):
    print('have to delete directory first')
else:
    shutil.copytree(target, dest) # file can't exist?
    print(f"got {str(target)} copied into {str(dest)}")

print('\n4') # 4 be careful with move...it overwrites doesn't like if destination directory already exists
source = Path(Path.cwd()/'new_torrent.txt')
dest = Path(Path.cwd()/'new_new_torrent.txt')
shutil.move(source, dest)
time.sleep(2)
print(f"moved {source.name} into {dest}") # move with overwrite & name change   can also do with directories
source = Path(Path.cwd()/'new_new_torrent.txt')
dest = Path(Path.cwd()/'new_torrent.txt') # change it back
shutil.move(source, dest)
time.sleep(2)
print(f"moved {source.name} into {dest}")

print('\n5') # 5 before doing a batch delete, print to check
check_path = Path(Path.cwd()/'torrents_backup')
check_path_dir = os.listdir(check_path)
if len(check_path_dir) == 0:
    target = Path(Path.cwd()/'torrents')
    dest = Path(Path.cwd()/'torrents_backup')
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(target, dest) # file can't exist?
for filename in check_path.glob('*txt'):
    print(filename)
    os.unlink(filename) # comment out to check, then take # off
print(f'all the .txt files in {check_path} are gone')
time.sleep(2)

print('\n6') # 6 not permanantly deleting stuff
new_obj = open('error.txt','w')
new_obj.write('this is a file that should not be here')
new_obj.close()
new_obj = open('error.txt','r')
contents = new_obj.read()
print(f'the files says: {contents}')
time.sleep(2)
unwanted = Path(Path.cwd()/'error.txt')
send2trash.send2trash(unwanted) # only goes to recycle bin, can't pull it out

print('\n7') # 7 walking files  ...know what your map looks like especially depth  good for search
walk_path = Path(Path.cwd()/'walk_me')
for f1s, f2s, f3s in os.walk(walk_path):
    print(f"f1 is: {f1s}")
    for f2 in f2s:
        print(f" {f1s} : {f2}")
        for f3 in f3s:
            print(f"{f2s} : {f3}")
    print('\n')
