import os, platform
os.system('git pull')
 
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from HOT import dmc_apv
    dmc_apv()
elif bit == '32bit':
    from HOT import dmc_apv
    dmc_apv()
