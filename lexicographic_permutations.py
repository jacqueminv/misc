'''
Sharpen your saw

Lexicographic permutations guarentees that your permutation follows a sorted
order. In other words, the sequence of permutations would the same as in a
dictionary.

Example

The Lexicographic permutations for the set {1,2,3,4} results as:

{1,2,3,4} {2,1,3,4} {3,1,2,4} {4,1,2,3}
{1,2,4,3} {2,1,4,3} {3,1,4,2} {4,1,3,2}
{1,3,2,4} {2,3,1,4} {3,2,1,4} {4,2,1,3}
{1,3,4,2} {2,3,4,1} {3,2,4,1} {4,2,3,1}
{1,4,2,3} {2,4,1,3} {3,4,1,2} {4,3,1,2}
{1,4,3,2} {2,4,3,1} {3,4,2,1} {4,3,2,1}

'''

def swap(items, i, j):
    items[i], items[j] = items[j], items[i]
    return items

def move_to_left(items):
    for i in range(1, len(items)):
        if items[i] > items[0]:
            return swap(items, i, 0)

def leftward(items, i, j):
    return items[:j] + [items[i]] + items[j:i]

def rightward(items, i, j):
    return items[:j] + items[i:] + items[j:i]

def permute_subset(items):
    permutations = []
    end = len(items) - 1
    i = end
    while i != 1:
        swapped = False
        for j in range(i-1, 0, -1):
            if items[i] > items[j]:
                if i-j > 2 and items[i-1] > items[j+1]:
                    break
                if i == end:
                    items = leftward(items, i, j)
                    for x in range(j+1,i):
                        if items[x] > items[x+1]:
                            items = swap(items, x, x+1)
                else:
                    items = rightward(items, i, j)
                permutations += [items]
                swapped = True
                break
        if swapped is False:
            i = i - 1
        else:
            i = end
            swapped = False
    return permutations

def permute(items):
    permutations = []
    for i in range(len(items)):
        permutations += [items[:]]
        permutations += permute_subset(items)
        items = move_to_left(items)
    return permutations

p = permute([1,2,3,4,5])
for _ in p:
    print _
