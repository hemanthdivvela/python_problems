#Remove Duplicates from a List

def dup(lst):
    empty = []
    duplicates =[]
    for i in range(len(lst)):
        if lst[i] in empty:
            empty.append(lst[i])
        """else:
            duplicates.append(lst[i])"""
    print("original list",lst)        
    print("in list correct values:",empty)
    '''print("in list duplicate values:",duplicates)'''
    '''return empty'''


lst = [1,2,1,2,3]
dup(lst)

