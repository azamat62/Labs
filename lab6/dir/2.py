import os
print('Exist:', os.access('words.txt', os.F_OK))
print('Readable:', os.access('words.txt', os.R_OK))
print('Writable:', os.access('words.txt', os.W_OK))
print('Executable:', os.access('words.txt', os.X_OK))