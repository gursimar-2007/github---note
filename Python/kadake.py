# [===]
lists=[-2,1,-3,4,-1,2,1,-5,4]
def hello(lists):
    assumed_max=actual_max=lists[0]
    for list in lists[1:]:
        assumed_max=max(list,assumed_max+list)
        actual_max=max(actual_max,assumed_max)
    return actual_max
print(hello(lists))
