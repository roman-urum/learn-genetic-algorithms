l=[1,1,1,1,1,1,1,1,1,1]
#l=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#l = [1] * 50 + [0] * 50
#l = [0] * 50 + [1] * 50
print (sum(l))
#m = [ x * (i - len(l)/2) if i > len(l)/2 else -(len(l)/2 - i)*x for i, x in enumerate(l)]
#m = [ -x * (i - len(l)/2) if i > len(l)/2 else (len(l)/2 - i)*x for i, x in enumerate(l)]
m = [ -x * abs(len(l)/2 - i) if abs( len(l)/2 - i )  > 2 else x * ( len(l)/2 - abs(len(l)/2 - i) ) for i, x in enumerate(l)]
print (m)
#print (sum(m))
#print(sum(x*(i/2) if i>len(l) / 2 else x * (-i*10) for i, x in enumerate(l)))