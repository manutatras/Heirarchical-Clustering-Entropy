from Agglo_clust import Attr_group
import pickle as pk

# Read input dataframe as df
# import pandas as pd
# df = pd.read_csv("clstrdata.csv")

lam = 100
pb = Attr_group().start(df,lam,len(df.columns))
pk.dump(pb,open("final_dataframe.pkl","wb"))

