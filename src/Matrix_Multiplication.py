# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:44:37 2017

@author: Usman
"""
import random,time,numpy as np,threading
from matplotlib import pyplot as plt

def multiply(rows,columns,matrix,matrix2,matrix3):
    for i in range(0,int(rows),1):
        for j in range(0,int(columns),1):
            value=0
            for k in range(0,int(columns),1):
                value+= matrix[i][k]*matrix2[k][j]
            matrix3[i][j]=value
    #print ("Sequential: ",matrix3)


def multiparalell(min_row_matA,max_row_matA,min_col_matB,max_col_matB,columns,lock,i,matrix,matrix2,matrix3):
    lock.acquire() #Acquiring Lock
    try:
        #print ("Before Matrix: ",matrix3)
        for i in range(min_row_matA,max_row_matA,1):
            for j in range(0,columns,1):
                value=0
                for k in range(0,columns,1):
                    value+= matrix[i][k]*matrix2[k][j]
                matrix3[i][j]=value
        #print ("Paralell Matrix: ",matrix3)
    finally:
        lock.release()    

def main(): 
    rows=int(input("Input the dimensions for NxN matrix:"))
    nthreads=4#input("Input the number of threads: ")
    columns=rows    
    min_row_matA=0 #Variables used to divide matrix in the chunks
    max_row_matA=0
    min_col_matB=0
    max_col_matB=0
    threads=[]
    step=int(rows)/int(nthreads) #deciding how far each thread should process the first matrix
    lock=threading.Lock() #making a new lock object
    final_chunk=int(step)*int(nthreads)
    matrix = [[1 for i in range(int(rows))] for i in range(int(columns))] #declaring the matrices
    matrix2 = [[1 for i in range(int(rows))] for i in range(int(columns))]
    matrix3 = [[0 for i in range(int(rows))] for i in range(int(columns))]
    #print (matrix)
    #print (matrix2)
        
    for i in range(0,int(rows),int(step)):
        #print("Step: ",int(step))
        if(i+int(step)<=rows and max_row_matA!=rows): #If number of threads are even
            #print(max_row_matA)
            min_row_matA=i  #For VectorA - dividing it into parts
            max_row_matA=i+int(step)          
            min_col_matB=i
            max_col_matB=i+int(step)
            #print("First IF Called")
            if(rows%int(nthreads)!=0 and i+int(step)==final_chunk): #If final chunk has been reached and still one some rows remain
            #    print("Second IF Called") #Extend the number of rows for the last thread.
                max_row_matA=max_row_matA+(rows-final_chunk)
                max_col_matB=max_col_matB+(rows-final_chunk)
            time.sleep(0.5)
            start = time.clock()
            #print("Thread: ",i,"(",min_row_matA,",",max_row_matA,")")
           #print("Thread: ",i,"(",min_col_matB,",",max_col_matB,")")
            t=threading.Thread(target=multiparalell,args=(int(min_row_matA),int(max_row_matA),int(min_col_matB),int(max_col_matB),columns,lock,i,matrix,matrix2,matrix3))
            t.start()
            threads.append(t)
        
    for x in range(len(threads)):
        t.join()
    end = time.clock()
    #print("Paralell Matrix: ",matrix3)
    #print ("Processing Time for Paralell Addition: ",round(end - start,4))
    startSeq = time.clock()
    multiply(rows,columns,matrix,matrix2,matrix3)            
    endSeq = time.clock()       
    print("Process Time for Sequential multiplication: ",round(endSeq-startSeq,4)) #Printing Parallell Time
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