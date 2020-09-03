# what condition finally will not execute
import os

try:
    print('Try...')
    os._exit(0)
except:
    print('Except...')    
else:
    print('Else....')
finally:
    print('Finally...') 
    
              
               