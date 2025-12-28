def number_pattern(n):
    i_string = ''
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    else:
        for i in range(n):
            i_string += str(i + 1) + ' '
            final_string = i_string.strip()
        return final_string
            

print(f'MY result: {number_pattern(4)}')
print(f'C result: {repr(number_pattern(4))}')
print(f'My result: {number_pattern(12)}')
print(f'C result: {repr(number_pattern(12))}')


