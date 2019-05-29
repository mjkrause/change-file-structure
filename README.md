# change-file-structure
Naive script to restructure a directory tree by converting parent-child relationships.


Run it like so (Python 3.6):
```bash
$ python src/change_file_structure <SOURCE_DIR> <DESTINATION_DIR>
```

### What is does:

Suppose you have a directory tree with _foo_, _bar_, and _baz_ as parent directories of _spam_ and _ham_, such as the following pattern: 

```bash
dir__
     |_foo__spam__leaf1
     |    |     |_leaf2
     |    |        :
     |    |
     |    |_ham___leaf3
     |          |_leaf4
     |          |_leaf5
     |             :
     |      
     |_bar__spam _leaf6
     |    |     |_leaf7
     |    |        :
     |    |
     |    |_ham___leaf8
     |          |_leaf9
     |          |_leaf10
     |             :
     |       
     |_baz__spam__leaf11
     |    |     |_leaf12
     |    |        :
     |    |
     |    |_ham___leaf13
     |          |_leaf14
     |          |_leaf15
     |             :
     :
```

`change-file-structure` would convert it such that _spam_ and _ham_ are now the parent directories of _foo_, _bar_, and _baz_. The above example would be converted into the following tree structure:

```bash
dir__spam__foo__leaf1
     |  |     |_leaf2
     |  |         :
     |  |
     |  |__bar__leaf6
     |  |     |_leaf7
     |  |         :
     |  |
     |  |__baz__leaf11
     |        |_leaf12
     |           :
     |
     ham___foo__leaf3
     |  |     |_leaf4
     |  |     |_leaf5
     |  |         :
     |  |
     |  |__bar__leaf8
     |  |     |_leaf9
     |  |     |_leaf10
     |  |         :
     |  |
     |  |__baz__leaf13
     |        |_leaf14
     |        |_leaf15
     |           :
     :
 ```
 
Only copies, but does not delete, the original structure to the destination directory.

