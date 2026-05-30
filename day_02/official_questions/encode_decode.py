def encode(strs):
    op = ""
    for i in strs:
        op += str(len(i))+"#"+i
    return op
def decode(str):
    op = []
    while str:
        ind = str.find("#")
        num = int(str[:ind])
        op_string = str[ind+1 : num+ind+1]
        op.append(op_string)
        str = str[num+ind+1:]
    return op

assert encode(["neelima", "bhaktha"])=="7#neelima7#bhaktha"
assert decode(encode(["neelima", "bhaktha"])) == ["neelima", "bhaktha"]
print("all test cases passed")
