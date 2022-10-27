import json
from operator import itemgetter
import re
import math
import pprint

def clean_up(input):
    res = re.sub('[^A-Za-z0-9]+', ' ', input).lower().split()
    return res

def cal_distance(input):
    result=[]
    for word in input:
        res = {word:{i:abs(len(i)- input[word])for i in input}}
  
        result.append(res)
    return result

def co_word(input):
    res = {i:len(i) for i in input}
    return res

def co_oc(input):
    # another way but worse
    # cnt = dict(zip(list(res),[list(res).count(i) for i in list(res)])) 
    cnt = {i:input.count(i) for i in input}
    return cnt

# print(count_co(clean_up(data[0])))

data_file = open("../yelp_academic_dataset_review.json")
data = []

for line in data_file:
    data.append(json.loads(line)['text'])
    if len(data) == 100:
        untrashtify = clean_up(data[0])
        char_count= co_word(untrashtify)
        pp = pprint.PrettyPrinter(width=41, compact=True)
        pp.pprint(cal_distance(char_count))
        break
data_file.close()



