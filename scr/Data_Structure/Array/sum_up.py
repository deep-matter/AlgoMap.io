

def sum(num , target):
    dict_ = {}
    for i , val in enumerate(num):
        x = target - val 
        print(i)
        if x in dict_:
            print(dict_[x])
            print(i)
            return [dict_[x], i ]
        dict_[val] = i

## buidling Polynomial to be evaluated

def Polynomial(num , target):
    # complexity O(n)
    dict_ = {}
    for i , val in enumerate(num):
        x = target - val 
        print(i)
        if x in dict_:
            print(dict_[x])
            print(i)
            return [dict_[x], i ]
        dict_[val] = i




if __name__ == "__main__":
    number_list =[3,7,2,15]
    target = 9
    Sum = sum(number_list, target)
    print(Sum)
    

        
        