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
print(dirs_only)
