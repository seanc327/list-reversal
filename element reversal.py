def reverse_elems(input_list):
    reversed_list = []
    # for loop will yield a linear runtime, O(n)
    for i in input_list:
        reversed_list = [i] + reversed_list
        # returns reversed_list
    return reversed_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print(reverse_elems(my_list))  # expected: [5, 4, 3, 2, 1]

