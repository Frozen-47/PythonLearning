i = [1,2,3,23,1,8,3]



def merge_sort(i):
    if len(i) <= 1:
        return i
    mid = len(i) // 2
    left_half = merge_sort(i[:mid])



