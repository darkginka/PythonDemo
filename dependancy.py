import pandas as pd 

df = pd.read_csv("data.csv") 
district_name=[] 
dict={} 
lst=[] 

district_name = df['district_name'].tolist() 

unique_district_name=list(set(district_name)) 

# new_DF=df[df["district_name"]=="RAIGARH"] 
# print(set(new_DF['block_name'].to_list())) 

count=0 
for i in unique_district_name: 
    new_DF=df[df["district_name"]==i]  
    lst.append(list(set(new_DF['block_name'].to_list()))) 
for i in unique_district_name: 
    dict[i]=lst[count] 
    count=count+1 
print(dict) 