
# 초성

FIRST = [ 
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 
    'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

#중성 (모음)

MIDDLE = [ 
    'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', ['ㅗ', 'ㅏ'], ['ㅗ', 'ㅐ'],
    ['ㅗ', 'ㅣ'], 'ㅛ', 'ㅜ', ['ㅜ','ㅓ'], ['ㅜ','ㅔ'], ['ㅜ','ㅣ'],
    'ㅠ', 'ㅡ', ['ㅡ', 'ㅣ'], 'ㅣ'
]

# 종성

LAST = [
    '', 'ㄱ', 'ㄲ', ['ㄱ','ㅅ'], 'ㄴ', ['ㄴ','ㅈ'], ['ㄴ', 'ㅎ'], 'ㄷ', 'ㄹ', ['ㄹ', 'ㄱ'], ['ㄹ','ㅁ'], ['ㄹ','ㅂ'], ['ㄹ','ㅅ'], ['ㄹ','ㅌ'], ['ㄹ','ㅍ'], ['ㄹ','ㅎ'], 'ㅁ',
    'ㅂ', ['ㅂ','ㅅ'], 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

# 한글 시작 유니코드
OFFSET = 0xac00

# 자음

JA = [
    'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ',
    'ㅁ', 'ㅂ', 'ㅃ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

# 완성된 초성
COMP_FIRST = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ',
    'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

# 완성된 중성
COMP_MIDDLE = [
    'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ',
    'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'
]

# 완성된 종성
COMP_LAST = [
    ' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ',
    'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

# 합쳐지는 자음들
COMPLEX_JA = [
    ['ㄱ','ㅅ','ㄳ'],
    ['ㄴ','ㅈ','ㄵ'],
    ['ㄴ','ㅎ','ㄶ'],
    ['ㄹ','ㄱ','ㄺ'],
    ['ㄹ','ㅁ','ㄻ'],
    ['ㄹ','ㅂ','ㄼ'],
    ['ㄹ','ㅅ','ㄽ'],
    ['ㄹ','ㅌ','ㄾ'],
    ['ㄹ','ㅍ','ㄿ'],
    ['ㄹ','ㅎ','ㅀ'],
    ['ㅂ','ㅅ','ㅄ']
]

# 합쳐지는 모음들
COMPLEX_MO = [
    ['ㅗ','ㅏ','ㅘ'],
    ['ㅗ','ㅐ','ㅙ'],
    ['ㅗ','ㅣ','ㅚ'],
    ['ㅜ','ㅓ','ㅝ'],
    ['ㅜ','ㅔ','ㅞ'],
    ['ㅜ','ㅣ','ㅟ'],
    ['ㅡ','ㅣ','ㅢ']
]

def _makeDict(array):
    _dict = {}
    for i, v in enumerate(array):
        if array[i]:
            _dict[ord(array[i])] = i
    return _dict

JA_HASH = _makeDict(JA)
FIRST_HASH = _makeDict(COMP_FIRST)
MIDDLE_HASH = _makeDict(COMP_MIDDLE)
LAST_HASH = _makeDict(COMP_LAST)

def _makeComplexDict(array):
    _dict = dict(dict())
    for i, v in enumerate(array):
        code1 = ord(array[i][0])
        code2 = ord(array[i][1])
        if code1 not in _dict.keys():
            _dict[code1] = {}
        _dict[code1][code2] = ord(array[i][2])
    return _dict

COMPLEX_JA_HASH = _makeComplexDict(COMPLEX_JA)
COMPLEX_MO_HASH = _makeComplexDict(COMPLEX_MO)

def is_JA(c):
    return c in JA_HASH

def is_First(c):
    return c in FIRST_HASH

def is_Middle(c):
    return c in MIDDLE_HASH

def is_Last(c):
    return c in LAST_HASH

def is_Korean(cn):
    return 0xac00 <= cn and cn <= 0xd7a3

def is_Middle_Joinable(a, b):
    if (a in COMPLEX_MO_HASH and b in COMPLEX_MO_HASH[a]) : 
        return COMPLEX_MO_HASH[a][b]
    else:
        return False

def is_Last_Joinable(a, b):
    if a in COMPLEX_JA_HASH and b in COMPLEX_JA_HASH[a]:
        return COMPLEX_JA_HASH[a][b]  
    else: 
        return False

def merge(string):
    mode = 0
    prev_code = 0
    result = []
    comp_idx = -1
    korean = ''
    middle1 = 0
    _first = 0
    middle2 = 0
    last1 = 0
    last2 = 0

    def createKorean(idx):
        nonlocal comp_idx
        nonlocal _first
        nonlocal middle1
        nonlocal middle2
        nonlocal last1
        nonlocal last2
        nonlocal result
        if comp_idx + 1 > idx:
            return
        
        step = 1
        while(True):
            
            if step == 1:
                _first = ord(string[comp_idx + step])
                if is_Middle(_first): # 차음이 모음이면 ㅏ or ㅙ 같은 경우
                    middle1 = ord(string[comp_idx + step + 1])
                    if comp_idx + step + 1 <= idx and is_Middle(middle1): # 다음 있고 다음도 모음이면
                        result.append(chr(is_Middle_Joinable(_first, middle1)))
                        comp_idx = idx
                        return
                    else:
                        result.append(string[comp_idx + step])
                        comp_idx = idx
                        return
                elif not is_First(_first):
                    result.append(string[comp_idx + step])
                    comp_idx = idx
                    return
                korean = string[comp_idx + step]
            if step == 2:
                middle1 = ord(string[comp_idx + step])
                if is_First(middle1): # 두번째 또 자음이면 ㄱㅅ 에서 ㅅ
                    _first = is_Last_Joinable(_first, middle1)
                    korean = chr(_first)
                    result.append(korean)
                    comp_idx = idx
                    return
                else:
                    #print(_first, middle1)
                    korean = chr((FIRST_HASH[_first] * 21 + MIDDLE_HASH[middle1]) * 28 + OFFSET)
            elif step == 3:
                middle2 = ord(string[comp_idx + step])
                if is_Middle_Joinable(middle1, middle2):
                    middle1 = is_Middle_Joinable(middle1, middle2)
                else:
                    last1 = middle2
                korean = chr((FIRST_HASH[_first] * 21 + MIDDLE_HASH[middle1]) * 28 + (0 if last1 == 0 else LAST_HASH[last1]) + OFFSET)
            elif step == 4:
                last2 = ord(string[comp_idx + step])
                if is_Last_Joinable(last1, last2):
                    last1 = is_Last_Joinable(last1, last2)
                else:
                    last1 = last2
                korean = chr((FIRST_HASH[_first] * 21 + MIDDLE_HASH[middle1]) * 28 + (0 if last1 == 0 else LAST_HASH[last1]) + OFFSET)
            elif step == 5:
                last2 = ord(string[comp_idx + step])
                last1 = is_Last_Joinable(last1, last2)
                korean = chr((FIRST_HASH[_first] * 21 + MIDDLE_HASH[middle1]) * 28 + (0 if last1 == 0 else LAST_HASH[last1]) + OFFSET)

            if comp_idx + step >= idx:
                result.append(korean)
                comp_idx = idx
                return

            step += 1

    for i, char in enumerate(string):

        code = ord(char)

        if not is_First(code) and not is_Middle(code) and not is_Last(code):
            createKorean(i-1)
            createKorean(i)
            mode = 0
            continue
        
        if mode == 0: # 초성 차례
            if is_First(code): # 초성이라면 문제 없음
                mode = 1
            elif is_Middle(code): # 중성이 오면 ㅐ ㅘ, 바로 구분을 못해서 나중에 처리
                mode = 4
        elif mode == 1: # 중성 차례
            if is_Middle(code): # 중성이라면 문제 없음
                mode = 2
            else: # 자음이 왔다면 합쳐지거나 안합쳐지는 경우가 있으니..
                if is_Last_Joinable(prev_code, code):
                    # 합쳐질 수 있다면 ㄻ 같은 경우인데 이 뒤에 모음이 와서 ㄹ마 가 될수도 있고 초성이 올 수도 있다. 따라서 섣불리 완성할 수 없으니 나중에 처리
                    mode = 5
                else: # 합쳐질 수 없다면 앞 글자 완성 후 중성 체크
                    createKorean(i-1)
        elif mode == 2: # 종성 차례
            if is_Last(code): # 종성 다음엔 자음 or 모음
                mode = 3
            elif is_Middle(code): # 종성이 아닌 중성이 왔다면 앞 모음과 합칠 수 있는지 확인
                if not is_Middle_Joinable(prev_code, code): # 합칠 수 없다면 오타
                    createKorean(i -1)
                    mode = 4
                # 합쳐진다면 그대로
            else: # 받침이 안되는 자음이라면 쌍자음 같은 애들로 만들고 다시
                createKorean(i-1)
                mode = 1
        elif mode == 3 : # 종성이 하나 온 상태.
            if is_Last(code) : # 또 종성이면 합칠수 있는지 본다.
                if not is_Last_Joinable(prev_code, code): #없으면 한글자 완성
                    createKorean(i-1)
                    mode = 1; # 이 종성이 초성이 되고 중성부터 시작
                #합칠 수 있으면 계속 진행. 왜냐하면 이번에 온 자음이 다음 글자의 초성이 될 수도 있기 때문
            elif is_First(code): # 초성이면 한글자 완성.
                createKorean(i-1)
                mode = 1 # 이 글자가 초성이되므로 중성부터 시작
            elif is_Middle(code): # 중성이면 이전 종성은 이 중성과 합쳐지고 앞 글자는 받침이 없다.
                createKorean(i-2)
                mode = 2
        elif mode == 4: # 중성이 하나 온 상태
            if is_Middle(code): # 중성이 온 경우
                if is_Middle_Joinable(prev_code, code): # 이전 중성과 합쳐질 수 있는 경우
                    createKorean(i)
                    mode = 0
                else: #//중성이 왔지만 못합치는 경우. ㅒㅗ 같은
                    createKorean(i-1)
            else: # 아니면 자음이 온 경우.
                createKorean(i-1);
                mode = 1
        elif mode == 5: # 초성이 연속해서 두개 온 상태 ㄺ
            if is_Middle(code): # 이번에 중성이면 ㄹ가
                createKorean(i-2)
                mode = 2
            else:
                createKorean(i-1)
                mode = 1
        prev_code = code
    createKorean(i-1)
    print(result)
    return "".join(result)


# 한글 딕셔너리
twobulsik = {
    "~": "~", "!": "!", "@": "@", "#": "#", "$": "$", "%": "%", "^": "^", "&": "&", "*": "*", "(": "(", ")": ")", "_": "_", "+": "+", 
	"`": "`", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "0": "0", "-": "-", "=": "=",
	"Q": "ㅃ", "W": "ㅉ", "E": "ㄸ", "R": "ㄲ", "T": "ㅆ", "Y": "ㅛ", "U": "ㅕ", "I": "ㅑ", "O": "ㅒ", "P": "ㅖ", "{": "{", "}": "}", "|": "|", 
	"q": "ㅂ", "w": "ㅈ", "e": "ㄷ", "r": "ㄱ", "t": "ㅅ", "y": "ㅛ", "u": "ㅕ", "i": "ㅑ", "o": "ㅐ", "p": "ㅔ", "[": "[", "]": "]", "\\": "\\",
	"A": "ㅁ", "S": "ㄴ", "D": "ㅇ", "F": "ㄹ", "G": "ㅎ", "H": "ㅗ", "J": "ㅓ", "K": "ㅏ", "L": "ㅣ", ":": ":", "\"": "\"", 
	"a": "ㅁ", "s": "ㄴ", "d": "ㅇ", "f": "ㄹ", "g": "ㅎ", "h": "ㅗ", "j": "ㅓ", "k": "ㅏ", "l": "ㅣ", ";": ";", "'": "'",
	"Z": "ㅋ", "X": "ㅌ", "C": "ㅊ", "V": "ㅍ", "B": "ㅠ", "N": "ㅜ", "M": "ㅡ", "<": "<", ">": ">", "?": "?",
	"z": "ㅋ", "x": "ㅌ", "c": "ㅊ", "v": "ㅍ", "b": "ㅠ", "n": "ㅜ", "m": "ㅡ", ",": ",", ".": ".", "/": "/",
    " ": " "
}

mode = None

while mode != 'q':
    print("도와줘요! 한글이 안쳐져요!")
    print("영어로 입력하면 한글로 바꿔줍니다!")

    eng = input("영어로 입력하세요 : ")
    
    kor = []
    for char in eng:
        kor.append(twobulsik[char])
    
    #print(kor)

    print("{result}".format(result=merge(kor)))

    mode = input("다시? (q를 누르면 나갑니다.): ")
