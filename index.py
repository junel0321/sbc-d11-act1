alpha = ["Q", "S", "A", "M", "Z", "R"]
str = len(alpha)
for i in range(str):
    print(f"Pass {i+1}")
    for j in range(0, str-i-1):
        print(f"Comparing {alpha[j]} and {alpha[j+1]}")
        if alpha[j] > alpha[j+1]:
            alpha[j], alpha[j+1] = alpha[j+1], alpha[j]
            
            print(f"Swapped: {alpha}")
        else:
            print(f"No swapping needed")
        print(f"List after the pass {i+1}: {alpha}")
print(f"Final sorted list {alpha}")