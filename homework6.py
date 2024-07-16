# работа со словарём
my_dict={"Дима":1986, "Ира":2003, "Олег":1963, "Алла":2009}
print(my_dict)
print(my_dict["Алла"])
my_dict["Глеб"]=2013
print(my_dict)
my_dict.update({"Боря":1980, "Лиза":1999})
print(my_dict)
a=my_dict.pop("Олег")
print(my_dict)
print(a)
print(my_dict.get("Ира"))
print(my_dict)
# работа со множеством
my_set={1, 2, 3, 1, 2, 4, "Bugs", True}
print(my_set)
print(my_set.add("Klass"))
tup=(1, 2, 3.6)
print(my_set.add(tup))
print(my_set)
print(my_set.discard("Bugs"))
print(my_set)