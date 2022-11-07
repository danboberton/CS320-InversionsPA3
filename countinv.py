from sys import argv, exit

# provided
#
# Read integers from the given filename.
#
# Return value: list of integers
def read_array(filename):
    try:
        with open(filename) as f:
            return [int(n) for n in f.read().split()]
    except:
        exit("Couldn’t read numbers from file \""+filename+"\"")


# implement
#
# Return the number of inversions in the given list, by doing a merge
# sort and counting the inversions.
#
# Return value: number of inversions
def count_inversions(in_list):
    listLen = len(in_list)
    if listLen > 2:
        # Might not be even number
        half = int(listLen / 2)
        split1 = in_list[0:half]
        split2 = in_list[half:listLen]
        resultL = count_inversions(split1)
        resultR = count_inversions(split2)
        result = merge_i(split1, split2, in_list)
    else:
        result = bubbleWithCount(in_list)

    return result




# implement
#
# Merge the left & right lists into in_list.  in_list already contains
# values--replace those with the merged values.
#
# Return value: inversion count
def merge_i(l_list, r_list, in_list):
    result = 0
    in_list.clear()
    while len(l_list) !=0 and len(r_list) !=0:
        if l_list[0] < r_list[0]:
            result += len(l_list)
            in_list.append(r_list.pop())
        else:
            in_list.append(l_list.pop())

        if len(l_list) == 0:
            in_list.extend(r_list)
            r_list.clear()
        if len(r_list) == 0:
            in_list.extend(l_list)
            l_list.clear()

    return result

def bubbleWithCount(in_list):
    swaps = 0
    lenList = len(in_list)
    for i in range(lenList - 1):
        for j in range( lenList - i - 1):
            if in_list[j] > in_list[j+1]:
                in_list[j], in_list[j+1] = in_list[j+1], in_list[j]
                swaps += 1

        if swaps == 0:
            return 0

    return swaps


# provided
if __name__ == '__main__':
    if len(argv) != 2:
        exit("usage: python3 "+argv[0]+" datafile")
    in_list = read_array(argv[1])
    print(count_inversions(in_list))
    # Added
    print(in_list)