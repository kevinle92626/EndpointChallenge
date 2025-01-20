Just pull all 3 files (directory.py, my_dict.py, and input.txt) into the same folder and run directory.py.
The result will be output to stdout or change the input parameter on the last line of directory.py to True
(eg., 

main(input_file="input.txt", output_file="output.txt", write_to_output=True)

and it will redirect all stdout to the output.txt file.

Note: I was not sure which helper libraries I can use so I did not use any.  I implemented my own
data structure similar to dictionary/hashmap to store the directories.  The directories are store in a list 
of tuples consisting of a key (directory name) and a list of all its sub-directory.  I also use recursive
throughout the codes to keep it simple and within the couple hours duration as suggested.  Of course,
recursive has its own drawbacks such as memory consumption, possible stack overflow, and harder to debug
but I did the best I could with what I have.  Thank you for giving me an opportunity to cramp all those
codes in a few hours.
