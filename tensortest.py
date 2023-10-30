import tensorflow
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "0"