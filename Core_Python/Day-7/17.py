# nested elif

print('Welcome to Gaming Zone')
print()
l1 = ['nfs','hp','a','b']
print('Select your game code : ',l1)
print()
game = input('Enter user game : ')

if game == 'nfs':
    pass
elif game == 'hp':
    print('Welcome to Harrp Potter Session')
    l1 = ['stage1','stage2','stage3']
    print('Game selection code: ',l1)
    print()
    game2 = input('Enter user game selection : ')
    print()
    if game2 == 'stage1':
        print('Welcome to Sate-1')
    elif game2 == 'stage2':
        print('Welcome to Sate-2')
    elif game2 == 'stage3':
        print('Welcome to Sate-3')
    else:
        print('Selected option is not valid.')
elif game == 'a':
    pass
elif game == 'b':
    pass
else:
    print('Game is not in stock')




