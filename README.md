# Main Logic Flow

## 1. Check if the specific source file already exists in the destination directory

- <font color="red">False</font>: No, does not exist: Simply copy source to destination.

* <font color="green">True</font>: Yes, compare files and proceed based on criteria

## 2. When comparing files:

- I should compare size for now. _Though in the future I can implement modified date, content check (hash check) comparison_

* If source file is larger: Replace destination (Yes, a new file can have less data)
* If destination file is larger: Rename destination file (file_YYYYMMDD_HHMM.bck) and copy the source file
* If identical size: Skip copying.

## 3. I should include Error Handling:

- Permission issues
- Disk space constraints
- Read/write errors
- Interrupted operations
