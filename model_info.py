import tensorflow as tf
from tensorflow.keras.models import load_model
#tf.keras.utils.vis_utils import plot_model

model = load_model('model/activity.model')
#print(model.summary())
tf.keras.utils.plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)
