# mydict1={'a':1,'b':3,'c':5}
# mydict2={'a':5,'b':2,'c':4}
# def mergeValue(dict1, dict2):
#     merge = dict1.copy()
#     merge.update(dict2)
#     return merge
# print(mergeValue(mydict1, mydict2))



# def merge_sum(dict1, dict2):
#     merged = dict1.copy()
#     for key, value in dict2.items():
#         if key in merged:
#             merged[key] += value
#         else:
#             merged[key] = value
#     return merged
# a = {'x': 1, 'y': 2}
# b = {'y': 3, 'z': 4}
# print(merge_sum(a, b))

def sum_of_digits(n):
    # Step 1: Convert the number to a string
    n_str = str(n)
    
    # Step 2: Loop through each character (digit)
    total = 0
    for i in n_str:
        total += int(i)  # Convert back to int and add to total
    
    # Step 3: Return the total sum
    return total

# Example usage:
print(sum_of_digits(12345))  # Output: 15
