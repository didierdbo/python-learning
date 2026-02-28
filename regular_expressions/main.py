import re
string = 'search this inside of this text please!'
print('search' in string)

pattern = re.compile('search this inside')
a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(d)


regex = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"

email = "my.ownsite@our-earth.org"
print(f"{email}: ", "Valid Email" if re.fullmatch(regex, email) else "Invalid Email")

email = "abc36.com"
print(f"{email}: ", "Valid Email" if re.fullmatch(regex, email) else "Invalid Email")

password = "a2c4e6g@"
regex = r"[A-Za-z0-9.$%#@]{8,}"
print(f"{password}: ", "Valid Password" if re.fullmatch(regex, password) else "Invalid Password")

