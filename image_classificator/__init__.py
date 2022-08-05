import numpy as np
import tensorflow as tf
from tensorflow import keras
from pathlib import Path

class ImageClassificator:

	def __init__(self):
		script_location = Path(__file__).absolute().parent
		file_location = script_location / 'my_model'
		self.model = keras.models.load_model(file_location)
		self.class_names = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']

	def analyze_image(self, image):
		img_array = tf.keras.utils.img_to_array(image)
		img_array = tf.expand_dims(img_array, 0)  # Create a batch
		predictions = self.model.predict(img_array)
		score = tf.nn.softmax(predictions[0])

		# Category , Percent
		return self.class_names[np.argmax(score)], 100 * np.max(score)