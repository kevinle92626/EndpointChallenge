
import sys
from my_dict import My_Dict

# Use Hashmap (dict of dicts) to store the directory structures
class Directories:
    def __init__(self, name='/'):
        self._root = My_Dict()    # Create an empty list of dictionary (tuple) to store directory structures

    # Add new directory to the list and return the newly add directory
    def _add_directory(self, parent_dir: My_Dict, child_dir) -> My_Dict:
        full_path = child_dir.split("/")    # Parse (split) the new_dir to see if it's to be added to root or sub-root
        if len(full_path) == 1:   # Add directory to wherever we are at now
            return parent_dir.append(child_dir)
        else:                     # Add to sub-root
            # Traverse & create parent directories if needed before we create the child directory
            current_dir = parent_dir
            for idx in range(len(full_path) - 1):
                if full_path[idx] not in current_dir.keys():
                    current_dir = self._add_directory(current_dir, full_path[idx])
                else:    # already exist, go to next sub-directory
                    current_dir = current_dir.get_dir_by_name(full_path[idx])
            # Now add child directory
            current_dir = self._add_directory(current_dir, full_path[-1])

    def _sort_directories(self, directories: My_Dict):
        directories.sort()
        for parent_dir, child_dir in directories.items():
            self._sort_directories(My_Dict(child_dir))

    def _extract_path(self, data, from_dir, already_ran=False):
        # If the current element is a string, return it as a list
        if isinstance(data, str):
            return [data]
        # If the current element is a tuple, recursively extract strings from its second element
        elif isinstance(data, tuple):
            result = [data[0]]  # Get the first element (the string) from the tuple
            for item in data[1]:  # Traverse the second element (which is a list)
                if item[0] == from_dir or already_ran:
                    result.extend(self._extract_path(item, from_dir, already_ran=True))  # Recursively extract from the nested list or tuple
            return result
        return []

    def get_root(self):
        return self._root

    def create(self, parent_dir: My_Dict, child_dir: str, verbose=True):
        """
        Create a directory.

        Parameters:
        parent_dir (My_Dict): The parent directory of the child
        child_dir (str): The directory to be created

        Returns:
        None
        """
        self._add_directory(parent_dir, child_dir)
        if verbose:
            print(f"{self.create.__name__.upper()} {child_dir}")

    def delete(self, child_dir: str, verbose=True):
        """
        Delete a directory. Note: we will only delete if it's empty. (Not specified in requirements)

        Parameters:
        child_dir (str): The directory to be deleted

        Returns:
        None
        """
        if verbose:
            print(f"{self.delete.__name__.upper()} {child_dir}")
        full_path = child_dir.split('/')
        current_dir = self.get_root()    # we know input path will always start with root
        for idx in range(len(full_path) - 1):  # every parent nodes must exist before child can be deleted
            if full_path[idx] in current_dir.keys():
                current_dir= current_dir.get_dir_by_name(full_path[idx])
            else:    # parent doesn't exist`
                if verbose:
                    print(f"Cannot delete {child_dir} - {full_path[idx]} does not exist")
        current_dir.delete(full_path[len(full_path)-1])

    def list(self, directories: My_Dict, indent=0, first_time=True):
        if first_time:
            print(f"{self.list.__name__.upper()}")
            self._sort_directories(directories)
            first_time = False
        for dir, sub_dir in directories.items():
            print(f"{' ' * indent}{dir}")
            self.list(My_Dict(sub_dir), indent + 2, first_time)

    def move(self, from_dir, to_dir):
        from_dir_node = self._get_dir_by_path(self.get_root(), from_dir)
        to_dir_node = self._get_dir_by_path(self.get_root(), to_dir)
        temp = [to_dir_node, from_dir_node]
        new_dir_path = (temp[0][0], temp[0][1])
        for t in temp[1:]:
            new_dir_path = (new_dir_path[0], new_dir_path[1] + [t])
        dir_name = from_dir.split('/')[-1]
        new_dir_path_str = '/'.join(self._extract_path(new_dir_path, dir_name, already_ran=False))
        self.delete(from_dir, verbose=False)
        self.create(self.get_root(), new_dir_path_str, verbose=False)
        print(f"{self.move.__name__.upper()} {from_dir} {to_dir}")

    # Get a directory obj from a given path. This function will return the directory with exact match
    # from the given entire path.
    def _get_dir_by_path(self, parent_dir: My_Dict, full_dir_name: str) -> My_Dict:
        full_path = full_dir_name.split('/')
        if len(full_path) == 1:    # The directory we are looking for is at this level
            if parent_dir.contains(full_path[0]):
                return parent_dir.get_node_by_name(full_path[0])
            else:
                return None
        else:
            # Traverse & create parent directories if needed before we create the child directory
            current_dir = parent_dir
            for idx in range(len(full_path) - 1):
                if full_path[idx] in current_dir.keys():
                    current_dir = current_dir.get_dir_by_name(full_path[idx])
                    return self._get_dir_by_path(current_dir, "/".join(full_path[idx+1:]))
                else:
                    return None

def process_command(input: str):
    dir = Directories()
    commands = input.split()
    if commands[0].upper() == "CREATE":
        dir.create(dir.get_root(), commands[1])
    elif commands[0].upper() == "LIST":
        dir.list(dir.get_root(), indent=0)
    elif commands[0].upper() == "MOVE":
        dir.move(commands[1], commands[2])
    elif commands[0].upper() == "DELETE":
        dir.delete(commands[1], verbose=True)
    else:
        print(f"Command '{commands[0]}' not recognized.")

def get_user_input():
    return input().split()

def main(input_file=None, output_file=None, write_to_output=False):
    out = open(output_file, "w")
    if write_to_output:
        sys.stdout = out
    if input_file:
        with open(input_file, "r") as file:
            inputs = file.readlines()
            for command in inputs:
                process_command(command)
    else:
        command = get_user_input()
        while command[0].upper() != "EXIT":
            command_str = " ".join(command)
            process_command(command_str)
            command = get_user_input()
    if write_to_output:
        sys.stdout = sys.__stdout__
    out.close()

if __name__ == "__main__":
    main(input_file="input.txt", output_file="output.txt", write_to_output=False)
