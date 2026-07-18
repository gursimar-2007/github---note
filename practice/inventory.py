# students = {
#     1: ["Mmw", "k12", 1998],
#     2: ["Mmw", "k12", 1998],
#     3: ["Mmw", "k12", 1998]
# }
# for id, data in students.items():
#     print(id)
#     for info in data:
#         print(info)
cars={
    1:{"name":"mercedes","price":900000,"quantity":100},
    2:{"name":"LUNA","price":900000,"quantity":100},
    3:{"name":"WAGONR","price":900000,"quantity":100},
    4:{"name":"LORD ALTO","price":900000,"quantity":100},
}
for value in cars.values():
    if value["name"] == "mercedes":
        value["name"] = "TATA"

for car in cars.items():
    print(car)