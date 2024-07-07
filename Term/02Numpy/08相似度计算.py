import numpy as np
target_vector = np.array([1, 2])
names = ['sy', 'qq', 'lm', 'mgt']
vector_sy = np.array([4, 6])
vector_qq = np.array([1, 2])
vector_lm = np.array([10, 11])
vector_mgt = np.array([1, 3])


#方法一
dis1 = np.sum(np.power(vector_sy[0]-target_vector[0], 2) +
              np.power(vector_sy[1]-target_vector[1], 2))#计算sy到目标向量的距离平方
dis2 = np.sum(np.power(vector_qq - target_vector, 2))#计算qq到目标向量的距离平方
dis3 = np.sum(np.power(vector_lm - target_vector, 2))#计算lm到目标向量的距离平方
dis4 = np.sum(np.power(vector_mgt - target_vector, 2))#计算mgt到目标向量的距离平方

#找到最小距离的索引
np_index = np.array([dis1, dis2, dis3, dis4])
index = np.argmin(np_index)
print(names[index])

#方法二 广播
vector = np.array([vector_sy, vector_qq, vector_lm, vector_mgt])
#print(vector)
dis = np.sum(np.power(vector-target_vector, 2), axis=1)
#print(dis)
index = np.argmin(dis)  #找到最小距离的索引
print(names[index])

#范数
dis_list = np.linalg.norm(vector-target_vector, axis=1)#计算所有向量到目标向量的欧式距离
#print(dis_list)
name_zip = zip(names, dis_list)
name_zip_list = list(name_zip)
#print(name_zip_list)
#排序必须指定排序规则
name_zip_list = np.array(name_zip_list, dtype=object)
name_sort = np.argsort(name_zip_list[:, 1])
#print(name_sort)
print(names[name_sort[0]])
