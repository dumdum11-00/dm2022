import json
import re
import math

def clean_up(input):
    res = re.sub('[^A-Za-z0-9]+', ' ', input).lower().split()
    return res

def co_oc(input):
    # another way but worse
    # cnt = dict(zip(list(res),[list(res).count(i) for i in list(res)])) 
    cnt = {i:input.count(i) for i in input}
    return cnt

def cal_TF(input):
    cnt = {i:input.count(i)/len(input) for i in input}
    return cnt

def cal_IDF(input):
    cnt = {i:math.log(len(input)/(input.count(i)/len(input))) for i in input}
    return cnt

# print(count_co(clean_up(data[0])))

data_file = open("../yelp_academic_dataset_review.json")
data = []

for line in data_file:
    data.append(json.loads(line)['text'])
    if len(data) == 100:
        untrashtify = clean_up(data[0])
        print( co_oc(untrashtify))
        print("\n")
        print( cal_TF(untrashtify))
        print("\n")
        print( cal_IDF(untrashtify))
        break
data_file.close()



