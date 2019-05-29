# change-file-structure
Naive script to convert a file-type-oriented file structure into a directory-date-oriented structure


Run it like so (Python 3.6):
```bash
$ python src/change_file_structure <SOURCE_DIR> <DESTINATION_DIR>
```

### What is does:

Naive implementation to convert a file-type-oriented file structure such as:

```bash
dir__
     |_raw__day1__file1
     |    |     |_file2
     |    |        :
     |    |
     |    |_day2__file3
     |          |_file4
     |          |_file5
     |             :
     |      
     |_tif__day1 _file6
     |    |     |_file7
     |    |        :
     |    |
     |    |_day2__file8
     |          |_file9
     |          |_file10
     |             :
     |       
     |_dev__day1__file11
     |    |     |_file12
     |    |        :
     |    |
     |    |_day2__file13
     |          |_file14
     |          |_file15
     |             :
     :
```

into a date-oriented file structure:

```bash
dir__day1__raw__file1
     |  |     |_file2
     |  |         :
     |  |
     |  |__tif__file6
     |  |     |_file7
     |  |         :
     |  |
     |  |__def__file11
     |        |_file12
     |           :
     |
     day2__raw__file3
     |  |     |_file4
     |  |     |_file5
     |  |         :
     |  |
     |  |__tif__file8
     |  |     |_file9
     |  |     |_file10
     |  |         :
     |  |
     |  |__def__file13
     |        |_file14
     |        |_file15
     |           :
     :
 ```
 
Only copies, but does not delete, the original structure to the destination directory.

