def ascii_tree(height):
    # loop for each level of tree

    for i in range(height):
        # leading spaces for centering
        spaces = " " * (height - i - 1)
        #print(spaces)
        
        #numbers of leaves for current level of height
        leafs = "^" * (2* i + 1)
        print(spaces + leafs + spaces)
    # drawing center trunk 
    trunk_spaces = " " * (height - 1)
    print(trunk_spaces + "[]" + trunk_spaces)
    print(trunk_spaces + "[]" + trunk_spaces)
    print(trunk_spaces + "[]" + trunk_spaces)
   



#draw function 

ascii_tree(4)