#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

class PL_data():
    
    #takes a list of filenames like as above
    def __init__(self, filenames, **kwargs):
        kwargs['unpack'] = True
        self.dict, self.samples, self.ids = self.make_dictionary(filenames,**kwargs)
        self.leg = []
        
        
    def make_dictionary(self,filenames, **kwargs):
        samples = []#store the individual sample names
        unique_ids = []#store the unique dates+run
        dictionary = {}#dictionary to for convienance

        for filename in filenames:
            try:
                slash_index = filename.rindex('/')
                date_runs = filename[slash_index + 1:]
            
            except:
                continue
                
            try:
                slash_index = filename.rindex('\\')
                date_runs = filename[slash_index + 1:]
                
            except:
                slash_index = -1
                
            #open the filename and read header
            f = open(filename, 'r')
            header = f.readline()
            f.close()
            
            #extract the sample id from header
            start = header.find('\t') + 2
            length = header[start:].find('_')
            if length == -1:#also check if it was done using spacing instead of underscores
                length = header[start:].find(' ')
            
            #do the extraction
            sample = header[start: start + length]

            #load the data
            data = np.genfromtxt(filename, **kwargs)
            data1 = data[0,:]
            data2 = data[1,:]
            
            #if this is a duplicate sample
            if sample in samples:
                #add it to the dictionary in the sub dictionary under the unique ids
                dictionary[sample][date_runs] = [data1,data2]

            else:
                #if its the first 
                samples.append(sample)#append it to the sample lst
                dictionary[sample] = {date_runs: [data1,data2]} #add the subdictionary with the unique id to the existing dictionary
                
            unique_ids.append(date_runs)

        print(samples)
        print(unique_ids)
        return dictionary, samples, unique_ids
    
    
    #plots any amount of samples by name
    def plot_sample(self,sample_names,*args,clear_leg = True, show_leg = True, line_cm = None, slc = slice(None),
                    transform_x = lambda x: x, transform_y = lambda y: y, ax = None, **kwargs):
        
        lines = []
        if clear_leg:
            self.leg = []
            
        if ax is None:
            ax = plt.gca()
        
        length = 0
        for key in sample_names:
            length += len(list(self.dict[key].values()))
            
        
        if line_cm == None:
            colors = [None]*length
        else:
            evenly_spaced_interval = np.linspace(0, 1, length)
            colors = [line_cm(x) for x in evenly_spaced_interval]
        
        color_i = 0
        for key in sample_names:
            ID_sub_dict = self.dict[key]
            for sub_key in ID_sub_dict.keys():
                color = colors[color_i]
                data = ID_sub_dict[sub_key]
                line, = ax.plot(transform_x(data[0][slc]), transform_y(data[1][slc]),*args,
                                label = key + '-' + sub_key, color = color,**kwargs)
                lines.append(line)
                self.leg.append(key + '-' + sub_key)
                color_i += 1
        
        if show_leg:
            #show the legend
            ax.legend()
            
        return lines
        
        
    #plots by id name
    def plot_id(self,IDs,*args,clear_leg = True, show_leg = True, line_cm = None, slc = slice(None), transform_x = lambda x: x,
                transform_y = lambda y: y, ax = None, **kwargs):
        
        lines = []
        if clear_leg:
            self.leg = []
            
        if ax is None:
            ax = plt.gca()
            
        length = len(IDs)
        
        if line_cm == None:
            colors = [None]*length
        else:
            evenly_spaced_interval = np.linspace(0, 1, length)
            colors = [line_cm(x) for x in evenly_spaced_interval]
        
        color_i = 0
        for ID in IDs:
            values = self.dict.values()
            keys = list(self.dict.keys())
            for i,value in enumerate(values):
                key = keys[i]
                if ID in value.keys():
                    color = colors[color_i]
                    data = value[ID]
                    line, = ax.plot(transform_x(data[0][slc]), transform_y(data[1][slc]),*args,
                                    label = key + '-' + ID, color = color, **kwargs)
                    lines.append(line)
                    self.leg.append(key + '-' + ID)
                    color_i += 1
        
        if show_leg:
            ax.legend()
        
        return lines
        
        
        
    #plots all of the samples                
    def plot_all(self,*args,clear_leg = True, show_leg = True, line_cm = None, slc = slice(None), transform_x = lambda x: x, 
                 transform_y = lambda y: y, ax = None, **kwargs):
        
        lines = []
        if clear_leg:
            self.leg = []
            
        if ax is None:
            ax = plt.gca()
            
        length = len(self.ids)
        if line_cm == None:
            colors = [None]*length
        else:
            evenly_spaced_interval = np.linspace(0, 1, length)
            colors = [line_cm(x) for x in evenly_spaced_interval]
            
        color_i = 0  
        for i, dates in enumerate(self.dict.values()):
            keys = list(self.dict.keys())
            for j, data in enumerate(dates.values()):
                color = colors[color_i]
                sub_keys = list(self.dict[keys[i]].keys())
                line, = ax.plot(transform_x(data[0][slc]),transform_y(data[1][slc]),*args,
                                label = keys[i] + '-' + sub_keys[j], color = color,**kwargs)
                lines.append(line)
                self.leg.append(keys[i] + '-' + sub_keys[j])
                color_i += 1
                
        if show_leg:
            ax.legend()
        
        return lines
        
    #append a new sample to the dictionary
    def append(self,sample,ID,data):
        
        if sample in self.samples:
            self.dict[sample][ID] = [data[:,0],data[:,1]]
        else:
            self.dict[sample] = {ID: [data[:,0],data[:,1]]}
    
    
    #get a sample
    def __getitem__(self,key):
        if key in self.samples:
            return self.dict[key]
        
        values = self.dict.values()
        for i,value in enumerate(values):
            if key in list(value.keys()):
                return value[key]
    
    
    #get the length of the dictionary
    def __len__(self):
        return len(self.dict)

    def __getattr__(self,key):
        if key in self.samples:
            return self[key]
        
        values = self.dict.values()
        for i,value in enumerate(values):
            if key in list(value.keys()):
                return value[key]
            
          
