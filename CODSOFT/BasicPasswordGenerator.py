import random
alpha=['A','B','C','D','E','F','G','H','I''J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n=['1','2','3','4','5','6','7','8','9','0']
special=['!','@','#','$','%','&','^','*','(',')','-','+','_']

n_alpha=int(input("how many letters would you like in your password "))
s_symbols=int(input("how many special symbols would you like:"))
n_numbers=int(input("how many number would you like "))
password=""


# for alphabets
for i in range(1,n_alpha+1):
    ele=random.choice(alpha)
    password +=ele

# for number
for i in range(1,n_numbers+1):
    ele=random.choice(n)
    password +=ele

# for special characters
for i in range(s_symbols+1):
    ele=random.choice(special)
    password +=ele

print("password is :",password)

print(len(password))