
# --- Move screehsot Screenshot* files to 
# --- Check how long they have been held for and if more than 7 days destroy 

from pathlib import Path
import datetime
original_screenshots_dir=Path("/Users/rock/Desktop")
moved_screenshots_dir=Path("/Users/rock/Documents/screenshots")

# Get list of Screenshot in original_screenshots_dir
screenshots=original_screenshots_dir.glob("Screenshot*") # getting object Path.glob NOT the files

# Move Screenshots to another dir, moved_screenshots_dir
for screenshot in screenshots:
    new_screenshot_path=moved_screenshots_dir/screenshot.name
    screenshot.rename(new_screenshot_path)

# Checking if the screenshots have been held longer than 7 days (>7days)
# st_ctime - The last time the file's metadata (e.g. permissions, ownership) was changed, in seconds since the epoch.
list_screenshots=moved_screenshots_dir.glob("*")
for screenshot in list_screenshots:
    time_date_now=datetime.datetime.now()
    time_date_when_screen_was_moved=datetime.datetime.fromtimestamp(screenshot.stat().st_ctime)
    time_diff=time_date_now-time_date_when_screen_was_moved
    if time_diff.days>=7:
        with open(screenshot,"wb") as bin_file:
            bin_file.write(b'')
        screenshot.unlink()
        print("The screenshots were completely deleted!")
