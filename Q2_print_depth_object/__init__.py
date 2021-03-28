from collections import deque

class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


def print_depth(data):
    """
        The complexity of this solution is
        Time: O(N), where N is the total number of key present in the nested dictionary and total member variables present.
        We are visiting those key only once.

        Space: O(N^2), here we are creating new dictionary each time.
        In worst case if the input is nested one after another ex:{'a':{'b':'c':{'d':1}}} then we n,n-1,n-2 dictionary are created,
        which equals to n*(n-1)/2, means O(N^2)

        :param data: nested dictionary
        :return:
        """
    if not data:
        print("Empty Data Passed")
        return

    # Que to traverse in BFS
    que = deque([(data, 1)])

    while que:
        # get the top element
        current_data, current_level = que.popleft()

        # If this is an user defined class object this will contain __dict__ attribute for other primitive type it won't
        if hasattr(current_data, '__dict__'):
            # Getting the members of the object as key value pair dictionary
            object_members = vars(current_data)

            for key in object_members.keys():
                print(f"{key}: {current_level}") # print with a : as this is object key

                # If this object contains another object we add it to the que
                if hasattr(object_members[key], '__dict__'):
                    que.append((object_members[key], current_level+1))

        # Else if this is a Dictionary
        elif type(current_data) is dict:
            for key in current_data.keys():

                # If the dictionary contains an object we add it and increase its depth
                if hasattr(current_data[key], '__dict__'):
                    print(f"{key}: {current_level}") # print with a : if this is a object key
                    que.append((current_data[key], current_level+1))

                # If the dictionary contains a nested dictionary we add it and increase its depth
                elif type(current_data[key]) is dict:
                    print(f"{key} {current_level}")
                    que.append((current_data[key], current_level+1))

                else:
                    print(f"{key} {current_level}")


