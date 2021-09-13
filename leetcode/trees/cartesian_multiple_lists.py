
# function to find cartesian product of two sets
def cartesianProduct(set_a, set_b):
    result =[]
    for i in range(0, len(set_a)):
        for j in range(0, len(set_b)):
 
            # for handling case having cartesian
            # product first time of two sets
            # if type(set_a[i]) != list:        
            #     set_a[i] = [set_a[i]]
                 
            # coping all the members
            # of set_a to temp
            temp = [num for num in set_a[i]]
             
            # add member of set_b to
            # temp to have cartesian product    
            temp.append(set_b[j])            
            result.append(temp) 
             
    return result
 
# Function to do a cartesian
# product of N sets
def Cartesian(list_a, n):
     
    # result of cartesian product
    # of all the sets taken two at a time
    temp = list_a[0]
     
    # do product of N sets
    for i in range(1, n):
        temp = cartesianProduct(temp, list_a[i])
         
    return temp
 
# Driver Code
list_a = [['a', 'b', 'c'],          # set-1
          ['d', 'e', 'f'],          # set-2
          ['g', 'h', 'i']]   # set-3
lists = [['1','2'], ['3','4']]
           
# number of sets
n = len(lists)
 
# Function is called to perform
# the cartesian product on list_a of size n
print("result", Cartesian(lists, n))

# const cartesian = (lists) => {
#   let ps = []
#   let acc = [[]]
#   let i = lists.length

#   while (i--) {
#     let subList = lists[i]
#     let j = subList.length

#     while (j--) {
#       let x = subList[j]
#       let k = acc.length
#       while (k--) {
#         ps.push([x.concat(acc[k])])
#       }
#     }
#     // console.log("PS", ps)
#     acc = ps
#     ps = []
#   }
#   // console.log("ac", acc)
#   return acc.reverse()
# }

#  let words = lists
#      .reduce((results, ids) => results
#      .map(result => ids.map(id=> result.concat(id)))
#      .reduce((nested, result) => nested.concat(result), []), 
#      [[]])