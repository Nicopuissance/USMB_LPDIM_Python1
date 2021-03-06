# -*- coding: utf-8 -*-
##
#
# @author Alexandre Benoit, LISTIC Lab, IUT Annecy le vieux, FRANCE
# @brief a set of generic functions for data management
#
#"""
## a variable
#a=1 # default type : int
#
## an empty list
#mylist = []
#
##a filled list
#mylist2=[1,2,3]
#
##append to a list
#mylist.append(10)
#
## a buggy list
#mybuggylist=[1,'a', "Hi"]
#
##operators
#b=a+2
#mylist_sum=mylist+mylist2
#"""
#
#
#"""
#def average_above_zero(input_list):
#    ##
#    # compute the average of positive values
#    # @input_list : the list of values to process
#    # @return the average value of all the positive elements
#
#    #init critical variable
#    positive_values_sum=0
#    positive_values_count=0
#
#    first_item=input_list[0] #just a line to generate a code smell with an unused value
#
#    #compute the average of positive elements of a list
#    for item in input_list:
#        #select only positive items
#        if item>0:
#            positive_values_sum+=item
#            positive_values_count+=1
#        elif item==0:
#            print('This value is null:'+str(item))
#        else:
#            print('This value is negative:'+str(item))
#    #compute the final average
#    average=float(positive_values_sum)/float(positive_values_count)
#    print('Positive elements average is '+str(average))
#    return float(average)
#"""
#"""#testing average_above_zero function:
#mylist=[1,2,3,4,-7]
#result=average_above_zero(mylist)
#message='The average of positive samples of {list_value} is {res}'.format(list_value=mylist,
#                                                                          res=result)
#print(message)
#"""
#
#def max_value(input_list):
#    ##
#    # basic function able to return the max value of a list
#    # @param input_list : the input list to be scanned
#    # @throws an exception (ValueError) on an empty list
#
#    #first check if provided list is not empty
#    if len(input_list)==0:
#        raise ValueError('provided list is empty')
#    #init max_value and its index
#    max_val=input_list[0]
#    max_idx=0
#    #compute the average of positive elements of a list
#    """for item in input_list:
#        #select only positive items
#        if max_val<item:
#            max_val=item
#    """
#    #generic style : iterate over the range of list indexes
#    for idx in range(len(input_list)):
#        #select only positive items
#        if max_val<input_list[idx]:
#            max_val=input_list[idx]
#            max_idx=idx
#
#
#    #generic style : iterate over the range of list indexes
#    for idx, item in enumerate(input_list):
#        #select only positive items
#        if max_val<item:
#            max_val=item
#            max_idx=idx
#
#    return max_val, max_idx
#
#def average_above_zero(tab):
#    """
#    Calcule la moyenne
#    Args:
#        tab is a list of numeric value
#
#    return:
#        the computed average
#
#    raise:
#        Value error if no positive value is found
#        Value error if input tab is not a list
#    """
#    
#    if not(isinstance(tab , list)):
#        raise ValueError('Expected a list as input')
#    
#    average =.99
#
#    valSum =0.0
#    nPositiveValue = 0
#    NMAX = len(tab)
#
#    for val in range(0,NMAX):
#        if val > 0:
#            valSum = valSum + float(val)
#            nPositiveValue = nPositiveValue+1
#
#    if nPositiveValue <= 0:
#        raise ValueError('No positif value found')
#
#    average = valSum/nPositiveValue
#
#    return average
#
#
#test_tab = [1,7,8,-5 , 5]
#moy = average_above_zero(test_tab)
#print(moy)
#
#def max_value(tabValue):
#    
#    """
#    Calcule la valeur max du tableau
#    Args:
#        tab is a list of numeric value
#
#    return:
#        the max value
#
#    raise:
#    """
#    maxTab = max(testTab)
#    return maxTab
#
#
#tab = [1,7,8,-5 , 5]
#tabMax = max(tab)
#print(tabMax)
#
#
#tab = [1,2,3,4]
#tabMax = max(tab)
#print(tabMax)
#
#
#
#
#
#"""
##test max_value function
##1 basic test, expected answer=2
#mylist=[-1,2,-20]
#mymax, mymaxidx=max_value(mylist)
#mymax_tuple=max_value(mylist)
#mymax=mymax_tuple[0]
#print('Max value of {input_list} is {max_scan}'.format(input_list=mylist, max_scan=mymax))
##==> message : "Max value of [-1, 2, -20] is (2, 1)"
#
##2 error test : Exception expected
#max_value([])
#"""
#
#"""
## hints to solve the roi_bbox function exercise: numpy basics
#
##matrix processing lib
#import numpy
#
##create a numpy matrix with specific dimensions
#size_rows=10
#size_cols=10
#myMat=numpy.zeros([size_rows, size_cols], dtype=int)
##set a value in a specific cell
#myMat[1,3]=1
#
##fil something in the matrix, the basic way (a very slow python way...)
#for row in range(5,8):
#    for col in range(7,9):
#        myMat[row,col]=1
#
##get time to measure processing speed
#import time
#init_time=time.time()
#
##filling something in the matrix, a nicer way
#myMat[2:4,5:9]=1 #assign a scalar to each cell of a subarray
#myMat[4:7,7:9]=numpy.ones([3,2]) #copy an array in a subarray
#print(myMat)
#
##get ellapsed time
#filling_time=time.time() -init_time
#print('data prefecting time='+str(filling_time))
#
##fake bounding box coordinates matrix
#xmin=0
#xmax=100
#ymin=0
#ymax=200
##how to fill the 4x2 bbox coordinates matrix, method 1 using 1D numpy arrays (ugly?)
#bbox_coords=numpy.zeros([4, 2], dtype=int)
#bbox_coords[0,:]=numpy.array([ymin, xmin])
#bbox_coords[1,:]=numpy.array([ymin, xmax])
#bbox_coords[2,:]=numpy.array([ymax, xmin])
#bbox_coords[3,:]=numpy.array([ymax, xmax])
##how to fill the 4x2 bbox coordinates matrix, method 2 using lists (shorter way)
##->create a list of lists
#coordsList=[[ymin, xmin],[ymin, xmax],[ymax, xmin],[ymax, xmax]]
##->convert to an array
#coords_array=numpy.array(coordsList)
#"""
#
#
#def average_above_zero(tab):
#    """
#    brief: computes the average of the positve values of a array  
#    Args:
#        tab :a list of numeric value, expects at least one positive values, raise Exception if not
#    Returns:
#        the computed average as a float value
#    Raises:
#        ValueError if no positive value is found
#        ValueError if input tab is not a list
#    """
#    if not(isinstance(tab, list)):
#        raise ValueError('Expected a list as input')
#    #This is a single line comment
#    average=-99
#    valSum=0.0
#    nPositiveValues=0
#    for val in tab:
#        if val>0:
#            valSum=valSum+float(val)
#            nPositiveValues=nPositiveValues+1
#    
#    if nPositiveValues <=0:
#        raise ValueError('No positive value found')
#    average=valSum/nPositiveValues
#    
#    return average
#
#
##test script for fct average_above_zero
#test_tab=[1,2,3,-5]#create a fake tab
#moy=average_above_zero(test_tab)
#print('Positive values average=')
#print(moy)
#print('Positive values average='+str(moy))
#print('Positive values average={v}'.format(v=moy))
#----------------------------------------------------------MyCode------------------------------------------------------

