

t = int(input())

while t:

    def OP(N ,K ,A):
        c = 0
        for i in range(N-K+1):
            if any(A[i+j] %2 == 1 for j in range(K)):
                c+=1
        return c 
    t-=1

    arr1 = list(map(int,input().split()))

    N=arr1[0]
    K=arr1[1]

    arr = list(map(int,input().split()))
    res =[]
    op=OP(N,K,arr)
    res.append(op)

    for i in res:
        print(i)

    # i=0
    # j=K
    # bit = arr[0]

    # op=0
    # for k in range(1,K):
    #     bit |=arr[k]

    # print(bit)
    # if bit%2!=0:
    #     op+=1

    # while j<N:
    #     bit|=arr[j]
    #     bit&=arr[i]
        
    #     if bit%2!=0:
    #         op+=1
    #     i+=1
    #     print(arr[i],arr[j],bit, op)
    #     j+=1
        


    # print(op)


# t = int(input())

# while t:
#     t-=1

#     arr1 = list(map(int,input().split()))

#     N=arr1[0]
#     K=arr1[1]

#     arr = list(map(int,input().split()))

    

#     op=0

#     i=0
#     j=K
#     bit = arr[0]

#     op=0
#     for k in range(1,K):
#         bit |=arr[k]

#     print(bit)
#     if bit%2!=0:
#         op+=1

#     while j<N:
#         bit|=arr[j]
#         bit&=arr[i]
        
#         if bit%2!=0:
#             op+=1
#         i+=1
#         print(arr[i],arr[j],bit, op)
#         j+=1
        


#     print(op)
        

