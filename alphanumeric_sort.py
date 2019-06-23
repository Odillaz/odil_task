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
        
        # numbers
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

# unit tests
# assert (alphan_sort('A11a4')) == '411aA'
# assert (alphan_sort('BASv2s5w46z00')) == '02546asvzBAS'
# assert (alphan_sort('aBcDeFG264598')) == '264598aceBDFG'
# assert (alphan_sort('abcdef')) == 'abcdef'
# assert (alphan_sort('ABCDEF')) == 'ABCDEF'