### @author Nicolas Duwavrent

import random
import numpy as np
#get time to measure processing speed
#import time
#-----------------------------------------------------average_above_zero-----------------------------------------------
def average_above_zero(tab):
    """
    Brief: 
        computes of the avrage of the positive value sended
    Arg: 
        a list of numeric values, except on positive value, else it will raise an Error
    Return: 
        a list with the computed average as a float value and the max value
    Raise: 
        ValueError if no positive value is found
        ValueError if input tab is not a list
    """
    if not(isinstance(tab,list)):
        raise ValueError("Expected a list as input")
    return_vals=[]
    average=0.0
    nPositiveValue=0
    valSum=0.0
    maxi=0
    #NMAX = len(tab)
    #for idx in range(NMAX)
    for value in tab:
        if value>0:
            valSum=valSum+float(value)
            nPositiveValue=nPositiveValue+1
            if (maxi<value):
                maxi=value
    if nPositiveValue<=0:
        raise ValueError("No positive value found")
    average=valSum/nPositiveValue
    return_vals=[average,maxi]
    #return return_vals
    return return_vals[0] #pour le prof




#

#def average_above_zero(input_list):
#    ##
#    # compute the average of positive values
#    # @input_list : the list of values to process
#    # @return the average value of all the positive elements
#
#    #init critical variable
#    positive_values_sum=0
#    positive_values_count=0
#
#    first_item=input_list[0] #just a line to generate a code smell with an unused value
#
#    #compute the average of positive elements of a list
#    for item in input_list:
#        #select only positive items
#        if item>0:
#            positive_values_sum+=item
#            positive_values_count+=1
#        elif item==0:
#            print('This value is null:'+str(item))
#        else:
#            print('This value is negative:'+str(item))
#    #compute the final average
#    average=float(positive_values_sum)/float(positive_values_count)
#    print('Positive elements average is '+str(average))
#    return float(average)

