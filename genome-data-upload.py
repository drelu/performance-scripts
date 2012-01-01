from webhdfs.webhdfs import WebHDFS
import os, tempfile
import time

DATA_PATH="/N/u/luckow/DATA_BFAST/hg18chr21_10"


start = time.time()
webhdfs = WebHDFS("localhost", 50070, "luckow")

webhdfs.mkdir("/hg18chr21_10/")

for i in os.listdir(DATA_PATH):
    filename = os.path.join(DATA_PATH, i)
    print "Upload file: " + filename

    webhdfs.copyFromLocal(filename, 
                      os.path.join("hg18chr21_10", os.path.basename(filename)))
    
    
elapsed_time = time.time()-start
print "Upload Time: " + str(elapsed_time) + " sec"
