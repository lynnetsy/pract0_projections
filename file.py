from pprint import pprint

def read(filename):
    result = []

    f = open(filename)
    data = f.readlines()
    f.close()

    for n, line in enumerate(data, 1):
        if (n > 1):
            toList = line.split(',')
            value = {}
            value["id"] = toList[0]
            value["lon"] = int(toList[1])
            value["lat"] = int(toList[2])

            result.append(value)

    print("points:")
    pprint(result)

    return result
