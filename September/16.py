
# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1

start = [1,3,0,5,8,5]
end =  [2,4,6,7,9,9]

join = []
for i in range(len(start)):
    join.append([start[i],end[i]])
print(join)

join = sorted(join, key=lambda x: x[1]) # sort by end times
print(join)

s = join[0][1]

meet = 1 # bcoz 1st table always available

for i in range(1,len(start)):
    if(s < join[i][0]):
        meet+=1
        s = join[i][1]

print(meet)