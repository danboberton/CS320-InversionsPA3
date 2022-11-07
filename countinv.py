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
        result = merge_i(split1, split2, in_list)
    elif (listLen == 1):
        return 0
    elif listLen == 2:
        if in_list[0] > in_list[1]:
            temp = in_list[0]
            in_list[0] = in_list[1]
            in_list[1] = temp
            return 1

    return result




# implement
#
# Merge the left & right lists into in_list.  in_list already contains
# values--replace those with the merged values.
#
# Return value: inversion count
def merge_i(l_list, r_list, in_list):
    result = count_inversions(l_list) + count_inversions(r_list)
    in_list.clear()


    in_list.extend(l_list)
    in_list.extend(r_list)
    result += bubbleWithCount(in_list)
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