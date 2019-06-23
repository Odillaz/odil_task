def bubble_sort(list1):
	#""" sort list two-by-two until completely sorted """

    #sorting pair
    n=len(list1)-1
    p=0
    r=0
    while n>0:
        for i in range(1, len(list1)):
            if list1[p]>list1[i]:
                list1[p], list1[i]= list1[i], list1[p]
                p=p+1
                n=n-1
                r=r+1
            else:
                p=p+1
                n=n-1
    #repeating until no move made
    if r>0:
        bubble_sort(list1)

    return list1


#bubble_sort([1,8,6,4])
print (bubble_sort([9,8,6,4,2, 7, 17, 19, 16, 10]))
#bubble_sort([5,19,4,1,36,99,2])

# unit tests
assert bubble_sort([9,8,6,4,2, 7, 17, 19, 16, 10]) == sorted([9,8,6,4,2, 7, 17, 19, 16, 10])
assert bubble_sort([5,19,4,1,36,99,2]) == sorted([5,19,4,1,36,99,2])
assert bubble_sort([9,8,6,4,2, 7, 17, 19, 16, 10]) == sorted([9,8,6,4,2, 7, 17, 19, 16, 10])
assert bubble_sort([5,19,4,1,36,99,2]) == sorted([5,19,4,1,36,99,2])
assert bubble_sort(["Greg", "Armen", "Ken"]) == sorted(["Greg", "Armen", "Ken"])