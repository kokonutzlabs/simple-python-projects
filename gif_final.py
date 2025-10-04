import imageio.v3 as iio  # Import the imageio library version 3

# List of image file names (make sure these exist in the same folder)
filenames = ['team-pic1.png', 'team-pic2.png']

# Empty list to store image data
images = []

# Read each image and add it to the images list
for filename in filenames:
    images.append(iio.imread(filename))

# Write all images into a GIF file
iio.imwrite('team.gif', images, duration=500, loop=0)
