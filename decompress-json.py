import zlib
import json
import base64

def decompress_data(compressed_data):
    """Decompress data and convert it back to a Python dictionary."""
    data_json = zlib.decompress(compressed_data).decode('utf-8')
    data = json.loads(data_json)
    return data

# Base64 encoded data from your file
base64_data = "eJydUstu2zAQ/JVAvdYBJVKk5VsSo0CANCiS9BAUgUBxlzZbmXQpKq0R+N9LSnUqB86lOkjQPmZmZ/clqw1ki7OMc6kgB9pQDaohrCS8UawU2cezzMoNppoueGNXKaKd39Rhtx3CzmItdUBfhzXWLr58qgly1cX0t5cT/cq1ztfKwRD/8Gl4sv1TTAF2ypttMM4e9wBupQ8btGFEHXUvvzzkRVExPhdUN4CccjLVfPV4c327vLu+urgZ8bu+qQNaeQxzeX9LKiZIlXOiNUeR03wK8/B5ObYbC33UtDvWtvWo0aNVmEZ+yYJTwzfyNC0mBi3bDvfJFrOJ/pxIDrb0NoD7lSYn+1Qt4VlGVKg7DCGSdZPOWnv82UfS3QRiha7WMZaEnSZpnZLJ3df9tTJChx7iFi3UrbOr4S+b1Kay9O8lmD5pKAhJ8mAXDTKqfpZtj+/wgQxytPoHvrHt0HYI7Z/Gobdb72LuDWDwfcLbyFj8e0Q8jNB3482Nnei76W6/3t8RxqqclLyUDTRIKpju1svv2K2zyDzt4EywsmI0LwFAkHLaEVCtrVFG2vEo4sHG8zdpzCx6mOZIpzJgyQIp1zmdCRTFjOk5zKqGVbNSUqpQQ8PEoEZ5lAHhIp1lVpCCzch8RoqzvFjQYpFX50U1p4JPSi93g0H/JAtCGCWiikw5EDw6YIg7TSYlYRsHRpu/XLZv23TBfdOabv2uAFacC57PxQBquiW2GI7XPEammAeeI6FTUYOaV+b/nqcLMgxXecDK9n8AFOB1vQ=="

# Decode from Base64 to binary data
compressed_data = base64.b64decode(base64_data)

# Decompress and convert back to Python dictionary
decompressed_data = decompress_data(compressed_data)
print(decompressed_data)
