import tensorflow as tf

# Convert the model
converter = tf.lite.TFLiteConverter.from_saved_model('C:\Users\Lenovo\Desktop\Fit\Fittt') 
# path to the SavedModel directory
tflite_model = converter.convert()

# Save the model.
with open('model.tflite', 'wb') as f:
  f.write(tflite_model)