print('Special commands: !help !done')
formatts = 'Available formatters: plain, bold, italic, header, link, inline-code,' \
           ' ordered-list, unordered-list, new-line.'
formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line']
choose = 0


while choose != 'done':
    choose = input('Choose a formatter:')
    if choose == 'help':
        print(formatts)
    elif choose == 'done':
        break
    else:
        print()
