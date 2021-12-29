import sys
from lib import *


# arguments to the main file 
if not os.path.exists(str(pathlib.Path(__file__).parent.absolute()) + "/movieClips"):
    os.makedirs(str(pathlib.Path(__file__).parent.absolute()) + "/movieClips")
assert len(sys.argv) > 2, "** ERROR ** : not enough arguments have been passed"
nameScript, videoPath, folderName, mod = (arg for arg in sys.argv) 
videoPath =  str(pathlib.Path(__file__).parent.absolute()) + "/" + videoPath
assert os.path.exists(videoPath), str( "** ERROR ** :"+ videoPath +"does not exist")

# Procede to main 
initialPrint()
generateFolder(folderName)



