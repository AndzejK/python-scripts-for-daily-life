import os,shutil,glob
from paths import source_path,destination_path

##### Basic examples how to deal with files and directories #####

# A list of files and directories
files_and_dirs=os.listdir(source_path) # []
                                            # regular looping instead of telling 
            # what do?                      # what do at the end is said at start
full_paths=[os.path.join(source_path,item) for item in os.listdir(source_path)]

# Filter for just file or just directories
## Obtaining files
files_only=[file for file in os.listdir(source_path) if os.path.isfile(os.path.join(source_path,file))]
# for file in os.listdir(source_path):
#     if os.path.isfile(os.path.join(source_path,file)):
#         files_only.append(file)
## Obtaining dirs
dirs_only=[dir for dir in os.listdir(source_path) if os.path.isdir(os.path.join(source_path,dir))]

# ## Search in the files system from where I tell for all files and directories
# for cur_dir_path, dirs, files in os.walk(source_path):
#     print(f"Current Directory: {cur_dir_path}")
#     print(f"Subdirectories: {dirs}")
#     print(f"Files: {files}")
#     print()  # Print a newline for better readability

# ## the OS module is lowever lvl compare to shutil
# ## Getting the size of each directory and file:

# # shutil doesn't have its own listing functions
# # But it has useful functions for file operations after listing
# for item in os.listdir(source_path):
#     full_path=os.path.join(source_path,item)
#     if os.path.isdir(full_path):
#         size = shutil.disk_usage(full_path).total # using shutil to get the size of a dir
#     else:
#         size = os.path.getsize(full_path) # Using OS to get the size of a file
#     print(f"{item}: {size} bytes")

# ## rename file:
# os.rename(os.path.join(source_path,"file.0001"),os.path.join(source_path,("file.0001_renamed")))

# ## remove dir (empty)
# os.rmdir(os.path.join(source_path,"dir_name_"))


### I  created files with a specific sequence and then rename only the files that have that certain sequence.
### e.g. demo_file_00 ... demo_file_10
###      demo_dir_00  ... demo_dir_10

demo_files=["demo_file_"+str(demo_file)+".txt" for demo_file in range(0,11)]
demo_dirs=["demo_dir_"+str(demo_dir) for demo_dir in range(0,6)]
# print(demo_files)
# Create a directory
# os.makedirs(os.path.join(source_path,demo_dirs[0]), exist_ok=True)

# # create a file with random context
# import random,string
# demo_file=demo_files[0]
# with open(os.path.join(source_path,demo_file),'w') as r_file:
#     random_content=''.join(random.choices(string.ascii_letters + string.digits + ' \n',k=8 * 1024))
#     r_file.write(random_content)

