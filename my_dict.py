class My_Dict:
    def __init__(self, dir=[]):
        self.data = dir    # Use list to store the dictionary key-value pairs

    # Append item to dictionary. If key already exist, then update value.  Otherwise, add new key-value to dictionary
    # Note: the item is a tuple with key = [0], and value = [1] (key is the directory and value is a list of sub-dir
    def append(self, key, value=[]):    # return the directory just created
        update_flag = False
        for i in range(len(self.data)):
            if self.data[i][0] == key:
                self.data[i] = (key, value)    # Update the value if key already exists
                update_flag = True
                return My_Dict(self.data[i][1])
        if not update_flag:
            self.data.append((key, []))         # Key doesn't exist, add a new key-value pair
        return My_Dict(self.data[-1][1])    # return the directory of the last item added

    # Delete item from dictionary
    def delete(self, key):
        for i in range(len(self.data)):
            if self.data[i][0] == key:    # delete even if not empty
                del self.data[i]
                return

    # See if a key exists in the dictionary
    def contains(self, key):
        for item in self.data:
            if item[0] == key:
                return True
        return False

    # Get a directory obj by directory name (key). This function will return the nearest directory obj with
    # the given directory name..
    def get_dir_by_name(self, dir_name):
        for i in range(len(self.data)):
            if self.data[i][0] == dir_name:
                return My_Dict(self.data[i][1])
        raise(KeyError, "Key not found.")

    # Get the directory node. This function will return the tuple of the matching directory and not a directory
    def get_node_by_name(self, node_name) -> ():
        for i in range(len(self.data)):
            if self.data[i][0] == node_name:
                return self.data[i]
        raise(KeyError, "Key not found.")

    # Get all key-value pairs (iterator)
    def items(self):
        return self.data

    # Get all keys (iterator)
    def keys(self):
        return (item[0] for item in self.data)

    # Get all values (iterator)
    def values(self):
        return (item[1] for item in self.data)

    # Sort the dictionary by key in alphabetical order
    def sort(self):
        self.data.sort()

    def depth(self):
        return len(self.data)

    # display the dictionary
    def display(self):
        return self.data
