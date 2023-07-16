############################### STRING ################################

a = "Hello, World!"

# accessing and slicing
print(a[7])
print(a[2:5])
print(a[:5])
print(a[-11:-1])

# accessing with for loop
for i in a:
    print(i)

# len() = finding length of string
print(len(a))

# present or not
# in\not in
txt = "The best things in life are free!"
print('free' in txt)

if 'free' in txt:
    print('yes, \"free\" is present ')

print( 'boss' not in txt )

if 'boss' not in txt:
    print('no, \'boss\' not present')
else:
    print('yes, \'boss\' exists')

# upper() = making string in to uppercase
print(txt.upper())

# lower() = making string in to lowercase
print(txt.lower())

# stripe() = removing white space
aj = ' akmal ali '
print(aj.strip())

# replace() = replace a character with other 
print(aj.replace('k','j'))

# split() = splitting a string in to list of substring
print(aj.split(' '))

b = 'Hellow'
c = 'World'
print(b+' '+c)

# format()
aj_name = 'ajmal {}'
age = 22
print(aj_name.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {1} pieces of item {0} for {2} dollars."
print(myorder.format(quantity,itemno,price))

# escape character
print("i am \'mohammed\' sabeel")
print("i am 'mohammed' sabeel")


# capitalize() = convert the first character in to capital
mun = 'mUNAVAR'
print(mun.capitalize())

# casefold() = convert the strings in to lower case
print(mun.casefold())

# center() = used to center string by taking space specified inside center
chunk = mun.center(20)
print(len(chunk),chunk)

# count() = it return the number of specified strings
print(mun.count('m'))

# endswith() = it return the True if the string ends with specified character in the endswith()
print(mun.endswith('R'))

# expandtabs() = to increase tab size
print(mun.expandtabs())

# find() = find the starting index of specified item in the string,return -1 if the value not found
print(mun.find('NAVAR'))

# index() = find the starting index of specified item in the string ,it will raise an exception if value not found
print(mun.index('AVAR'))


# isalnum() = it return true if all characters in the string is alpha numeric
print(mun.isalnum())

# isalpha() = it return true if all characters in the string are alphabet
print(mun.isalpha())

lo = '101'
# isdecimal() = it return true if all characters in the string are decimal
print(lo.isdecimal())

# isdigit() = it return true if all characters in the string are digits
print(lo.isdigit())

# isdigit() = it return true if all characters in the string have white space
print(mun.isspace())


# removing all vowels in the strings

str = input('Enter the string :')

vowels_srtings = 'aeiouAEIOU'

for i in str:
    if i  in vowels_srtings:
        str = str.replace(i,'')

print('result after removing vowels :',str)

#removing all  characters in the string except vowels 

str = input('Enter the string :')

vowels_srtings = 'aeiouAEIOU'

for i in str:
    if i  not in vowels_srtings:
        str = str.replace(i,'')

print(' vowels in the string are:',str)


def removing_vowels(str):
    vowel_string = 'aeiouAEIOU'
    for i in str:
        if i in vowel_string:
            str = str.replace(i,'')

    
    print('result after removing voewls are :',str)
    return

removing_vowels('sabeel')


def finding_vowels(str):
    vowel_string = 'aeiouAEIOU'
    for i in str:
        if i not in vowel_string:
            str = str.replace(i,'')

    
    print('vowels are :',str)
    return

finding_vowels('sabeel')



# finding maximum lengthed word in the string


str = input('enter the the string you want :')

s=str.split()
max = 0
max_word = ''
for i in s:
    if len(i) > max:
        max = len(i)
        max_word = i

print('maximun length word is \'{}\' '.format(max_word),'and its length is {}.'.format(max)) 


def maximum_lengthed_word(str):
    s = str.split()
    max = 0
    max_word = ''
    for i in s:
        if len(i) > max:
            max = len(i)
            max_word = i
    
    print("maximum lengthed word is '{}' ".format(max_word),"and its length is {} ".format(max))
    return

maximum_lengthed_word('hellow welocome to python pogramming language')



# finding minimum lengthed word in the string

def maximum_lengthed_word(str):
    s = str.split()
    min = len(s[0])
    min_word = ''
    for i in s:
        if len(i) < min:
            min = len(i)
            min_word = i
    
    print("minimum lengthed word is '{}' ".format(min_word),"and its length is {} ".format(min))
    return

maximum_lengthed_word('hellow welocome to python pogramming language')
          
# reversing string
a = 'Hellow world'
print(a[::-1])


# palindrome workout

str = input('enter the string you want to check palindrome :')
if str == str[::-1]:
    print(str,'is palindrome')
else:
    print(str,'is not palindrome')


def palindrom_check(str):
    if str == str[::-1]:
        print(str,'is palindrome')
    else:
        print(str,'is not palindrome')

    return

palindrom_check('sabeel')



str = input('enter the string you want :')
rev_str = ''
for i in str:
    rev_str = i + rev_str

if str == rev_str:
    print(str,'is a palindrome')
else:
    print(str,'is not palindrome')



# palindrome logic

num = input('enter anything you want :')
pal = True
for i in range(len(num)//2):
    if num[i] != num[len(num)-i-1]:
       pal = False

if pal == True:
    print('its palindrome')
else:
    print('not palindrome')


# reverse logic

str1 = 'Hellow world'

rev_str = ''

for i in str1:
    rev_str = i + rev_str  
    
print(rev_str)


# Replaces each alphabet in a given string with another alphabet occurring at the n-th position from each of them.
def replace_with_nth_char(string,n):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    replaced_string = ''
    for i in string:
        if i in alphabet:
            is_lower = i.islower()
            i = i.lower()
            replaced_i = alphabet[(alphabet.index(i) + n)%26]
            if is_lower:
                replaced_string += replaced_i
            else:
                replaced_string += replaced_i.upper()
        else:
            replaced_string += i
    
    return replaced_string

print(replace_with_nth_char('helloo',1))


# add a word between splited word

str = 'Hello world'
s=str.split()
print(s)
result = ' hoi '.join(s)
print(result)

def split_and_add(str,add):
    s = str.split()
    new = ' '+add+' '
    result = new.join(s)
    print(result)
    return

split_and_add('hello world','hoi')


# reverse string

str1 = 'Hellow world'
new = list(str1)
print(new)

for i in range(len(new)//2):
    new[i],new[len(new)-i-1] = new[len(new)-i-1],new[i]

reversed_string = ''.join(new)
print(reversed_string)




################################# END STRING ###########################