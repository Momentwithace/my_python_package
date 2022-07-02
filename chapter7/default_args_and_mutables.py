def appender(lst = None):
    if lst is None:
        lst = []
    lst.append("You")
    return lst

print(appender())
print(appender([123]))
print(appender())
