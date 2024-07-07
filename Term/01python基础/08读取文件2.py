import json

with open('./test2.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for user_json in lines:
        user_list = user_json.split('*')
        #print(user_list)
        json_str = user_list[2]
        user_dic = json.loads(json_str)
        #print(user_dic)
        print(user_dic[0]["img_name"], user_dic[0]["points"])