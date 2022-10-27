import json
from operator import itemgetter
import re
import math
import pprint


def line_len(input):
    result = {}
    i = 0
    for line in input:
        result[i] = (len(line))
        i +=1
    return result

def cal_dis(input):
    disttance_mat= []
    for x in input.keys():
        res = {x:{i:abs(input[i]- input[x])for i, val in input.items() if i != x}}
        disttance_mat.append(res)


    pp = pprint.PrettyPrinter(width=41, compact=True)
    pp.pprint(disttance_mat)  
    return disttance_mat

def get_min_dis(input):
    result= []
    for matrix in input:
        for x, y in matrix.items():
            result.append(min(matrix[x], key=matrix[x].get))
    
    return result


# TODO: Add function for point merge

data_file = open("../yelp_academic_dataset_review.json")
data = []

limit = 10


for line in data_file:
    data.append(json.loads(line)['text'])
    if len(data) == limit:
        res = line_len(data)
        print(res)

        a = cal_dis(res)

        print(get_min_dis(a))
        break
data_file.close()



