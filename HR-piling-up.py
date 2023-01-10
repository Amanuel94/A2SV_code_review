# Enter your code here. Read input from STDIN. Print output to STDOUT


def stack(blocks):
    size=len(blocks)
    
    #Assume the first block has infinite length
    #So that any block can be on top of it
    top_block = float('inf')
    
    
    left, right = 0, size -1
    
    while left <= right:
        if blocks[left]>blocks[right] and blocks[left]<=top_block:
            top_block = blocks[left] 
            left+=1
        elif blocks[right]>=blocks[left] and blocks[right]<=top_block:
            top_block = blocks[right]
            right-=1
        else:
            break
            
    if right < left:
        return 'Yes'
    else:
        return 'No'
    
for T in range(int(input())):
    size =  int(input())
    blocks = list(map(int, input().split()))
    print(stack(blocks))
