# with open('writelines.txt', 'w') as f:
#     lines = ['line1\n', 'line2\n', 'line3']
#     f.writelines(lines)

# adding new line character using loop

with open('writelines.txt', 'w') as f:
    lines = ['line1', 'line2', 'line3']
    for i in lines:
        f.writelines(i+'\n')
