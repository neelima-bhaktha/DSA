x=[1,2,3]
try: #if you remove the colon it will throw an error
    for i in range(len(x)+1):
        print(x.pop())
except:
    print("index out of range!!!")
#index error