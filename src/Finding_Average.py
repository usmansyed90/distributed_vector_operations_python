# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:46:31 2017

@author: Usman
"""


import threading
import random,time,math,numpy as np
from matplotlib import pyplot as plt

def SeqAvg(vectorA):
    temp_sum=0
    #print("Vector A",vectorA) 
    for x in range (len(vectorA)):
        temp_sum=temp_sum+vectorA[i]
    print("Average from Seq:",temp_sum/len(vectorA))
    return  temp_sum/len(vectorA)#Return Min from Vector C sequentially
    #print( vectorC)

def AvgVectors(minimum,maximum,lock,i,step,vec_size,vectorA,Temp,finalVectorlist): #Vector process definition

   #lock.acquire() #Acquiring Lock
   try:
       print (threading.current_thread()) #printing currentthread
       for i in range(minimum,maximum,1):                #For loop with (Distributed Data)
                    Temp+=vectorA[i]

   finally:
    finalVectorlist.append(Temp)
    #lock.release() #Releasing Lock
    #print("MIN FROM THREAD FUNC",Temp)
    #del vectorMin[:]
    #print("TEMP: ",Temp)
   #return Temp

def main():                                 #main function
        print("")
minimum=0 #Min/Max Variables
maximum=0
finalMin=[]
finalVectorlist=[]
Temp=0
vec_size=10000000  #Declaring size for Vector 1 with 10**7
vectorA=[]
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
for i in range(0,vec_size,1):
           #vectorA[i]=random.randint(1,1000)
           vectorA.append(1)

      
#print(vectorA)      
for i in range(0,vec_size,int(step)):
        if(i+int(step)<=vec_size and maximum!=vec_size):   ##So that is stays within limits
            minimum=i
            maximum=int(i+int(step))
            if(i+int(step)==final_chunk): #if the next step is the final chunk
                #print("final chunk reached")
                maximum=maximum+(vec_size-final_chunk) #Add remaining chunk to last thread
#            print("Min: ",minimum)
#            print("Max: ",maximum)
#            AddVectors(int(minimum),int(maximum),lock,i,step)
            #########Calling Minimum Function Functions on Thread
            time.sleep(0.5)
            start = time.clock()
            t=threading.Thread(target=AvgVectors,args=(int(minimum),int(maximum),lock,i,step, vec_size,vectorA,Temp,finalVectorlist))
            t.start()
            threads.append(t)
#Calling the sequentual Minimum Function for comparative analysis
for x in range(len(threads)):
    t.join()
    #finalMin.append(ret)
print("Average from Paralell: ",round(sum(finalVectorlist)/int(vec_size),4))
end = time.clock()
print ("Processing Time for Paralell Function: ",round(end - start,4))
startSeq = time.clock()
SeqAvg(vectorA)   #Calling Seqential Avg         
endSeq = time.clock()       
print("Process Time for Sequential Function: ",round(endSeq-startSeq,4)) #Printing Parallell Time
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
plt.bar(ind,y_axis)
plt.xticks(ind,x_axis)


if __name__ == "__main__":
    main()           