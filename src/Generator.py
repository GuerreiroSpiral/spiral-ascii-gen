import numpy as np
from PIL import Image
from math import floor

class Generator:
	_ASCII_MAP_STRING = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
	_ASCII_LIST = []

	def _setup(self, image_path):
		try:
			image_data = Image.open(image_path)
			image_data = image_data.resize((64, 64), Image.ANTIALIAS)
		except Exception as e:
			print("Couldn't open image file. Printing error.")
			print(e)
			return -1
		rgb_im = image_data.convert('RGB')
		im_array = np.asarray(rgb_im, dtype=object)

		average_array = self._get_average(im_array)
		ascii_array = self._substitute_pixel(average_array)
		self._print_image(ascii_array)

	def _string_to_list(self):
		self._ASCII_LIST = list(self._ASCII_MAP_STRING)

	def _print_image(self, array):
		for x in range(0, array.shape[0]):
			for y in range(0, array.shape[1]):
				print(array[x][y][0]+array[x][y][0]+array[x][y][0], end='')
			print("\n", end='') # Prints a newline at the end of every row	

	"""
    Fetches the average brightness value of a single pixel based on RGB values, and then assigns it to its corresponding pixel position in the array.
    Formula: .33 * R + .5 * G + .16 * B
    """
	def _get_average(self, im_array):
		for x in range(0, im_array.shape[0]):
			for y in range(0, im_array.shape[1]):
				pixel = im_array[x][y]
				temp_rgb = 0
				for z in pixel:
					temp_rgb = 0.33 * pixel[0]
					temp_rgb += 0.5 * pixel[1]
					temp_rgb += 0.16 * pixel[2]
				im_array[x][y] = temp_rgb
		return im_array
		"""
    	The _ASCII_LIST constant is a list with crescent brightness-ascii character correspondence. 
    	The formula for attributing brightness x to value y in the list is:
    	255*x = 24*y or y = (24*x)/255, while ceiling values
    	"""
	def _substitute_pixel(self, average_array):
		self._string_to_list()
		for x in range(0, average_array.shape[0]):
			for y in range(0, average_array.shape[1]):
				pixel_brightness = average_array[x][y][0]
				list_index = floor((24*pixel_brightness)/255) # To prevent out-of-bounds index reference, we floor the result of the function. Impacts accuracy in some cases.
				average_array[x][y] = self._ASCII_LIST[list_index]
		return average_array


