blocks = int(input("Enter the number of blocks: "))
h = 0
layer = 1

while blocks >= layer:
    blocks -= layer
    h += 1
    layer += 1
    
print("The height of the pyramid:", h)
    
