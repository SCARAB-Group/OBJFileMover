# OBJFileMover
Makes syncronization of OBJ-files easy as 3.1415

## Usage:
Configure source and target paths in config.json then run OBJMover.py.

Source path is the LIMS production directory and the target paths are the background server directories. Then just run the script and watch the magic happen!

Note: the script will rename any existing file by adding a suffix with today's date, e.g. LIMSBBPROD_160102.OBJ

Works with Python 2.7. May work with other versions but this is not tested.
