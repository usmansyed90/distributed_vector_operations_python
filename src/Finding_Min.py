# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 17:42:08 2017

@author: Usman
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 01:06:44 2017

@author: Usman
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 13:38:36 2017

@author: Usman
"""


import threading
import random,time,math,numpy as np
from matplotlib import pyplot as plt
def SeqMin(vectorA):
    #print("Vector A",vectorA) 
    print("Minimum Value from SEQ:",min(vectorA)) #Minimum from Sequential
    return  min(vectorA)#Return Min from Vector C sequentially
    #print( vectorC)

#def Minimum(minimum,maximum,lock,i,step,vec_size,vectorA,vectorB,vectorC):

def MinVectors(minimum,maximum,lock,i,step,vec_size,vectorA,vectorMin,finalVectorlist): #Vector process definition
   global Temp
   try:
       #print (threading.current_thread()) #printing currentthread
       localvariable=max(vectorA)
       for i in range(minimum,maximum,1):                #For loop with (Distributed Data)
          #vectorMin.append(vectorA[i])
          #print("Vector Append:",vectorMin)
          if(vectorA[i]<localvariable):    #Getting min of Vector A
           localvariable=vectorA[i]
                      #print("Local Variable: ",localvariable)
                    
       

   finally:
       lock.acquire() #Acquiring Lock
       if (Temp==0 or Temp>localvariable):
           Temp=localvariable
       #print("TEMP: ",Temp) #Printing Value
       lock.release() #Releasing Lock
    #print("MIN FROM THREAD FUNC",Temp)
       del vectorMin[:]
    #print("TEMP: ",Temp)
    #finalVectorlist.append(Temp)
   return 

def main():                                 #main function
        print("")
vectorMin=[]
finalVectorlist=[]
Temp=0 #Temp variable to store temporary minimum value
minimum=0 #Min/Max Variables
maximum=0
finalMin=[]
ret=0
vec_size=1000  #Declaring size for Vector 1 with 10**7
vectorA=[None]*vec_size
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
           vectorA[i]=random.randint(1,1000)

      
      
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
            t=threading.Thread(target=MinVectors,args=(int(minimum),int(maximum),lock,i,step, vec_size,vectorA,vectorMin,finalVectorlist))
            t.start()
            threads.append(t)
#Calling the sequentual Minimum Function for comparative analysis
for x in range(len(threads)):
    t.join()
    #finalMin.append(ret)
print("Minimum Number from Paralell Mech: ",Temp)
end = time.clock()
print ("Processing Time for Paralell Minimum Function: ",round(end - start,4))
startSeq = time.clock()
SeqMin(vectorA)   #Calling Seqential Min         
endSeq = time.clock()       
print("Process Time for Sequential Minimum Function: ",round(endSeq-startSeq,4)) #Printing Parallell Time
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