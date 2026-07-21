#for  i  in  range(1,6,1):
#    print('*'*i)
 
#n =5
#for  i  in  range(1,n+1):
#     print(' '*(n-i)+'*'*(2*i-1))
 
     
#for  i  in range(1,10):
#    for j  in range(1,i+1):
#        print(f"{i}*{j}={i*j}",end="\t")
#    print("\n")

#n  = 3
#for i  in  range(1,n+1):
#    print(' '*(n-i)+'*'*(2*i-1))
#for i  in  range(n-1,0,-1):
#    print(' '*(n-i)+'*'*(2*i-1))
    
    
    
n = 3
k = []
for  i  in  range  (1,n+1):
    line =  ' '*(n-i)+'*'*(2*i-1)
    k.append(line)
line2 = k + k[:-1][::-1]
print("\n".join(line2))