import argparse 
import pyfiglet
import os
from Generator import Generator

class App:
	_BANNER = pyfiglet.figlet_format("Spiral-AG")

	def generate(self):
		print(self._BANNER)
		print("Please insert the full image path.")
		path=input()
		generator = Generator()
		generator._setup(path)

os.system('cls' if os.name == 'nt' else 'clear')
app = App()
app.generate()
				
