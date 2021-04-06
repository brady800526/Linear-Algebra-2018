import json

import numpy as np

#read input file.
link=[]
with open("./summary3.json","r") as f:
  link=json.load(f)

#initialize original transition matrix
original_transition=np.zeros((len(link),len(link)))
for i in range(len(link)):
  for o in link[i]:
    original_transition[i][o]=1

#normalize original transition matrix, avoid divide by 0.
totalLink=np.sum(original_transition,axis=0)
for i in range(len(link)):
    if(totalLink[i]==0):
        totalLink[i]=1
original_transition=original_transition/totalLink

print("Original transition matrix",original_transition)

initial_vector=np.ones(len(link))/len(link)
ordering_of_websites=np.zeros(len(link))
##########

#Todo: please implement pagerank algorithm and turn ordering_of_websites into a list representing the web pages. The order should be based on pagerank algorithm. The web page with a higher probability comes first.
cal_vector = np.zeros(len(link))
uniform_matrix = np.ones((len(link), len(link)))/len(link)
d = 0.85
dist = float('inf')

for _ in range(1000) or abs(np.sum(cal_vector  - initial_vector)) < 0.001:
  cal_vector = np.matmul(((1-d)*(uniform_matrix) + d * original_transition), initial_vector)
  dist = abs(np.sum(cal_vector - initial_vector))
  initial_vector = cal_vector

ordering_of_websites = cal_vector.argsort()[::-1]
##########

print("Your current answer",ordering_of_websites)

#turn your answer from a numpy array to list and output it as a json file.
ordering_of_websites=ordering_of_websites.tolist()
with open("answer3.json","w") as f:
    json.dump(ordering_of_websites,f)
