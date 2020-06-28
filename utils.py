#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Utils functions for handling WRF-Chem model data. Specific for my PhD project.
Created on Sat  27 Jun 2020

@author: Caterina Mogno c.mogno@ed.ac.uk
"""
import xarray as xr
import pandas as pd
def reset_time_dim(ds):
    """
    Time dimension in WRF-Chem datasets is just the time index [0,1,2,3...].
    This function convert dimension Time as datetime[64].

    :param ds:
     wrf-chem xarray dataset.
    :type ds:xarray.Dataset.
    :return:
     xarray.Dataset with datetime time dim.
    :rtype: xarray.Dataset.
    """
    return ds.assign_coords(Time=pd.to_datetime(ds.XTIME.values))



def dictdata(pth_dict):
    """
    Return a dictionary of data_name:datasets given a dictionary of 
    data_name:data_path.
    Useful format for performing same operations on each dataset.
  
    :param pth_dict:
     dict of paths to datasets.
    :type pth_dict: dict
    :return:
    dictionary of xarray.Dataset.
    :rtype: dict
    """
    
    d={}
    for k,s in pth_dict.items():
        d[k]=xr.open_mfdataset(s)
        d[k]=reset_time_dim((d[k]))
        
    return d
