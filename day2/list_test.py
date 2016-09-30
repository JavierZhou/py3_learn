#!/usr/bin/env python3

users = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
users.insert(3, 'x')
users.insert(3, 'xx')
print(users)
print(users[3:6])
users.remove(users[6])
print(users)
