def reverse_string(str):
    stack = []
    for i in str:
        stack.append(i)

    reverse = ''
    while stack:
        reverse += stack.pop()
    
    print(reverse)

reverse_string('sabeel')