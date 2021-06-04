# documentation


PL_data(flist, **kwargs)
 
**parameters**: 

               flist: list of the paths pointing to the desired data from the working directory

            **kwargs: the kwargs associated with the numpy.genfromtxt() function ex. 'skip_header'
            
**properties**: 

               PL_data.samples: returns the list of samples that is currently in the dictionary

            PL_data.unique_ids: returns the list of filenames/unique_ids in the dictionary
            
            PL_data.dictionary: returns the current dictionary
           
**methods**: 

                      PL_data.plot_all(*args,**kwargs): plots all of the data formated via the args and kwargs in matplotlib

         PL_data.plot_sample([sample],*args, **kwargs): 
                                                       
                                                       [sample]:list of sample names to be plotted ex. ['H1146', 'H1156']
         
                                              *args and **kwargs: matplotlib.pyplot formattin
                                                         
         PL_data.plot_id([IDs],*args,**kwargs): 
         
                                                [IDs]: list of the IDs desired to be plotted
         
                                   *args and **kwargs: matplotlib.pyplot formatting
                                                 
         PL_data.append(sample,ID,data): 
         
                                         sample: name of sample
         
                                             ID: name of file/ID
                                             
                                           data: the data associated with the sample and ID
                                           
          PL_data[sample]: returns a dictionary of all the data associated with sample, the keys being the unique ids
          
          PL_data[sample][ID]: returns the data associated with an ID
          
          len(PL_data): returns the number of samples currently in the dictionary
          
          
         
   
       
         

