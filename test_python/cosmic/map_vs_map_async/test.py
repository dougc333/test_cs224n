#4 choices in sync vs async, multi-args, concurrenct, blocking, ordering
from multiprocessing import Pool
import time
import os
import threading

#each process gets a fn. 

#map waits for all 10 functions to be done before proceeeding so you
#see all 10 functions completing before the print statements
def f(x):
    print(x*x,os.getpid(),threading.currentThread(),threading.active_count())
    time.sleep(4)


if __name__=="__main__":
    pool = Pool(processes=4)
    pool.map(f,range(10))
    #r = pool.map_async(f,range(10))
    print("HERE")
    print("MORE")
    #r.wait()
    print("DONE")



    #map_async starts processing 10 fns when r.wait() so you see 10fns start after HERE MORE
    #then they execute followed by done
    #map_async is non blcoking whereas mpa is blocking. Does this show the blocking/non_blocing 
    #behavior? r.wait() causes map_async to block. blocking means wait for r to finish. 
    # like threads wo worrying about locks, is this true? no. we didnt do any writes. 
    #