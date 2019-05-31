import pandas as pd
df=pd.DataFrame({'a':[11,True,31,454,45,45,45],'b':[21,22,23,45,45,45,45]})
print("Print first five rows of the dataframe")
print(df.head())
print("Print A column")
print(df['a'])
print("Print Row 2 and column 1")
print(df.iloc[1,0])
df=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})
df[df['a']<2]
df.to_csv("C:\\Users\\lalit goyal\\Desktop\\python\\panda_to_csv1.csv")
