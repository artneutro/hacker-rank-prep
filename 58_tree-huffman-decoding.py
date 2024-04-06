# https://www.hackerrank.com/challenges/tree-huffman-decoding/problem

import queue as Queue

cntr = 0

class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1
        
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count

def huffman_hidden():#builds the tree and returns root
    q = Queue.PriorityQueue()

    
    for key in freq:
        q.put((freq[key], key, Node(freq[key], key) ))
    
    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0' )
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj ))
        
    root = q.get()
    root = root[2]#contains root object
    return root

def dfs_hidden(obj, already):
    if(obj == None):
        return
    elif(obj.data != '\0'):
        code_hidden[obj.data] = already
        
    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

def check_next(s, root, i, decoded_string) :
    # If the root is a leave, append the data
    if ((root.left == None) and (root.right == None)) :
        decoded_string.append(root.data)
    # If not, check the left or the right increasing the index
    elif s[i] == '0' :
        i = check_next(s, root.left, i+1, decoded_string)
    elif s[i] == '1' :
        i = check_next(s, root.right, i+1, decoded_string)
    # Return the index to continue the next iteration from the same 
    return i
        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
	#Enter Your Code Here
    # Variable to store the solution
    decoded_string = []
    # Pointer to the current index in string
    i = 0
    # Go through all the string and check the next character 
    while (i < len(s)) :
        i = check_next(s, root, i, decoded_string)
    # Print the solution got on the list
    to_print = ''
    for j in decoded_string :
        to_print += j
    print(to_print)

ip = input()
freq = {}#maps each character to its frequency

cntr = 0

for ch in ip:
    if(freq.get(ch) == None):
        freq[ch] = 1
    else:
        freq[ch]+=1

root = huffman_hidden()#contains root of huffman tree

code_hidden = {}#contains code for each object

dfs_hidden(root, "")

if len(code_hidden) == 1:#if there is only one character in the i/p
    for key in code_hidden:
        code_hidden[key] = "0"

toBeDecoded = ""

for ch in ip:
   toBeDecoded += code_hidden[ch]

decodeHuff(root, toBeDecoded)

