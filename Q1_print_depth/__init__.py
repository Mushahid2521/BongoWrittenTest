from collections import deque

def print_depth(data):
    """
    The complexity of this solution is
    Time: O(N), where N is the total number of key present in the nested dictionary.
    We are visiting those key only once.

    Space: O(N^2), here we are creating new dictionary each time.
    In worst case if the input is nested one after another ex:{'a':{'b':'c':{'d':1}}} then we n,n-1,n-2 dictionary are created,
    which equals to n*(n-1)/2, means O(N^2)

    :param data: nested dictionary
    :return:
    """
    # if dict is empty
    if not data:
        print("Empty Dictionary Passed")
        return

    que = deque([(data, 1)])

    # Breadth First Search to get level increasingly
    while que:
        # getting the top value
        current_dictionary, current_level = deque.popleft(que)
        for key in current_dictionary.keys():
            print(f"{key} {current_level}")

            # If the value is a dictionary then we append it
            if type(current_dictionary[key]) is dict:
                que.append((current_dictionary[key], current_level+1))

