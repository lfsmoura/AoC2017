def steps(target):
    d = {
        "first": 2,
        "bpq": 2
    }
    for i in range(2,20000):
        d["first"] = d["first"] + d["bpq"] * 4
        d["bpq"] = d["bpq"] + 2
        d["last"] = d["first"] + 4 * d["bpq"]
        d["pos"] = (target - d["first"]) % d["bpq"] + 1
        d["middle"] = int(d["bpq"] / 2)
        #print (d)
        if target < d["last"]:
            return i + abs(d["middle"] - d["pos"])
    return -1



target = 289326

#print([(i,steps(i)) for i in range(10,50)])
print (steps(target))