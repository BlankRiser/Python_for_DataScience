
#Practice_1

from sklearn import tree
# install sklearn, numpy module 
clf= tree.DecisionTreeClassifier()

'''
A tree classifier is created which makes decision 
based on the next input.
'''
x=[[10,10],[10,20],[10,30],[10,40],[10,50]]
y=[[0,10],[20,10],[30,10],[40,10],[50,10]]

'''
x and y are the parameters that will be used to 
decide the outcome of the output
'''

clf=clf.fit(x,y)

#inserting the values to the tree classifier to make the decision.

predictingxy = clf.predict([[0,20]])

#predictingxy stores the result

print(predictingxy)

#Output:  [[20. 10.]]