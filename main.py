letter = "abcdefghijklmnopqrstuvwxy"
operator = "+-/*"

def read():
    global ch
    global i
    try:
        ch = word[i]
        i = i + 1
        if i == len(word):
            print("FINISH OK! " + str(i))
    except IndexError:
        print("FINISH OK! " + str(i))


def readBack():
    global ch
    global i
    i = i - 1
    ch = word[i]


def error(text):
    print("Ошибка! " + text)


def checkLetter():
    if ch in letter:
        pass
    else:
        error("Letter " + str(i))


def checkOperator():
    if ch in operator:
        pass
    else:
        error("Operator " + str(i))

def checkPSZ():
    read()
    if ch in operator:
        readBack()
    elif (ch == "{") or (ch == "[") or (ch == "("):
        checkSV()
    else:
        error("PSZ " + str(i))

def checkBAV():
    checkLetter()
    read()
    checkOperatorAndBAV()

def checkOperatorAndBAV():
    read()
    if ch in operator:
        checkOperator()
        read()
        checkBAV()
    elif ch in letter:
        readBack()
    else:
        error("OperatorAndBAV " + str(i))

def checkSV():
    if ch == "(":
        checkSVkr()
        read()
        checkOperatorSV()
    elif ch == "[":
        checkSVkv()
        read()
        checkOperatorSV()
    elif ch == "{":
        checkSVfig()
        read()
        checkOperatorSV()
    else:
        error("SV " + str(i))

def checkSVkr():
    if ch == "(":
        checkBAV()
        read()
        if ch == ")":
            readBack()
        else:
            error("SVkr " + str(i))
    else:
        error("SVkr " + str(i))

def checkSVkv():
    if ch == "[":
        checkSVkvkr()
        read()
        if ch == "]":
            readBack()
        else:
            error("SVkv " + str(i))
    else:
        error("SVkv " + str(i))

def checkSVkvkr():
    if ch == "(":
        checkSVkr()
        read()
        checkOperatorSVkvkr()
    else:
        error("SVkvkr " + str(i))

def checkOperatorSVkvkr():
    read()
    if ch in operator:
        checkOperator()
        read()
        checkSVkvkr()
    elif ch == "]":
        readBack()
    else:
        error("OperatorSVkvkr " + str(i))

def checkSVfig():
    if ch == "{":
        checkSVfigkvorkr()
        read()
        if ch == "}":
            readBack()
        else:
            error("SVfig " + str(i))
    else:
        error("SVfig " + str(i))

def checkSVfigkvorkr():
    if ch == "(":
        checkSVkr()
        read()
        checkOperatorSVfigkvorkr()
    elif ch == "[":
        checkSVkv()
        read()
        checkOperatorSVfigkvorkr()
    else:
        error("SVfigkvorkr " + str(i))

def checkOperatorSVfigkvorkr():
    read()
    if ch in operator:
        checkOperator()
        read()
        checkSVfigkvorkr()
    elif ch in "], )":
        readBack()
    else:
        error("OperatorSVfigkvorkr " + str(i))

def checkOperatorSVfigkvorkr():
    read()
    if ch in operator:
        checkOperator()
        read()
        checkSVfigkvorkr()
    elif ch in "], )":
        readBack()
    else:
        error("OperatorSVfigkvorkr " + str(i))

def checkOperatorSV():
    read()
    if ch in operator:
        checkOperator()
        read()
        checkSV()
    elif ch in "], ), }":
        readBack()
    else:
        error("OperatorSV " + str(i))

# word = "{a+b}+{b+c}"
# print(word)
print("Правильная скобочная запись арифметических выражений с тремя видами скобок.\nВнутри фигурных скобок обязательно должны быть квадратные, но могут быть\nкруглые, внутри квадратных должны быть круглые или бесскобочные выражения,\nвнутри круглых только бесскобочные арифметические выражения. Также, если один из\nоперандов является скобкой, то и второй должен быть скобкой (не может быть буквой).\nМогут быть “лишние” скобки, но одна буква не может браться в скобки.")
while True:
    print("Введите пример:")
    word = input()
    i = 0
    checkPSZ()

