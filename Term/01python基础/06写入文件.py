import json
dic = {
    'name': '秋秋',
    'age': 18,
}

#1.文件位置
#2.模型， w(直接写，会覆盖原来的内容），a（在后面拼接）

with open('D:/2023-2024第二学期小学期/Term/01python基础/date1.txt', 'w', encoding='utf-8') as f:
    json_str = json.dumps(dic, ensure_ascii=False)#ensure_ascii=False 不乱码
    f.write(json_str)
    print('成功写入....')
    pass