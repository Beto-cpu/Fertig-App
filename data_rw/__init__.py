import pandas as pd
import numpy as np
import glob
import shutil
import os

columns = ["class", "score", "fileRoute"]
data_file_route = 'data/data.csv'
images_folder_route = "data/images"

class DataRW:
	def __init__(self):
		self.data = pd.read_csv(data_file_route, index_col=0, sep=",")

	def get_data(self):
		return self.data

	def add_data(self, data, image):
		new_image_route = "{images_folder_route}/{id}.jpg".format(images_folder_route=images_folder_route, id=self.data.size)
		data = {
			"class": data["class"],
			"score": data["score"],
			"fileRoute": new_image_route
		}
		image.save(new_image_route)

		self.data.loc[len(self.data.index)] = data

		self.data.to_csv(data_file_route)

		return self.data
