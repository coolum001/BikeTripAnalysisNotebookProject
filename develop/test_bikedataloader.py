from bikeloader import bikeloader as bl
import tempfile
import pandas as pd

import os
import pytest


def test_load():
    '''
    pytest function to test is pandas dataframe is in the expected format
    
    we test the data column names, and the index type
    
    we also test that the data includes each hour of the day  (ie we have not mis-translated the datetime
    strings into wrong timestamps
    
    '''
    url = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
    csv_file = '../data/fremont.csv'

    bikedf = bl.load_csv_datetime_data(url=url, file_path = csv_file)
    
    assert bikedf.columns[0]=='West' and bikedf.columns[1]=='East'
    
    assert pd.core.indexes.datetimes.DatetimeIndex==type(bikedf.index)
    
    bike_timestamps = bikedf.index
    assert all(pd.unique(bike_timestamps.hour) == [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, \
                                               12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
    
#end test_load

def test_save():
    '''
    pytest function to test that downloaded url is saved to an os file
    '''
    url = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
    csv_file = '../data/pytest01.csv'
    
    os.remove(csv_file) if os.path.exists(csv_file) else None
    
    bikedf = bl.load_csv_datetime_data(url=url, file_path = csv_file)
    
    assert os.path.exists(csv_file)
    
    os.remove(csv_file) if os.path.exists(csv_file) else None
    
#end test_save

def test_asserts():
    '''
    pytest function to test if empty input parameters raise assert exceptions
    '''
    url = None
    csv_file = '../data/pytest01.csv'
    
    with pytest.raises(AssertionError):
        bikedf = bl.load_csv_datetime_data(url=url, file_path = csv_file)
    #end with
    
    url = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
    csv_file = None
    
    with pytest.raises(AssertionError):
        bikedf = bl.load_csv_datetime_data(url=url, file_path = csv_file)
    #end with
    
#end test_asserts
    
    
    

