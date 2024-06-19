#  calculate the median of  the  list after merging to 2 list
def median(list1,list2):
    list1= sorted(list1 + list2)
    length= len(list1)
    if length % 2 !=0:
        return list1[length//2]
    else :
        return (list1[(length//2)-1]+ list1[length//2])//2
    
# main function
list1=[2, 3, 5, 8]
list2=[10, 12, 14, 16, 18, 20]
print(median(list1,list2))