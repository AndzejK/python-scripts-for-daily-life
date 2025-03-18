import os,shutil,re,time
import datetime, random,string
from tqdm import tqdm
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

# file_names=generate_file_names()
# generate_random_context(src_path=source_path,dirs=dirs_only_filtered,files=file_names_18)

## wipe out a directory and what is in it
test_dir=r"/Users/rock/Documents/myStudy/Python/Bentley/python-scripts/tests/files/moveSRC/05_demo_dir_20250314"


def remove_dir_and_its_content(src):
    # get total size of files
    total_size=0
    for root,dirs,files in os.walk(test_dir,topdown=False):
        for file in files:
            total_size+=os.path.getsize(os.path.join(root,file))
    
    # Progress bar setup
    with tqdm(desc=f"📂 Wiping out... {os.path.basename(src)}",unit="B",unit_scale=True,colour='red',total=total_size) as pbar:
        # Remove files and update progress
        for root,dirs,files in os.walk(src,topdown=False):
            for file in files:
                file_path=os.path.join(root,file)
                file_size=os.path.getsize(file_path)
                os.remove(file_path)
                pbar.update(file_size) # update a progress bar by a file size
            # Remove dir if empty:
            for dir in dirs:
                os.rmdir(os.path.join(root,dir))
        # Final cleanup
        if os.path.exists(src):
            # print(f"A directory '{dir}' was removed...")
            os.rmdir(src)
            

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


dir_search_pattern=r"^(?!01)\d{2}_demo_dir_2025" # A negative lookahead, skips what start with 01
dir_search_pattern_all=r"\d{2}_demo_dir_2025"
dirs_only_filtered=[dir_fil for dir_fil in dirs_only if re.match(dir_search_pattern_all,dir_fil)]

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

#### Claude
real_file='LM-Studio-0.3.9-5-arm64.dmg'
src = os.path.join(source_path,real_file) 
dst = os.path.join(destination_path,real_file)

def dynamic_progress_bar(src, dst):
    """Progress bar with changing colors based on progress"""
    file_size = os.path.getsize(src)
    
    with open(src, 'rb') as fsrc, open(dst, 'wb') as fdst:
        # Initialising  progress bar
        with tqdm(total=file_size, 
                  unit='B',
                  unit_scale=True,
                  desc=f"🚀 Transferring {os.path.basename(src)}") as pbar:
            
            bytes_copied = 0
            while True:
                buf = fsrc.read(1024*1024)
                if not buf:
                    break
                
                # Simulate network fluctuation for demonstration
                time.sleep(0.01)  
                
                fdst.write(buf)
                bytes_copied += len(buf)
                
                # Update progress
                pbar.update(len(buf))
                
                # Change color based on progress
                progress = bytes_copied / file_size
                if progress < 0.3:
                    pbar.colour = 'red'
                elif progress < 0.7:
                    pbar.colour = 'yellow'
                else:
                    pbar.colour = 'green'

# dynamic_progress_bar(src,dst)
# print(os.listdir(os.path.join(source_path,demo_directories[0])))

# for d_file in demo_files:
    # os.remove(os.path.join(source_path,demo_directories[0],d_file))


# for i in range(100):
#     with tqdm( desc=f"📃 File", bar_format=f"{MAGENTA} {'{l_bar}'}{BRIGHT_GREEN}{'{bar}'}{BRIGHT_BLUE}{'{r_bar}'}{RESET}") as pbar:
#         total_size=100
#         bytes_copied=0
#         while total_size>bytes_copied:
#             time.sleep(0.001)
#             bytes_copied+=1
#             #update() ?
#             #change color
#             pbar.update(1)
#             progress=bytes_copied/total_size
#             if progress<0.3:
#                pbar.colour="red" # I recreate each time a new tqdm instance rather than updating the existing one?
#             elif progress<0.7:
#                 pbar.colour="yellow"#f"{YELLOW}{'{bar}'}"
#             else:
#                pbar.colour="green" #f"{BRIGHT_GREEN}{'{bar}'}"

# #### DeepSeek ####

# # Settings for tqdm
# RED = '\033[91m'  # ANSI escape code for bright red
# BRIGHT_GREEN = '\033[92m'
# GREEN = '\033[92m'
# BRIGHT_BLUE = '\033[94m'
# MAGENTA = '\033[35m'
# YELLOW = ' \033[33m'
# BLUE = '\033[94m'
# RESET = '\033[0m' # ANSI escape code to reset color


# total_size = 100

# # Initialize ONE progress bar with dynamic color
# with tqdm(
#     total=total_size,
#     desc="📃 File",
#     bar_format=f"{MAGENTA}{{l_bar}}{RESET}{{bar}}{BLUE}{{r_bar}}{RESET}",  # Base format
#     unit_scale=True
# ) as pbar:
#     bytes_copied = 0
#     while bytes_copied < total_size:
#         time.sleep(0.1)
#         bytes_copied += 1
#         progress = bytes_copied / total_size

#         # Dynamically update bar color based on progress
#         if progress < 0.3:
#             color = RED
#         elif progress < 0.7:
#             color = YELLOW
#         else:
#             color = GREEN

#         # Override the bar's color using ANSI codes
#         pbar.n = bytes_copied  # Directly set the current progress
#         pbar.last_print_n = bytes_copied  # Force refresh
#         pbar.bar_format = f"{MAGENTA}{{l_bar}}{RESET}{color}{{bar:20}}{RESET}{BLUE}{{r_bar}}{RESET}"
#         pbar.refresh()  # Manually refresh the bar

#         pbar.update(0)  # Force update (no increment)


# def get_colour(x):
#     if x < 30:
#         return 'red'
#     elif x < 70:
#         return 'yellow'
#     else:
#         return 'green'

# with tqdm(total=100, bar_format='{l_bar}{bar:20}{r_bar}', colour=get_colour) as pbar:
#     for i in range(100):
#         time.sleep(0.1)
#         pbar.update(1)

# for i in tqdm(range(100), bar_format='{l_bar}{bar:20}{r_bar}', colour='green'):
#     time.sleep(0.1)

# pbar = tqdm(total=100)
# for i in range(100):
#     time.sleep(0.1)
#     if i < 30:
#         pbar.bar_format = '{l_bar}{bar:20}{r_bar}'
#     else:
#         pbar.bar_format = '{l_bar}{bar:20}{r_bar}'
#     pbar.update(1)
# pbar.close()

