'''feature generation base classes, the container for data is the sframe.SFrame'''
#-*- coding: utf-8 -*-

import logging

LOGGER = logging.getLogger(__file__)

# pylint: disable=too-few-public-methods
class InPlaceTransfer(object):
    '''do in-place transfer for features'''
    def __init__(self, col_name, function, dtype=None):
        '''
        col_name: column name of feature
        function: function which used to transfer feature
        dtype: return data type of function
        '''
        self.type = 'inplace'
        self.col_name = col_name
        self.function = function
        self.dtype = dtype

    def transfer(self, sarr):
        '''
        sarr: sframe.SArray object
        '''
        return self.function(sarr[self.col_name])


class UnPackTransfer(object):
    '''
    to do unpack tranfer for features, such as 
    transfer one numerical value feature to multiple 
    discrete binary (0, 1) value feature
    '''
    def __init__(self, col_name, function, dtype=None):
        '''
        col_name: column name of feature
        function: function which used to transfer feature
        dtype: data type for each object of return list of function
        '''
        self.type = 'unpack'
        self.col_name = col_name
        self.function = function
        self.dtype = dtype

    def transfer(self, sarr):
        '''
        sarr: sframe.SArray object
        return: list of values
        '''
        return self.function(sarr[self.col_name])

class JoinTransfer(object):
    '''
    join muliple features to generate another new feature
    '''
    def __init__(self, col_names, result_col_name, function, dtype=None):
        '''
        col_names: column name list of features
        function: function which used to transfer feature
        dtype: return data type of function
        '''
        self.type = 'join'
        self.col_names = col_names
        self.result_col_name = result_col_name
        self.function = function
        self.dtype = dtype

    def transfer(self, sarr):
        '''
        sarr: sframe.SArray object
        '''
        params = [sarr[col_name] for col_name in self.col_names]
        return self.function(params)


#feature transfer on sframe.SFrame object
def feature_transfer(sf_data, transfer_utils):
    '''
    sf_data: sframe.SFrame object
    transfer_utils: list of tranfer objects (InPlaceTransfer, UnPackTransfer, JoinTransfer)
    '''
    for trans_obj in transfer_utils:
        #for inplace transfer
        if trans_obj.type == 'inplace':
            sarr = sf_data.apply(trans_obj.transfer, trans_obj.dtype)
            sf_data[trans_obj.col_name] = sarr
        #for unpack transfer
        elif trans_obj.type == 'unpack':
            sarr = sf_data.apply(trans_obj.transfer, trans_obj.dtype)
            new_sf = sarr.unpack(trans_obj.col_name)
            sf_data.remove_column(trans_obj.col_name)
            sf_data.add_columns(new_sf)
        #for join transfer
        elif trans_obj.type == 'join':
            sarr = sf_data.apply(trans_obj.transfer, trans_obj.dtype)
            sf_data[trans_obj.result_col_name] = sarr
        else:
            LOGGER.warning("unknown type of transfer object: %s", trans_obj.type)

    return sf_data
