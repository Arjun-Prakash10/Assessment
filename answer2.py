def validator(s):
    if not s[0].isupper():
        return False
    if s[1:].isupper():
        return False
    if s[-1] not in ['.' , '?' , '!']:
        return False
    for i in range(len(s)):
        if s[i]=='-':
            if s[i-1]!=' ' or s[i+1]!=' ' or s[i-2]==' ' or s[i+2]==' ':
                return False
    return s

def reducer(a):
    
    a = a[:-1]
    
    words = a.split()
    dedup = []
    for i in words:
        if (i not in dedup or i=='-'):
            dedup.append(i)
    a = ' '.join(dedup)
    
    word_groups = []
    prev=0
    for i in range(len(a)):
         if a[i]=='-':
                word_groups.append(a[prev:i].strip())
                prev=i+1
    word_groups.append(a[prev:len(a)].strip())
    
    reduced_str = ''
    for i in word_groups:
        if not (i.strip()):
            continue
        else:
            reduced_str = reduced_str + ' ' +i 
        
    return reduced_str.strip()

def check_and_clean(s):
    if validator(s):
        return reducer(s)
    return "invalid"

string = input()
print(check_and_clean(string))