def alphan_sort(val):  
    """ sort by numbers, lower case,then upper case characters """  
    numbers =[]
    lowercase =[]
    uppercase =[]
    sorted_list = []

    for char in val:
        # lowercase characters
        if (char.islower()):
            lowercase.append(char)
        
        # numbers, exception case not handled
        if (char.isnumeric()):
            numbers.append(char)

        # upper cases
        if (char.isupper()):
            uppercase.append(char) 

    # create sorted list 
    sorted_list.extend(sorted(numbers))
    sorted_list.extend(sorted(lowercase))
    sorted_list.extend(sorted(uppercase))
    return "".join(sorted_list)

print (alphan_sort('A11a4'))

# unit tests, because exception case is not handled
assert (alphan_sort('A11a4')) == '114aA'
assert (alphan_sort('BASv2s5w46z00')) == '02456asvzBAS'
assert (alphan_sort('aBcDeFG264598')) == '245689aceBDFG'
assert (alphan_sort('abcdef')) == 'abcdef'
assert (alphan_sort('ABCDEF')) == 'ABCDEF'
