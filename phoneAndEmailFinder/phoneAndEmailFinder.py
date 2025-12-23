import re, pyperclip

phoneRegex = re.compile(r'''
    (\+?\d{1,3}[-.\s]?)?      # country code
    (\(?\d{3}\)?[-.\s]?)     # area code
    (\d{3})([-.\s]?\d{2})([-.\s]?\d{2})
''', re.VERBOSE)

emailRegex = re.compile(r'''
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    \.[a-zA-Z]{2,}
''', re.VERBOSE)

text = pyperclip.paste()

matches = []

for match in phoneRegex.findall(text):
    matches.append(''.join(match).strip())

for match in emailRegex.findall(text):
    matches.append(match)

if matches:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
