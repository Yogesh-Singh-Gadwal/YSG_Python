# File Handling

import os

if os.path.exists('data.txt'):
    os.remove('data.txt')
    print('File is deleted..')
else:
    print('No File is Present..')


