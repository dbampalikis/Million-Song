# File to load the input to the MapReduce

import os # Module providing a portable way of using operating system dependent functionality
import hdf5_getters 
import sys

# Root directory
rootdir = '../MillionSongSubset/data/A/A'

# Go through the subdirectoies, directories and files in the root directory
for subdir, dirs, files in os.walk(rootdir):
   for file in files:
      if file.endswith(".h5"):
         # Open the file
         h5 = hdf5_getters.open_h5_file_read(subdir+"/"+file)
         # Get similiar artists
         similar = hdf5_getters.get_similar_artists(h5)
         for i in range (0,99):
            # Write to standard out
            sys.stdout.write(similar[i]+"\n")
         h5.close()
