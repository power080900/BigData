import pandas as pd

df = pd.read_excel('D:/lee/study/BigData/project/Data/project_program.xlsx',sheet_name="program", skiprows = 0)
name1 = df.loc[(df['Category'] == "클래식"), ['ProgramName']].values.tolist()
name2 = []
for l in name1:
    for m in l:
        name2.append(m)
image1 = df.loc[(df['Category'] == "클래식"), ['Image']].values.tolist()
image2 = []
for n in image1:
    for o in n:
        image2.append(o)


dictA = dict(zip(name2,image2))
print(dictA)







