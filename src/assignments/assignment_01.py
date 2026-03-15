marks = [78, 85, 62, 90, 55, 88]
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)
print("\nHighest:", highest)
print("\nLowest:", lowest)
print("\nAverage:", average)

print("\nDistinction:")
for mark in marks:
    if mark >= 75:
        print(mark)

# Add new mark
marks.append(95)
print("\nAfter Adding 95:", marks)

# Remove a mark
marks.remove(55)
print("\nAfter Removing 55:", marks)

# Sort marks 
marks.sort()
print("\nSorted Marks:", marks)

# Reverse marks 
marks.reverse()
print("\nReversed Marks:", marks)