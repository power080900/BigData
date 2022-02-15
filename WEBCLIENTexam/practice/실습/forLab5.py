import random
start = int(random.randint(1,10))
end = int(random.randint(30,40))
sumi = 0

if start % 2 == 0 :
    for i in range(start, end+1, 2) :
        sumi += i
elif start % 2 == 1 :
    for i in range(start + 1, end+1, 2) :
        sumi += i
print("X :",start)
print("Y :",end)
print("X부터 Y까지의 짝수의 합:",sumi)