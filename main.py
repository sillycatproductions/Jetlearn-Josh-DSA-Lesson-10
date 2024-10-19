# main code start --------------------------------------------------------------------------------------:P

class Tree(): #tree class
    def __init__(self,a):
        self.data = a #middle
        self.left = None #left
        self.right = None #right

def inorder(root): #method of searching tree (left, middle, right) or (left, data, right) as it is binary search
    if root != None: #if root exists
        if root.left != None: #if left exists
            inorder(root.left) #search left
        print(root.data) #search middle
        if root.right != None: #if right exists
            inorder(root.right) #search right

def insert(root, b): #to add the values in (line 43)
    if root == None: #if root does not exist
        return Tree(b) #return value (b)
    if root.data > b: #if middle is bigger than value
        root.left = insert(root.left,b) #insert value into left
    else: #if middle is smaller than value or equal to value
        root.right = insert(root.right,b) #insert value to right
    return root #return all values

def search(root, c): #searching for the value (line 48)
    if root.data == c: #if middle = search value
        return root #return all values
    elif root.data > c and root.left != None: #if middle bigger than search value and left exists
        return search(root.left, c) #return the search value
    elif root.data < c and root.right != None: #if middle is smaller than search value and right exists
        return search(root.right, c) #return search value
    else: 
        return -1 #otherwise return the value as -1
    
# main code end --------------------------------------------------------------------------------------:P

# input start ---------------------------------------------------------------------------------------:P

count = int(input('How many elements will be in the tree? ')) #user writes how many elements will be in the tree
root = None #make root not exist
for i in range(count): #loop for the amount of elements in tree
    val = int(input('Enter value: ')) #user writes the value
    root = insert(root, val) #makes the root the value

inorder(root) #line 9 - line 15

sear = int(input('What number do you want to search? ')) #makes search value
key = search(root, sear) #makes key

if key == -1: #if key = -1 (line 34)
    print('Key', sear,'does not exist.') #prints that the key the user is seraching for does not exist
else:
    print('Key', sear,'exists!') #otherwise prints that the key the user is looking for exists

#code end -------------------------------------------------------------------------------------------:P