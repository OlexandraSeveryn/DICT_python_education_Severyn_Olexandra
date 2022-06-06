print('Special commands: !help !done')
print('-' * 29)

formatts = 'Available formatters: plain, bold, italic, header, link, inline-code,' \
           ' ordered-list, unordered-list, new-line.'
formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line']
choose = 0
m_down = []


def available_formatters():
    if choose == formatters[0]:         # plain
        users_text = input('Text: ')
        m_down.append(users_text)
        print(f'{users_text}')

    elif choose == formatters[1]:       # bold
        users_text = input('Text: ')
        m_down.append(users_text)
        print(f'**{users_text}**')

    elif choose == formatters[2]:       # italic
        users_text = input('Text: ')
        m_down.append(users_text)
        print(f'*{users_text}*')

    elif choose == formatters[4]:       # link
        label = input('Label: ')
        url = input('URL: ')
        m_down.append(f'''[{label}] ({url})''')
        print(f'''[{label}] ({url})''')

    elif choose == formatters[5]:       # inline-code
        users_text = input('Text: ')
        m_down.append(users_text)
        print()

    elif choose == formatters[8]:       # new-line
        users_text = input('Text: ')
        m_down.append(users_text)
        print()

    elif choose == formatters[3]:       # header
        lvl = int(input('Level: '))
        try:
            if lvl not in range(1, 7):
                print('The level should be within the range of 1 to 6. Try again!')
            else:
                users_text = input('Text: ')
                m_down.append(users_text)
                print(f'{lvl * "#"} {users_text}')
        except ValueError:
            print('The level should be within the range of 1 to 6. Try again!')

    # ordered and unordered lists

    elif choose == formatters[6]:       # ordered-list
        num_of_rows = int(input('Number of rows:'))
        try:
            if num_of_rows > 0:
                for n in range(1, num_of_rows + 1):
                    users_text = input(f'Row #{n}:')
                    m_down.append(users_text)
                    print(f'#{users_text}')
        except ValueError:
            print('The number of rows should be greater than zero.')

    elif choose == formatters[7]:       # unordered-list
        num_of_rows = int(input('Number of rows:'))
        try:
            if num_of_rows > 0:
                for n in range(1, num_of_rows + 1):
                    users_text = input(f'Row #{n}:')
                    m_down.append(users_text)
                    print(f'*{users_text}')
        except ValueError:
            print('The number of rows should be greater than zero.')


while choose != 'done':
    choose = input('Choose a formatter:')
    if choose == 'help':
        print(formatts)
    elif choose == 'done':
        break
    else:
        available_formatters()


if choose == 'done':
    saving = open('output.md', "w")
    saving.write(f'''{''.join(m_down)}''')
