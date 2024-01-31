import csv
import string
import json

def deleteListFromDict(listName,sortDict):
    for key in listName:
        if(sortDict.get(key)):
            sortDict.pop(key)

def deleteFindName(inputFromUser, index):
    targetName = inputFromUser.split()[index+1]
    targetName = targetName.replace("’", '')
    targetName = targetName.replace("‘", '')
    for character in string.punctuation:
        targetName = targetName.replace(character, '')
    listName = []
    if (inputFromUser.split()[index] == "="):
        for key in sortdict:
            if (sortdict.get(key).get('name') == targetName):
                listName.append(key)

    elif (inputFromUser.split()[index] == "!="):
        for key in sortdict:
            if (sortdict.get(key).get('name') != targetName):
                listName.append(key)
    return listName

def deleteFindLastName(inputFromUser,index):
    targetName = inputFromUser.split()[index+1]
    targetName = targetName.replace("’", '')
    targetName = targetName.replace("‘", '')
    for character in string.punctuation:
        targetName = targetName.replace(character, '')
    listName=[]
    if (inputFromUser.split()[index] == "="):
        for key in sortdict:
            if (sortdict.get(key).get('last name') == targetName):
                listName.append(key)
    elif (inputFromUser.split()[index] == "!="):
        for key in sortdict:
            if (sortdict.get(key).get('last name') != targetName):
                listName.append(key)
    return listName

def deleteFindGrade(inputFromUser,index):
    grade = inputFromUser.split()[index+1]
    grade = grade.replace("’", '')
    grade = grade.replace("‘", '')
    for character in string.punctuation:
        grade = grade.replace(character, '')
    grade = int(grade)
    listName=[]
    if (inputFromUser.split()[index] == "="):

        for key in sortdict:
            if (int(sortdict.get(key).get('grade')) == grade):
                listName.append(key)

    elif (inputFromUser.split()[index] == "!="):
        for key in sortdict:
            if (int(sortdict.get(key).get('grade')) != grade):
                listName.append(key)


    elif (inputFromUser.split()[index] == "<") or inputFromUser.split()[index] == "!>":
        for key in sortdict:
            if (int(sortdict.get(key).get('grade')) < grade):
                listName.append(key)

    elif (inputFromUser.split()[index] == ">") or inputFromUser.split()[index] == "!<":
        for key in sortdict:
            if (int(sortdict.get(key).get('grade')) > grade):
                listName.append(key)
    elif (inputFromUser.split()[index] == "<="):
        for key in sortdict:
            if (int(sortdict.get(key).get('grade')) <= grade):
                listName.append(key)
    elif (inputFromUser.split()[index] == ">="):
        for key in sortdict:
            if (int(sortdict.get(key).get('grade')) >= grade):
                listName.append(key)
    return listName

def deleteFindId(inputFromUser,index):
    id = inputFromUser.split()[index+1]
    id = id.replace("’", '')
    id = id.replace("‘", '')
    for character in string.punctuation:
        id = id.replace(character, '')
    id = int(id)
    listName=[]
    if (inputFromUser.split()[index] == "="):
        listName.append(id)

    elif (inputFromUser.split()[index] == "!="):
        for key in sortdict:
            if(int(key)!=id):
                listName.append(key)

    elif (inputFromUser.split()[index] == "<") or inputFromUser.split()[index] == "!>":
        for key in sortdict:
            if (int(key) < id):
                listName.append(key)
    elif (inputFromUser.split()[index] == ">") or inputFromUser.split()[index] == "!<":
        for key in sortdict:
            if (int(key) > id):
                listName.append(key)

    elif (inputFromUser.split()[index] == "<="):
        for key in sortdict:
            if (int(key) <= id):
                listName.append(key)

    elif (inputFromUser.split()[index] == ">="):
        for key in sortdict:
            if (int(key) >= id):
                listName.append(key)
    return listName

