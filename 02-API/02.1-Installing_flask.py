#Useless sciprt, but I like this stuff

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
    
def main():    
    install('Flask==2.0.3')

 
if __name__ == "__main__":
    main()
