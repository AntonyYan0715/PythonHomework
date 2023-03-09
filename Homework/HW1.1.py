import yaml

def mylist1(length):
    result = []
    
    if (length == 0):
        result.append(0)
        return result
    
    else:
        for i in range(length - 1):
            result.append(i)
        
        result.append(-sum(result))
        return result


# parameters mylist,l,r are given you as a string
# you need to return a list of integers
class ElementNotFound(Exception):
    pass

class ElementReversed(Exception):
    pass

import yaml
import functools

def mylist1(length):
    result = []
    
    if (length == 0):
        result.append(0)
        return result
    
    else:
        for i in range(length - 1):
            result.append(i)
        
        result.append(-sum(result))
        return result


# parameters mylist,l,r are given you as a string
# you need to return a list of integers
class ElementNotFound(Exception):
    pass

class ElementReversed(Exception):
    pass

def mylist2(mylist,l,r):
    mylist = list(map(int, mylist.split(',')))
    l = int(l)
    r = int(r)
    
    if (l in mylist) and (r in mylist):
        l_index = mylist.index(l)
        r_index = mylist.index(r)
        
        if l_index < r_index:
            if (r_index - l_index == 1):
                return mylist
            
            else:
                new_list = mylist.copy()
                for i in range(r_index - l_index - 1):
                    new_list.pop(l_index + 1)
            
                return new_list
        
        else:
            raise ElementReversed('elements are reversed')
    
    else:
        raise ElementNotFound('element is not found')


def mydict(dic,n):
    # print your result
    del dic[max(dic.keys())]
    
    for key in dic.keys():
        del dic[key][n]
    
    sum_dic = {}
    for key in dic.keys():
        sum_dic[sum(dic[key])] = key
    
    sum_list = sorted(sum_dic.keys(), reverse=True)
    for i in sum_list:
        print('key:', sum_dic[i], ',value:', dic[sum_dic[i]], sep='')
    

# parameter listsofint is a string of comma separated lists of ints, 
# two lists are separated by a semicolon
# example: "1,2,3;3,4,5;3,4,7"
# return the sorted intersection as a list
def findintersection(listsofint):
    list1 = []
    
    for each in listsofint.split(';'):
        list1.append(set(list(map(int, each.split(',')))))
    
    list2 = list(functools.reduce(set.intersection, list1))
    
    return sorted(list2)