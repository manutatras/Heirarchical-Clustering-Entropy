
# Hierarchical clustering based on Information loss

### Requirements 

-pandas

-numpy

-pickle

-scipy

-matplotlib


### To Run the clustering

Edit the main.py file

df  : input pandas dataframe

lam : Variable used for smoothing

$ python main.py


Will create three files

hierarchy_Z.pkl      	: File used for ploting the dendrogram

hierarchy_details.pkl	: List of [list of heights(distance) of clusters, maximum depth used to cut the heirarchical clusters]

final_dataframe.pkl	: Dataframe contains the vectors and corresponding clusters. Read the file using >pickle.read(open("final_dataframe.pkl","rb"))

### To see the Dendrogram

$ python display_dendro.py


