from scipy.cluster import hierarchy
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import pickle

Z = pickle.load(open("hierarchy_Z.pkl","rb"))
plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
)
plt.show()
