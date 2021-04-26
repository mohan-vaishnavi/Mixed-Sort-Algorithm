from datetime import datetime
import random


def bubble(arr):
    s = c = 0
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
    # Last i elements are already in place
        for j in range(0, n - i - 1):
            c += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                s += 1
    return arr, c, s


def insertion(l):
    length = len(l)
    c = s = 0
    for i in range(1, length):
        j = i;
        c+=1;
        while (j > 0) and (l[j - 1] > l[j]):
            if l[j-1]>l[j]:
                c+=1
        temp = l[j - 1]
        l[j - 1] = l[j]
        l[j] = temp
        j-=1
        s+=1
    return l, c, s



def mixed(inp):
    print("\nMixed sort:\n")
    c = m = ins = 0
    l = len(inp)

    inp[0:l // 2],c1,s1 = bubble(inp[0:l // 2])
    inp[l // 2:l],c2,s2 = bubble(inp[l // 2:l])
    for j in range(l // 2 + 1, l, 2):
        key1, key2 = inp[j - 1], inp[j]
        i = j - 2
        while i > 0 and inp[i] > key2:
            c += 1 
            inp[i + 2] = inp[i]
            m += 1 
            i -= 1
        if inp[i] < key2:
            c += 1 
            inp[i + 2] = key2
            m += 1 
            ins += 1
            if inp[i] < key1:
                inp[i + 1] = key1
                ins += 1 
                c += 1 
                m += 1 

            else:
                c += 1
                while i != -1 and inp[i] > key1:
                    inp[i + 1] = inp[i]
                    i -= 1
                    c += 1 # tracking comparison
                    m += 1 # tracking movement
                c += 1
                inp[i + 1] = key1
                ins += 1 # tracking insertion

        else:
            c += 1
            inp[i:i + 3] = key1, key2, inp[i]
            ins += 2 # tracking insertion
            m += 3
    print(f"Comparisons: {c+c1+c2} \nMovements: {m+s1+s2} \nInsertions: {ins}\n")
    return inp


input_dataset = random.sample(range(10,100000),1000)
input_dataset1 = input_dataset
input_dataset2 = input_dataset

start_b = datetime.now()
b_sorted, comp, swap = bubble(input_dataset)
end_b = datetime.now()

start_i = datetime.now()
i_sorted, comps, swaps = insertion(input_dataset1)
end_i = datetime.now()

start = datetime.now()
mix_sorted = mixed(input_dataset2)
end = datetime.now()


print(f"time(ms): {(end-start)}")
print("------------------------------------")
print("Bubble sort:\n")
print(f"Comparisons: {comp} \nSwaps: {swap}\n")
print(f"time(ms): {-(start_b-end_b)}")
print("------------------------------------")
print("Insertion sort:\n")
print(f"Comparisons: {comps} \nSwaps: {swaps}\n")
print(f"time(ms): {end_i-start_i}\n")

if mix_sorted == b_sorted:
    print('The list has been successfully sorted')
    



    

