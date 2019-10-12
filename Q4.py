def ProcessArray():
    ClassContact=open("ClassContact.txt","w")
    ClassContact.close()
    ClassList = open('ClassList.txt', 'r')
    for Name in ClassList.readlines():
        Info = SearchFile(Name.strip())
        Num = AddToFile(Info, Name.strip())
    return len(ClassList.readlines()) - Num
def SearchFile(Name):
    StudentContact = open('StudentContact.txt', 'r')
    for Line in StudentContact.readlines():
        if Line[:len(Name)] == Name:
            StudentContact.close()
            return Line
    StudentContact.close()
    return ''
def AddToFile(Info, Name):
    Num = 0
    ClassContact = open('ClassContact.txt','w')
    if Info == '':
        Num += 1
        ClassContact.write(Name + '*No Number')
    else:
        ClassContact.write(Info)
    ClassContact.close()
    return Num


print("Students with no number: " + str(ProcessArray()))
