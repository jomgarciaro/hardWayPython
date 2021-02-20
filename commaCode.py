def comma(lists):
    string = ''
    for i in range(0, len(lists) - 1):
        string = string + str(lists[i]) + ', '
    string = string + ' and ' + str(lists[len(lists) - 1])
    print(string)

spam = ['apples', 'bananas' , 42, 'cats']
comma(spam)
