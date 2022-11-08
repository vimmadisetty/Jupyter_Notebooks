import os
import glob
import pandas as pd


os.chdir("H:\Connecting_counties_to_Metropolitan\Census_Tracts_data")

df=pd.DataFrame()
for file in os.listdir():
    if(file.endswith('.csv')):
        df=df.append(pd.read_csv(file,sep='delimiter', header=None))

df.to_csv('zing.csv',index=False)
        





'''
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

# merging the files
joined_files = os.path.join("H:\Connecting_counties_to_Metropolitan\Census_Tracts_data", "*.csv")
  
# A list of all joined files is returned
joined_list = glob.glob(joined_files)
  
# Finally, the files are joined
df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
df.to_csv('zing.csv',index=False)

'''