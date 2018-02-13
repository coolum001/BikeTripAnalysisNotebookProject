from urllib.request import urlretrieve
import pandas as pd

def load_csv_datetime_data(url=None, file_path=None):
    '''
    Load a csv dataset from a file location, of failing that, a url.
    
    This function assumes that the file/url nominated holds csv data,
    with one column holding datetime values, labelled 'Date', and 
    the first data column hold west bound counts
    the second data column hold east bound counts
    
    Input:
    url: string: the url to retrieve data from for the nominate file is missing
    file_path: string: the path holding/to hold the csv data set
    
    Returns:
    A pandas dataframe, with columns "West", "East", and a datetime index
    
    Exceptions:
    Throws assertion failures if the url and file_path parameters are not supplied
    
    '''
    assert not (file_path==None), 'No save file path specified'
    assert not (url==None),  'No download url specified'
    
    try:
        b_file = open(file_path)
    except:
        # file not there yet
        # request url 
        urlretrieve(url, file_path)
    #end try
    
    # read the csv file.  colm named 'Date' can be used as an index
    bikedf = pd.read_csv(file_path, index_col='Date', parse_dates=True, infer_datetime_format=True)
    # retitle colms with shorter names
    bikedf.columns = ['West', 'East']
    
    return bikedf
#end load_bike_data