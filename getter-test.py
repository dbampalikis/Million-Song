# Test file to test the hdf5_getter
import hdf5_getters

# Open the song file
h5 = hdf5_getters.open_h5_file_read("../MillionSongSubset/data/A/A/A/TRAAAAW128F429D538.h5")
# Access the field "duration" in the file
duration = hdf5_getters.get_duration(h5)
# Print it
print duration
# Close the file
h5.close()

