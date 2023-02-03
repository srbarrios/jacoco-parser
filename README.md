# jacoco_parser

This is a simple Python script that will parse a Jacoco XML report and will return a list of items with this format:

`<package_folder>/<source_filename>>:<line_number>`

Example: 
`com/suse/manager/webui/controllers/ImageBuildController.java:152`

Using this data format from the XML file:
```
- package name
  - sourcefile name
    - line nr (if mi == 0)
```

# jacoco_push_redis

This is a simple Python script that will parse a Jacoco XML report and will handle a Redis Set, where each key is a source filepath and the Set is the test names:

`<package_folder>/<source_filename>`

Example: 
`com/suse/manager/webui/controllers/ImageBuildController.java:152`

Using this data format from the XML file:
```
- package name
  - sourcefile name
    - line nr (if mi == 0)
```