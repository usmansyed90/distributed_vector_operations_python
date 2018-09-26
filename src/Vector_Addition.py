# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 16:57:39 2017

@author: Usman
"""


import threading
import random,time,math,numpy as np
from matplotlib import pyplot as plt

def SeqAdd(vectorA,vectorB,vectorC):
    for r in range(0, len(vectorA)):
        vectorC[r]=int(vectorA[r])+int(vectorB[r]) #Adding Vector A and B to C sequentially
    #print( vectorC)

#def Minimum(minimum,maximum,lock,i,step,vec_size,vectorA,vectorB,vectorC):

def AddVectors(minimum,maximum,lock,i,step,vec_size,vectorA,vectorB,vectorC): #Vector process definition
   lock.acquire() #Acquiring Lock
   try:
       print (threading.current_thread()) #printing currentthread
       threadname=threading.current_thread()
       #print (threadname.split( ))
       for i in range(minimum,maximum,1):                #For loop with (Distributed Data)
                     vectorC[i]=int(vectorA[i])+int(vectorB[i])    #Adding Vector B with Vector A and saving in Vector C

   finally:
#    print("Vector A : ",vectorA) #Printing Value
#    print("Vector B : ",vectorB) #Printing Value
#    print("Vector C : ",vectorC) #Printing Value
    lock.release() #Releasing Lock
    return

def main():                                 #main function
        print("")
minimum=0 #Min/Max Variables
maximum=0
vec_size=100000  #Declaring size for Vector 1 with 10**7
vectorA=[None]*vec_size
vectorB=[None]*vec_size
vectorC=[None]*vec_size
Sum_Time=0
lock=threading.Lock() #making a new lock object
nThreads=input("Please input number of threads you want to initialize: ")
threads=[]
step=int(vec_size)/int(nThreads) #CAlculating the Size of Chunk one jump needs to be for the thread
final_chunk=int(step)*int(nThreads)
print("Size of Vector: ",vec_size)
print("Number of threads: ",nThreads)
print("Size of 1 chunk: ",int(step))
#print("Final Chunk: ",final_chunk)##Outer loop will befor the threads
for i in range(0,len(vectorA),1):
           vectorA[i]=1
           vectorB[i]=1
           vectorC[i]=1
      
      
for i in range(0,vec_size,int(step)):
        if(i+int(step)<=vec_size and maximum!=vec_size):   ##So that is stays within limits
            minimum=i
            maximum=int(i+int(step))
            if(i+int(step)==final_chunk):
                #print("final chunk reached")
                maximum=maximum+(vec_size-final_chunk)
#            print("Min: ",minimum)
#            print("Max: ",maximum)
#            AddVectors(int(minimum),int(maximum),lock,i,step)
            #########Calling Addition Functions on Thread
            time.sleep(0.5)
            start = time.clock()
            t=threading.Thread(target=AddVectors,args=(int(minimum),int(maximum),lock,i,step, vec_size,vectorA,vectorB,vectorC))
            t.start()
            threads.append(t)
#Calling the sequentual Addition fo rcomparative analysis
for x in range(len(threads)):
    t.join()
end = time.clock()
#print("Vector A: ",vectorA)
#print("Vector B: ",vectorB)
#print("Vector C: ",vectorC)
print ("Processing Time for Paralell Addition: ",round(end - start,4))
startSeq = time.clock()
SeqAdd(vectorA,vectorB,vectorC)            
endSeq = time.clock()       
print("Process Time for Sequential Addition: ",round(endSeq-startSeq,4)) #Printing Parallell Time
print("Sequential Time - Paralell Time :",round((endSeq-startSeq)-(end-start),4)) #Printing Sequential Time
if((endSeq-startSeq)>(end-start)):
    print("Paralell Mechanism was",round((((endSeq-startSeq))-((end-start)))/(end-start),4),"% Faster")
if((endSeq-startSeq)<(end-start)):
    print("Sequential Mechanism was",round((((end-start))-((endSeq-startSeq)))/(endSeq-startSeq),4),"% Faster")
if((endSeq-startSeq)==(end-start)):
    print("Sequential and Paralell were same")
x_axis=["Seq Mech Time","Par Mech Time"]
y_axis=[round((endSeq-startSeq),4),round((end-start),4)]

ind=np.arange(len(x_axis))
print("Graph shows the times for Paralell and Sequential Mechanisms")
plt.bar(ind,y_axis)
plt.xticks(ind,x_axis)
if __name__ == "__main__":
    main()           