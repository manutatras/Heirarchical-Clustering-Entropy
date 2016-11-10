
Hierarchical clustering based on Information loss

#### Requirements ####

-pandas
-numpy
-pickle
-scipy
-matplotlib

#### How to Run ####

## To Run the clustering

# Edit the main.py file
df		: input pandas dataframe

 -------------------------------------------------------
| Vectorname | Attr-1 | Attr-2 | Attr-3 | .... | Attr-n |
 -------------------------------------------------------
| Entity_1	 |   95	  |   56   |   45	| .... |   23   |
| Entity_2	 |   0	  |   45   |   89	| .... |   15   |
| Entity_3	 |   12	  |   23   |   78	| .... |   29   |
| ....		 |  ...	  |  ...   |  ...	| .... |   40   |
| Entity_m	 |   35	  |   90   |   3	| .... |   96   |
 --------------------------------------------------------

lam = Variable used for smoothing

# Run the clustering algorithm
$ python main.py


Will create three files

hierarchy_Z.pkl      	: File used for ploting the dendrogram
hierarchy_details.pkl	: List of [list of heights(distance) of clusters, maximum depth used to cut the heirarchical clusters]
final_dataframe.pkl		: Dataframe contains the vectors and corresponding clusters
						  Read the file using >pickle.read(open("final_dataframe.pkl","rb"))

## To see the Dendrogram

$ python display_dendro.py


