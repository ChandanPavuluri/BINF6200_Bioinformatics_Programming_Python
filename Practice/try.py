
import os
final = ‘/Users/ckpav/PycharmProjects/BINF6200/Practice/result.txt'

try:
    os.path.exists(final)
    if True:
        os.remove(final)
except OSError as e:
    print(f “Error: {e.strerror}”)



