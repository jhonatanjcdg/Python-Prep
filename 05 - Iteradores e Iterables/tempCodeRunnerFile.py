fibo = [0,1]
n = 2
while(n < 30):
    fibo.append(fibo[n-1]+fibo[n-2])
    n += 1
print(fibo)


# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:


print(sum(fibo))