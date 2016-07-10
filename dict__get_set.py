person_dict = {"name":"Xiao", "sex":"male", "age":19, "job":"student"}
print(person_dict["name"])#有該欄位的話
print(person_dict["name1"])#沒有name1的欄位
#介紹 dict.get("欄位名稱key",如果沒有的話回傳的預設值)
get_name1 = person_dict.get("name","bob")
print(get_name1)
#沒有name1的欄位 看看會發生什麼事情
get_name2 = person_dict.get("name1","bob")
print(get_name2)