import json

with open('D:/2023-2024第二学期小学期/Term/01python基础/test.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    #{"img_name":"train_1.jpg",
    # "points": [[178, 1008], [425, 1008], [425, 1099], [178, 1099]] }
    for user_json in lines:
        user_dic = json.loads(user_json)
        print(user_dic)
        print(user_dic[0]["img_name"], user_dic[0]["points"])
