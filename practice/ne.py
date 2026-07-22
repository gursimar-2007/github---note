listers=[
    {"name":"name1","roll":"11","perc":"87%"},
    {"name":"name2","roll":"12","perc":"92%"},
    {"name":"name3","roll":"13","perc":"98%"}
]
i=0
print(f"{"s.no":<20}| {"name":<20}| {"rollno":<20}| {"perc":<20}|")
print("-"*88)
for lister in listers:
    # print(lister)
    i+=1
    print(f"{i:<20}| {lister["name"]:<20}| {lister["roll"]:<20}| {lister["perc"]:<20}|")
# print(i)
