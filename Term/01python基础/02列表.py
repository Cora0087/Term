name = ['小明','球球','柠檬']

#增
name.append('松韵')
print(name)
#删

name.pop()
print(name)
name.remove('小明')
print(name)
#改
name[1] = '番茄'
print(name)
#查
name.append('松韵')
name.append('小明')
print(name)
print(name[2])
print(name[-1])
#切片
print(name[:2])

