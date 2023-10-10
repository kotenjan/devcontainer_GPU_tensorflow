import tensorflow as tf

gpus = tf.config.list_physical_devices('GPU')
print("Available GPUs:", gpus[0][0])
