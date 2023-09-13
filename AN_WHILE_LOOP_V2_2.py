while True:
    name = input('\nPlease enter your name: ')
    if name == 'Tom':
        print('\n\tYour access request has been GRANTED, ' + name + '!\n')
    else:
        print('\n\tYour access request has been DENIED, ' + name + '!\n')
    break