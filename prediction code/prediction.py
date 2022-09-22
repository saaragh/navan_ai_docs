import tensorflow as tf
import numpy as np
import argparse

# get path to the downloaded model and image to predict as arguments 
parser = argparse.ArgumentParser(description='Argument to collct info')
parser.add_argument('--model_path', help='path to the downloaded model')
parser.add_argument('--image_path', help='path to the test image')
args = parser.parse_args()
model_path = args.model_path
image_path = args.image_path

# only for testing
# model_path = "61821920.h5"
# image_path = "1.jpg"

#load model
model = tf.keras.models.load_model(model_path)
input_shape = model.input_shape[1:]

# image preprocessing
img = tf.keras.preprocessing.image.load_img(image_path,target_size=input_shape)
img = tf.keras.preprocessing.image.img_to_array(img)
img = np.expand_dims(img, axis=0)

# prediction
result = model.predict(img)

print(result)