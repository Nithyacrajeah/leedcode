import json

try:
    with open(".")as f:
     data=json.load (f)
     print(data)


     all_user=[user["id"]for user in data]
     my_following=[user["followers"]for user in data if user["username"]=="akhil"[0]
     my_id=[user["id"]for user in data if user["username"]=="akhil"].pop()
     to_followers=set (all_user)-set(my_followings)
     to_followers.remove(my_id)
    print(to_follow)
    suggestions=random.sample(to_follow, 2)
     print(to_follow)
except Exception as e:
     print(e.__clas__)

lst=[10,11,12,13,14]
st=[*lst]
print(st)