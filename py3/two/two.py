info = {}
name = input("please input your name:")
info["name"] = name
age = int(input("please input your age:"))
info["age"] = age
# for i in info.items():
#     print(i)
# print('finish!!')



# for k,v in info.items():
#     print("%s--->%s" %(k,v))

for k,v in info.items():
    print(k+':',v)