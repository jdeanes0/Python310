n = 10
total = 0

for i in range(1,n+1):
    # print(i)
    total += pow(i,2)

print(f"sigma: \t{total}")
print(f"n^3: \t{pow(n,3)}")
print(f"n^2: \t{pow(n,2)}")

def most_possible_visits(n):
    count = 0

    for i in range(1,n+1):
        count += i

    # The most possible visits will be ...something
    # print(f"Most possible to know if one has reached their max: {count - (n-2)}")
    print(f"Most visits possible: {count}")

most_possible_visits(5)

def swap(i: int,j: int,list: list):
    tmp = list[i]
    list[i] = list[j]
    list[j] = tmp

def selection_sort(list: list):
    # outer - check every value
    for i in range(len(list)):
        #inner - find the largest element
        largest = list[i]
        for j in range(0,len(list)-1):
            if list[i] < list[j]:
                swap(i,j,list)
    
    for e in list:
        print(e)


selection_sort([3, 50, 77, 7536, 10, 11, 12, 88])