import pandas as pd

df = df = pd.read_excel('D:/lee/study/BigData/project/Data/project_place.xlsx',sheet_name="place", skiprows = 0)
name1 = df.loc[(df['Class'] == "미술관"), ['PlaceName']].values.tolist()
name2 = []
for l in name1:
    for m in l:
        name2.append(m)
image1 = df.loc[(df['Class'] == "미술관"), ['Image']].values.tolist()
image2 = []
for n in image1:
    for o in n:
        image2.append(o)


dictA = dict(zip(name2,image2))
print(dictA)