def deleteFindEmail(inputFromUser,index):
    targetEmail = inputFromUser.split()[index+1]
    targetEmail = targetEmail.replace("’", '')
    targetEmail = targetEmail.replace("‘", '')
    targetEmail = targetEmail.replace("'", '')
    targetEmail = targetEmail.replace("'", '')
    targetEmail = targetEmail.replace("\"", '')
    listName=[]
    if (inputFromUser.split()[index] == "="):
        for key in sortdict:
            if (sortdict.get(key).get('email') == targetEmail):
                listName.append(key)

    elif (inputFromUser.split()[index] == "!="):
        for key in sortdict:
            if (sortdict.get(key).get('email') != targetEmail):
                listName.append(key)
    return listName

def checkCondition(val1,val2,cond):
    if cond==">"  and val1>val2:
        return True
    elif  (cond=="=>" or cond=="!<") and val1>=val2:
        return True
    elif cond=="<"  and val1<val2:
        return True
    elif  (cond=="<=" or cond=="!>") and val1<=val2:
        return True
    elif  cond=="="  and val1==val2:
        return True
    return False
Dict = {}
with open('students.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names: {", ".join(row)}')
            line_count += 1
            print()
        else:

            Dict[int(row[0])]={'name': row[1], 'lastname': row[2], 'email': row[3], 'grade': row[4]}
            line_count += 1
    print()



sortdict = {}

for key in sorted(Dict.keys()):
    sortdict[key] = Dict[key]
