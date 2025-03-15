import os,shutil,re
import datetime, random,string
from paths import source_path,destination_path

### Functions:
## function that generates file names
def generate_file_names(num_of_files=11,ext='txt',basename='nrailpw11-pw-db-02_FULL_'):
    import datetime
    cur_date=datetime.date.today()
    cur_time=datetime.datetime.now().time()
    cur_date_formatted=cur_date.strftime("%Y%m%d")
    cur_time_formatted=cur_time.strftime("%H%M%S")
    file_name=basename+cur_date_formatted+'_'+cur_time_formatted+'_'
    demo_files=[file_name+f'{str(demo_file).zfill(2)}.{ext}' for demo_file in range(1,num_of_files)]

    return demo_files

## function that generates random content
def generate_random_context(src_path: str, dirs: list[str], files: list[str]) -> None:
    for dir_filtered in dirs:
        for d_file in files:
            with open(os.path.join(src_path,dir_filtered,d_file),'w') as f_demo:
                random_content=''.join(random.choices(string.ascii_letters + string.digits + ' \n',k=8 * 1024))
                f_demo.write(random_content)
##### Basic examples how to deal with files and directories #####

# A list of files and directories
files_and_dirs=os.listdir(source_path) # []
                                            # regular looping instead of telling 
            # what do?                      # what do at the end is said at start
full_paths=[os.path.join(source_path,item) for item in os.listdir(source_path)]

# Filter for just file or just directories
## Obtaining files
files_only=[file for file in os.listdir(source_path) if os.path.isfile(os.path.join(source_path,file))]

## Obtaining dirs
dirs_only=[dir for dir in os.listdir(source_path) if os.path.isdir(os.path.join(source_path,dir))]

dir_search_pattern=r"^(?!01)\d{2}_demo_dir_20250314" # A negative lookahead, skips what start with 01
dirs_only_filtered=[dir_fil for dir_fil in dirs_only if re.match(dir_search_pattern,dir_fil)]

# ## Search in the files system from where I tell for all files and directories
# for cur_dir_path, dirs, files in os.walk(source_path):
#     print(f"Current Directory: {cur_dir_path}"
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


# Generate file names, nrailpw11-pw-db-02_FULL_XXXXXX_XXXXXX_XX
# demo_files=[file_name+f'{str(demo_file).zfill(2)}' for demo_file in range(1,11)]

# Create name for a directory
basename_for_dir="_demo_dir_"
cur_date=datetime.date.today()
cur_date_formatted=cur_date.strftime("%Y%m%d")
dir_name=basename_for_dir+cur_date_formatted
demo_directories=[str(d_name).zfill(2)+dir_name for d_name in range(1,6)]

# Create directories
# for demo_dir in demo_directories:
#     os.makedirs(os.path.join(source_path,demo_dir), exist_ok=True)

# Delete directories
# for demo_dir in demo_directories:
#     os.removedirs(os.path.join(source_path,demo_dir))

demo_file_names=generate_file_names()

# dir_test_fn=["dirTobeCopied"]
# generate_random_context(src_path=source_path,dirs=dir_test_fn,files=demo_file_names)

# Create files with random content 
# for d_file in demo_file_names:
#     with open(os.path.join(source_path,demo_directories[0],d_file),'w') as file:
#         random_content=''.join(random.choices(string.ascii_letters + string.digits + ' \n',k=8 * 1024))
#         file.write(random_content)

# Remove files with random content
# Identify specific naames first!

files_only=[file for file in os.listdir(source_path) if os.path.isfile(os.path.join(source_path,file))]


# print(os.listdir(os.path.join(source_path,demo_directories[0])))

# for d_file in demo_files:
    # os.remove(os.path.join(source_path,demo_directories[0],d_file))

