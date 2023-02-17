import time

fhand = open('mbox-short.txt')
emails = []
for line in fhand:
    if line.startswith('From:'):
        line = line.strip()
        line = line.split()
        email = line[-1]
        if email not in emails:
            emails.append(email)

result = ''
for email in emails:
    result += email +'\n'
print(result)
fhand.close()
file = open('Email List.txt', 'w')
file.write(result)
file.close
