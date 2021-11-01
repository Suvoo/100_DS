def rotations(n):
    rot = [n]
    for i in range(len(str(n))-1):
        no = list(str(n))
        temp = no[:-1]
        no[0] = no[-1]
        no[1:] = temp
        n = ''.join(no)
        n=int(n)
        rot.append(n)
    return (rot)

def isPrime(n):
    i = 2
    while i*i <= n:
        if(n%i == 0):
            return False
        i+=1     
    return True
    
n = 197

if n<10:
    if n==2 or n==3 or n==5 or n==7:
        print('coprime')
    print('no')

rot = rotations(n)
# print(rot)

c,k=0,0
for i in range(len(rot)):
    # print(isPrime(rot[i]))
    if isPrime(rot[i]) == False:
        k = 1
        break

if k == 0:
    print('coprime')
else:
    print('no')
    
        

