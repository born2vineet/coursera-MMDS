__author__ = 'Vineets'

def isprime(num):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def mapper(data):
    output = {}
    for num in data:
        for i in range(2, num + 1):
            if num % i == 0 and isprime(i):
                if not i in output:
                    output[i] = [num]
                else:
                    output[i].append(num)
    return output

def reducer(data):
    output = []
    for key, value in data.items():
        output.append([key, sum(value)])
    return output

if __name__ == '__main__':
    data = [15, 21, 24, 30, 49]
    map_out = mapper(data)
    red_out = reducer(map_out)
    print 'result:', red_out
