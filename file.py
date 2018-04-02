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

            try:
                value["id"] = toList[0]
                value["lon"] = float(toList[1])
                value["lat"] = float(toList[2])

                result.append(value)
            except ValueError,e:
                print("error",e,"on line",n)

    print("points:")
    pprint(result)

    return result
