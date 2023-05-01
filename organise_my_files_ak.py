
# --- Move screehsot Screenshot* files to 
# --- Check how long they have been held for and if more than 7 days destroy 

from pathlib import Path
original_screenshots_dir=Path("/Users/rock/Desktop")
moved_screenshots_dir=Path("/Users/rock/Documents/screenshots")

# Get list of Screenshot in original_screenshots_dir
list_of_screenshots=original_screenshots_dir.glob("Screenshot*") # getting object Path.glob NOT the files

# Move Screenshots to another dir, moved_screenshots_dir
for screenshot in list_of_screenshots:
    new_screenshot_path=moved_screenshots_dir/screenshot.name
    screenshot.rename(new_screenshot_path)
