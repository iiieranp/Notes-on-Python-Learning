def subset(n):
    if n==1:
        return[[],[1]] #不能×不建议用集合（可变，但元素不能修改，（且无序），但是可以遍历），不能用元组（完全不可变）
    else:
        t=subset(n-1)
        for i in subset(n-1): #注意这里是subset(n-1)而不是t，否则下面会无线递归
            i.append(n)
            t.append(i) 
            #print(t) #查看进程
        return t
