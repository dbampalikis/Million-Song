import os
import hdf5_getters
rootdir = '../MillionSongSubset/data/A/A/A'
for subdir, dirs, files in os.walk(rootdir):
   for file in files:
      if file.endswith(".h5"):
         h5 = hdf5_getters.open_h5_file_read(subdir+"/"+file)
         similar = hdf5_getters.get_similar_artists(h5)
         for i in range (0,99):
            print similar[i]
         h5.close()