"""#testing average_above_zero function:
mylist=[1,2,3,4,-7]
result=average_above_zero(mylist)
message='The average of positive samples of {list_value} is {res}'.format(list_value=mylist,
                                                                          res=result)
print(message)
"""
#--------------------------------------------------MaxValue------------------------------------------------------------
def max_value(input_list):
    """
    Brief: 
        return the max value in a list
    Arg: 
        a list of numeric values, else it will raise an Error
    Return: 
        the max value
    Raise: 
        ValueError if value is found
        ValueError if input tab is not a list
    """
    if not(isinstance(input_list,list)):
        raise ValueError("Expected a list as input")
    ##
    # basic function able to return the max value of a list
    # @param input_list : the input list to be scanned
    # @throws an exception (ValueError) on an empty list

    #first check if provided list is not empty
    if len(input_list)==0:
        raise ValueError('provided list is empty')
    #init max_value and its index
    max_val=input_list[0]
#    max_idx=0
    #compute the average of positive elements of a list
    for item in input_list:
        #select only positive items
        if max_val<item:
            max_val=item
    return max_val
    
#    #generic style : iterate over the range of list indexes
#    for idx in range(len(input_list)):
#        #select only positive items
#        if max_val<input_list[idx]:
#            max_val=input_list[idx]
#            max_idx=idx
#
#
#    #generic style : iterate over the range of list indexes
#    for idx, item in enumerate(input_list):
#        #select only positive items
#        if max_val<item:
#            max_val=item
#            max_idx=idx
#
#    return max_val, max_idx


#---------------------------------------------------reverse_table------------------------------------------------------
def reverse_table(input_list):
    """
    brief: reverse a list without an other list
    Args:
        tab :a list of values, raise Exception if the list is empty
    Returns:
        the list reversed
    Raises:
        ValueError if input tab is not a list
    """
    if not(isinstance(input_list, list)):
        raise ValueError('Expected a list as input')
    if (input_list==[]):
        raise ValueError('Expected a filled list')
    temp=""
    lenght=len(input_list)-1
    
    for index in range((int)(round((lenght+1)/2))):
        temp=input_list[index]
        input_list[index]=input_list[lenght]
        input_list[lenght]=temp
        lenght-=1
    return input_list


