
import json

with open('place3.json','r', encoding='utf-8') as f:
    data1 = json.load(f)
# print(json.dumps(data1, indent=4, ensure_ascii=False))


with open('program3.json','r', encoding='utf-8') as f:
    data2 = json.load(f)
# print(json.dumps(data2, indent=4, ensure_ascii=False))
Name = "서울풍물시장 청춘1번가"
place1 = data1.keys()
Address1 = data1.loc['address']

print(place1)
print(type(list(place1)))
































