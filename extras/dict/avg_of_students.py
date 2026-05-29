marks={
    "rajawat": 75,
    "neelima" : 50,
    "pranjali" : 40

}

print(marks.keys())
print(marks.values())

average = sum(marks.values())/len(marks.values())
print(average)