#--------------------------------------------------------roi_bbox------------------------------------------------------
def roi_bbox(inputMat):
    """
    brief: compute the bounding box coordinates of the object.
    Args:
        tab :numpy array of numpy.bool values else raise Exception if not
    Returns:
        a numpy array 
    Raises:numpy array list
        ValueError if input tab is not composed of 0 or 1
        
    """
    if not(isinstance(inputMat, np.ndarray)):
        raise ValueError('Expected a numpy array as input')
    if not(inputMat.dtype==np.bool):
        raise ValueError('Expected an input of type numpy.bool')
        
    lmin=inputMat.shape[0]
    lmax=0
    cmin=inputMat.shape[1]
    cmax=0
    
    for l in range(inputMat.shape[0]):
        for c in range(inputMat.shape[1]):
            if (inputMat[l,c]==True):
                if l<lmin:
                    lmin=l
                if l<lmax:
                    lmax=l
                if c<cmin:
                    cmin=c
                if c<cmax:
                    cmax=c
    roi=[lmin,cmin],[lmin,cmax],[lmax,cmin],[lmax,cmax]        
    return np.array(roi)

#---------------------------------------------------random_fill_sparse--------------------------------------------------
def random_fill_sparse(npArray, K):
    """
    brief: compute the bounding box coordinates of the object.
    Args:
        tab :numpy array else raise Exception if not
    Returns:
        a numpy array 
    """
    if not(isinstance(npArray, np.ndarray)):
        raise ValueError('Expected a numpy array as input')
    largeur=npArray.shape[0]-1
    longeur=npArray.shape[1]-1
    for l in range(npArray.shape[0]):
        for c in range(npArray.shape[1]):
            npArray[l][c]=''
    Kmax=npArray.shape[0]*npArray.shape[1]
    if (K>Kmax):
        K=Kmax
    while K>0:
        y=random.randint(0,longeur)
        x=random.randint(0,largeur)
        if (npArray[x][y]!='X'):
            npArray[x][y]='X'
            K=K-1
    return npArray
#------------------------------------------------------------remove_whitespace-----------------------------------------
def remove_whitespace(string):
    """
    brief: take the string an delete the whitespace
    Args:
        string :a non empty string else raise Exception if not
    Returns:
        a list
    Raises:
        ValueError if input tab is not a list
        ValueError if input tab is not composed of 0 or 1
        
    """
    if not(isinstance(string, str)):
        raise ValueError('Expected a string as input')
    if not string:
        raise ValueError('Expected a not empty string')
    return string.replace(" ","")

#------------------------------------------------------------Shuffle---------------------------------------------------
            
def shuffle(liste):
    """
    brief: choose randomly in the given liste
    Args:
        tab :a list of values, raise Exception if not
    Returns:
        the value selected randomly
    Raises:
        ValueError if input tab is not a list
    """
    if not(isinstance(liste, list)):
        raise ValueError('Expected a list as input')
    if not liste:
        raise ValueError('Expected a non empty list')
    index=random.randint(0,len(liste)-1)
    return liste[index]

#----------------------------------------------sort_selective----------------------------------------------------------
def sort_selective(list_in):
    """
    brief: Selective sort. This algorithm consist in finding smallest values and doing permutations.
    Args:
        tab :a list of values, raise Exception if the list is empty
    Returns:
        the sorted list
    Raises:
        ValueError if input tab is not a list
        ValueError if input tab is not empty
    """
    if not(isinstance(list_in, list)):
        raise ValueError('Expected a list as input')
    if not list_in:
        raise ValueError('Expected a non empty list')
    taille=len(list_in)-1
    for lecture in range (taille):
        print (lecture)
        mini=taille
        for case in range(lecture,taille):
            if (list_in[case]<list_in[mini]):
                mini=case
        temp=list_in[lecture]
        list_in[lecture]=list_in[mini]
        list_in[mini]=temp
    return list_in   