inputFromUser = input("Enter a sql command or exit:")
while inputFromUser.lower() != "exit":
    if inputFromUser.split()[0] == "SELECT":
        selected = {}
        for key in sortdict:
            x = sortdict[key]
            conjunction = inputFromUser.split()[8]  # and / or

            if inputFromUser.split()[5] == "grade" :
                first_value_to_compare = int(inputFromUser.split()[7])
                first_value_at_hand = int(x[inputFromUser.split()[5]])
            elif inputFromUser.split()[5] == "id":
                first_value_to_compare = int(inputFromUser.split()[7])
                first_value_at_hand = key
            else:
                first_value_to_compare = inputFromUser.split()[7]
                first_value_to_compare = first_value_to_compare.replace('‘', '')
                first_value_to_compare = first_value_to_compare.replace('’', '')
                first_value_to_compare = first_value_to_compare.replace("'", "")
                first_value_at_hand = x[inputFromUser.split()[5]]
            if len(inputFromUser.split())!=11:
                if inputFromUser.split()[9] == "grade" :
                    second_value_to_compare = int(inputFromUser.split()[11])
                    second_value_at_hand = int(x[inputFromUser.split()[9]])
                elif inputFromUser.split()[9] == "id":
                    second_value_to_compare = int(inputFromUser.split()[11])
                    second_value_at_hand = key
                else:
                    second_value_to_compare = inputFromUser.split()[11]
                    second_value_to_compare = second_value_to_compare.replace('‘', '')
                    second_value_to_compare = second_value_to_compare.replace('’', '')
                    second_value_to_compare = second_value_to_compare.replace("'", "")
                    second_value_at_hand = x[inputFromUser.split()[9]]

            #                    0      1   2       3       4     5  6  7  8    9  10   11    12  13  14
            # inputFromUser = "SELECT name FROM STUDENTS WHERE grade > 40 AND name = ‘John’ ORDER BY DSC"
            con1 = checkCondition(first_value_at_hand, first_value_to_compare, inputFromUser.split()[6])
            if len(inputFromUser.split())==11:
                con2=True
            else :
                con2 = checkCondition(second_value_at_hand, second_value_to_compare, inputFromUser.split()[10])
            # Dict[int(row[0])] = {'name': row[1], 'last name': row[2], 'email': row[3], 'grade': row[4]}
            addDict = False


            if len(inputFromUser.split())==11:
                addDict = con1
            else :
                if inputFromUser.split()[8] == "AND" and (con1 and con2):
                    addDict = True
                elif inputFromUser.split()[8] == "OR" and (con1 or con2):
                    addDict = True

            if addDict:

                if inputFromUser.split()[1].lower() == "all":
                    selected[key] = x
                else:
                    a = inputFromUser.split()[1]
                    values = {}
                    for i in a.split(","):
                        if i=="id":
                            values["id"]=key
                        else:
                            values[i] = x[i]

                    selected[key] = values

        ordered_selected = {}

        if len(inputFromUser.split()) == 11:
            if inputFromUser.split()[10] == "DSC":
                for key in sorted(selected.keys(), reverse=True):
                    ordered_selected[key] = selected[key]

            else:
                ordered_selected = selected
        else:

            if inputFromUser.split()[14] == "DSC":
                for key in sorted(selected.keys(), reverse=True):
                    ordered_selected[key] = selected[key]

            else:
                ordered_selected = selected

        print("selected and sorted")
        print(ordered_selected)
    elif inputFromUser.split()[0] == "INSERT":
        if inputFromUser.split()[1] == "INTO" and inputFromUser.split()[2] == "STUDENT" and inputFromUser.split()[3].split("(")[0]=="VALUES":
            values=inputFromUser.split()[3].split("(")[1].split(",")
            if len(values) == 5:
                values[4]= values[4].replace(")", "")
                if sortdict.get(int(values[0])):
                    print("This id has been taken")
                else:
                    Dict[int(values[0])]={'name': values[1], 'last name': values[2], 'email': values[3], 'grade': values[4]}
                    sortdict[values[0]] = Dict[int(values[0])]
            else:
                print("Wrong values")
        else:
            print("Wrong input")
    elif inputFromUser.split()[0] == "DELETE":
        if inputFromUser.split()[1] == "FROM" and inputFromUser.split()[2] == "STUDENT" and inputFromUser.split()[3] == "WHERE":
            strAndOr=""
            listOfWords = []
            for key in range(4,len(inputFromUser.split())):
                listOfWords.append(inputFromUser.split()[key])
            listName = []
            while len(listOfWords) != 0:
                firstKey=listOfWords.pop(0)
                if (firstKey == "name"):
                    str1 = ""
                    for words in listOfWords:
                        str1 += words+" "
                    if(strAndOr=="or" or strAndOr==""):
                        listName += deleteFindName(str1, 0)
                    elif(strAndOr=="and"):
                        listNew = deleteFindName(str1, 0)
                        listName = set(listName) & set(listNew)
                    listOfWords.pop(0)
                    listOfWords.pop(0)
                elif (firstKey == "grade"):
                    str1 = ""
                    for words in listOfWords:
                        str1 += words + " "
                    if (strAndOr == "or" or strAndOr == ""):
                        listName += deleteFindGrade(str1, 0)

                    elif (strAndOr == "and"):
                        listNew = deleteFindGrade(str1, 0)
                        listName = set(listName) & set(listNew)
                    listOfWords.pop(0)
                    listOfWords.pop(0)
                elif (firstKey == "id"):
                    str1 = ""
                    for words in listOfWords:
                        str1 += words + " "
                    if (strAndOr == "or" or strAndOr == ""):
                        listName += deleteFindId(str1, 0)
                    elif (strAndOr == "and"):
                        listNew = deleteFindId(str1, 0)
                        listName = set(listName) & set(listNew)
                    listOfWords.pop(0)
                    listOfWords.pop(0)

                elif (firstKey == "email"):

                    str1 = ""
                    for words in listOfWords:
                        str1 += words + " "
                    if (strAndOr == "or" or strAndOr == ""):
                        listName += deleteFindEmail(str1, 0)
                    elif (strAndOr == "and"):
                        listNew = deleteFindEmail(str1, 0)
                        listName = set(listName) & set(listNew)
                    listOfWords.pop(0)
                    listOfWords.pop(0)

                elif firstKey == "last" and listOfWords[0]=="name":
                    str1 = ""
                    for words in listOfWords:
                        str1 += words + " "
                    if (strAndOr == "or" or strAndOr == ""):
                        listName += deleteFindLastName(str1,1)
                    elif (strAndOr == "and"):
                        listNew = deleteFindLastName(str1,1)
                        listName = set(listName) & set(listNew)

                    listOfWords.pop(0)
                    listOfWords.pop(0)
                    listOfWords.pop(0)
                if(len(listOfWords)!=0):
                    strAndOr=listOfWords.pop(0).lower()
            deleteListFromDict(listName,sortdict)

        else:
            print("Wrong input")
    else:
        print("Wrong input")
    inputFromUser = input("Enter a sql command or exit:")
with open("sample.json", "w") as outfile:
    json.dump(sortdict, outfile, indent=2)






