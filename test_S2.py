""" Basic introduction to unit testing with Python

@brief get started with python testing by looking at https://docs.pytest.org/en/latest/getting-started.html#getstarted. Note that any script to be ran within the python testing framework (pytest) should follow the standard test discovery rules (https://docs.pytest.org/en/latest/goodpractices.html#test-discovery)
"""

import os
import pytest
print('Starting test script from working directory : '+os.getcwd())

def test_basicTrue():
    """ one of the simplest test that does nothing except saying it works..."""
    assert True


#testing session 1 functions
def load_S1_script():
    """
        utility function that tris to load the script written along the first lesson
        @throws an ImportError exception if the script file does not exist
        @return the script as a loaded module
    """
    S1_script_filename='assignments/Session1/S1_algotools.py'
    print('Trying to load target scripts:'+S1_script_filename)
    import imp
    s1_algotools=imp.load_source('session_1_script', S1_script_filename)
    return  s1_algotools



#load the scripts to check
def test_session1script_exists():
    try:
        load_S1_script()
        assert True
    except  ImportError:
        print('Expected script not found, carrefuly check the assignement instructions ')
        assert False

#def check_S1_selective_average(testList):
#    ##
#    # utility function that asserts if load_S1_script().average_above_zero works fine
#    # @param testList a list of values onto average_above_zero is applied
#    # @test ensures the function returns the correct average value
#    import numpy as np
#    #another way to process the positive elements average to compare with
#    positive_elements_float_array=np.array([i for i in testList if i >= 0], dtype=float)
#    reference_average_value=np.mean(positive_elements_float_array)
#    assert load_S1_script().average_above_zero(testList) ==reference_average_value

#------------------------------------------------------------------------------average_above_zero---------------------------------

def test_S1_selective_average_non_zeros_values():
    ##
    # @test validates average_above_zero works fine with integer values >0
    testList=[1,2,3,4]
    assert load_S1_script().average_above_zero(testList) ==2.5

def test_S1_selective_average_with_zeros_values():
    ##
    # @test validates average_above_zero works fine with integer values >=0
    testList=[0,1,2,3,4]
    assert load_S1_script().average_above_zero(testList)==2.5

def test_S1_selective_average_with_negative_values():
    ##
    # @test validates average_above_zero works fine with integer values <=0
    testList=[0,-7]
    with pytest.raises(ValueError):
        load_S1_script().average_above_zero(testList)

def test_S1_selective_average_with_string_values():
    ##
    # @test validates average_above_zero works fine with integer values <=0
    testList=['ab','c']
    with pytest.raises(ValueError):
        load_S1_script().average_above_zero(testList)

def test_S1_selective_average_with_empty_list():
    ##
    # @test validates average_above_zero works fine with an empty list
    try:
        load_S1_script().average_above_zero([])
        assert False
    except ValueError:
        assert True
        
#------------------------------------------------------------------------------Max value---------------------------------
def test_S1_max_value_with_positive_values():
    # @test validates max_value works fine with only positive values
    testList=[1,2,3,4,7]
    assert load_S1_script().max_value(testList) == 7

def test_S1_max_value_with_negative_values():
    # @test validates max_value works fine with only negative values
    testList=[-1,-2,-3,-4,-7]
    assert load_S1_script().max_value(testList) == -1

def test_S1_max_value_with_mixed_values():
    # @test validates max_value works fine with only mixed values
    testList=[1,-2,3,-4,-7]
    assert load_S1_script().max_value(testList)== 3
    
def test_S1_max_value_with_empty_list():
    # @test validates max_value works fine with an empty list
    testList=[]
    try:
        load_S1_script().max_value(testList)
        assert False
    except ValueError:
        assert True

def test_S1_max_value_with_other_type_than_list():
    # @test validates max_value works fine with an other type than list
    testList=1
    try:
        load_S1_script().max_value(testList)
        assert False
    except ValueError:
        assert True
#------------------------------------------------------------------------------Reverse_Table---------------------------------
  
    
def test_S1_reverse_table_with_positive_values():
    # @test validates reverse_table works fine with only positive values
    testList=[1,2,3,4,7]
    assert load_S1_script().reverse_table(testList) == [7,4,3,2,1]

def test_S1_reverse_table_with_negative_values():
    # @test validates reverse_table works fine with only negative values
    testList=[-1,-2,-3,-4,-7]
    assert load_S1_script().reverse_table(testList) == [-7,-4,-3,-2,-1]

def test_S1_reverse_table_with_mixed_values():
    # @test validates reverse_table works fine with mixed values
    testList=[1,-2,3,-4,-7]
    assert load_S1_script().reverse_table(testList) == [-7,-4,3,-2,1]
   
def test_S1_reverse_table_with_letters():
    # @test validates reverse_table works fine with only letters
    testList=['a','b','c','d']
    assert load_S1_script().reverse_table(testList) == ['d','c','b','a']

def test_S1_reverse_table_with_mixed_type():
    # @test validates reverse_table works fine with letters and numbers
    testList=[-1,2,3,-4,'a','b',1]
    assert load_S1_script().reverse_table(testList) == [1,'b','a',-4,3,2,-1]
    
def test_S1_reverse_table_with_empty_list():
    # @test validates reverse_table works fine with an empty list
    testList=[]
    try:
        load_S1_script().reverse_table(testList)
        assert False
    except ValueError:
        assert True

#------------------------------------------------------------------------------Reverse_Table---------------------------------
  
    
def test_S1_random_fill_sparse_with_error_type():
    # @test validates reverse_table works fine with only positive values
    testList=[1,2,3,4,7]
    assert load_S1_script().reverse_table(testList) == [7,4,3,2,1]

    
    
    