#---------------------------------------------sort-bubble--------------------------------------------------------------
def sort_bubble(list_in):
    """
    brief: Bubble sort. It consists in pair comparisons of all the N elements to be sorted.
    Args:
        tab :a list of values, raise Exception if the list is empty
    Returns:
        the sorted list
    Raises:
        ValueError if input tab is not a list
        ValueError if input tab is not empty
    """
    if not(isinstance(list_in, list)):
        raise ValueError('Expected a list as input')
    if not list_in:
        raise ValueError('Expected a non empty list')
        
    for i in range (len(list_in)-1,0,-1):
        fini=1
        for j in range (0,i):
            if (list_in[j+1]<list_in[j]):
                temp=list_in[j+1]
                list_in[j+1]=list_in[j]
                list_in[j]=temp
                fini = 0
        if(fini):
            return list_in
    return list_in


#---------------------------------------------Print--------------------------------------------------------------------

#test_tab=[0,1,2,3,4,-6]
#
#
## a variable
#a=1 # default type : int
#
## an empty list
#mylist = []
#
##a filled list
#mylist2=[1,2,3,4,5]
#
##append to a list
#mylist.append(10)
#
## a buggy list
#mybuggylist=[1,'a', "Hi"]
#
##operators
#b=a+2
#mylist_sum=mylist+mylist2
#
#mylist3=[-1,2,-20]
#
#moy=average_above_zero(test_tab)
#print(moy[0])
#print('Positive values average={v}'.format(v=moy[0]))
#print('Max value={max}'.format(max=moy[1]))
#
#
##test max_value function
##1 basic test, expected answer=2
#
#
#
#mymax, mymaxidx=max_value(mylist3)
#mymax_tuple=max_value(mylist3)
#mymax=mymax_tuple[0]
#print('Max value of {input_list} is {max_scan}'.format(input_list=mylist, max_scan=mymax))
##==> message : "Max value of [-1, 2, -20] is (2, 1)"
#
##2 error test : Exception expected
##max_value([])
#"""
#
#"""
#print (reverse_table(mylist2))
## hints to solve the roi_bbox function exercise: numpy basics
#
##matrix processing lib
#
##create a numpy matrix with specific dimensions
#size_rows=10
#size_cols=10
#myMat=numpy.zeros([size_rows, size_cols], dtype=int)
##set a value in a specific cell
#myMat[1,3]=1
#
##fil something in the matrix, the basic way (a very slow python way...)
#for row in range(5,8):
#    for col in range(7,9):
#        myMat[row,col]=1
#
#
#init_time=time.time()
#
##filling something in the matrix, a nicer way
#myMat[2:4,5:9]=1 #assign a scalar to each cell of a subarray
#myMat[4:7,7:9]=numpy.ones([3,2]) #copy an array in a subarray
#print(myMat)
#
##get ellapsed time
#filling_time=time.time() -init_time
#print('data prefecting time='+str(filling_time))
#
##fake bounding box coordinates matrix
#xmin=0
#xmax=100
#ymin=0
#ymax=200
##how to fill the 4x2 bbox coordinates matrix, method 1 using 1D numpy arrays (ugly?)
#bbox_coords=numpy.zeros([4, 2], dtype=int)
#bbox_coords[0,:]=numpy.array([ymin, xmin])
#bbox_coords[1,:]=numpy.array([ymin, xmax])
#bbox_coords[2,:]=numpy.array([ymax, xmin])
#bbox_coords[3,:]=numpy.array([ymax, xmax])
##how to fill the 4x2 bbox coordinates matrix, method 2 using lists (shorter way)
##->create a list of lists
#coordsList=[[ymin, xmin],[ymin, xmax],[ymax, xmin],[ymax, xmax]]
##->convert to an array
#coords_array=numpy.array(coordsList)
#
#imputMat=np.zeros((5,6),dtype=np.bool)
#imputMat[2:4,3:5]=np.ones((2,2), dtype=np.bool)
#print(str(imputMat))
#print(str(roi_bbox(imputMat)))
#
#print("Remove whitespace :"+remove_whitespace("Je suis dingue"))
#
#print(random_choice(mylist2))
#imputMat=np.empty((5,10),dtype=str)
#print(random_fill_sparse(imputMat, 10))
    
#liste50=[]
#for i in range (50):
#    liste50.append(random.randint(-100,100))
#print (sort_bubble(liste50))