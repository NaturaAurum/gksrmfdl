FIRST = 0x001 #초성
MIDDLE = 0x010 #중성
LAST = 0x100 #종성


def chain(*iters):
    """
    반복가능한 오브젝를 받아서 합쳐진 chain 오브젝트로 변환
    """
    for it in iters:
        for element in it:
            yield element


"""
한글 초성, 중성, 종성 들을
chr 내장 함수와 map을 이용해 리스트로 만들어주고
딕셔너리에 넣어준다.
"""
char_dict = {
    FIRST : list(map(chr, [
        0x3131, 0x3132, 0x3134, 0x3137, 0x3138, 0x3139,
        0x3141, 0x3142, 0x3143, 0x3145, 0x3146, 0x3147,
        0x3148, 0x3149, 0x314a, 0x314b, 0x314c, 0x314d,
        0x314e
    ])),
    MIDDLE : list(map(chr, [
        0x314f, 0x3150, 0x3151, 0x3152, 0x3153, 0x3154,
        0x3155, 0x3156, 0x3157, 0x3158, 0x3159, 0x315a,
        0x315b, 0x315c, 0x315d, 0x315e, 0x315f, 0x3160,
        0x3161, 0x3162, 0x3163
    ])),
    LAST : list(map(chr, [
        0x3131, 0x3132, 0x3133, 0x3134, 0x3135, 0x3136,
        0x3137, 0x3139, 0x313a, 0x313b, 0x313c, 0x313d,
        0x313e, 0x313f, 0x3140, 0x3141, 0x3142, 0x3144,
        0x3145, 0x3146, 0x3147, 0x3148, 0x314a, 0x314b,
        0x314c, 0x314d, 0x314e
    ])) # 종성의 0번째는 공백이지만, 종성이 없는건 판단해서 안넣어주면 되니까 포함시키지 않아도 무관
}

# 초성은 초성index * 588 (중성 count * 종성 count 즉, 21 * 28 = 588)
# 중성은 중성index * 28 (종성 count)
# 종성은 종성 index 그대로
# 한글의 유니코드 시작은 44032 -> 0xac00
# 즉 한글은 음절은 0xac00 + (588 * 초성index) + (28 * 중성index) + (종성index) 으로 이루어짐

SETS = { key : set(value) for key, value in char_dict.items()} # 각 딕셔너리 요소에서 중복을 없앤 집합
SET = set(chain(*SETS.values())) # 모든 한글을 합쳐서 중복을 없앤 집합

INDICES = {key : {char : index for index, char in enumerate(value)} for key, value in char_dict.items()} # 한글 index 정리

def is_korean_syllable(kc) : # 한글 음절이 맞는지
    return 0xac00 <= ord(kc) <= 0xd7a3

def is_korean_compatibility_jamo(kc): #호환 체크 
    return 0x3130 <= ord(kc) <= 0x318f

def is_supported_korean(kc): # 지원되는 한글인지
    return is_korean_syllable(kc) or is_korean_compatibility_jamo(kc)

def check(kc, jamo_only = False):
    if not ((jamo_only or is_korean_compatibility_jamo(kc) or is_supported_korean(kc))):
        raise ValueError("'{kc} is not supported korean character")

def get_type(kc):
    check(kc)
    assert is_korean_compatibility_jamo(kc), f"not a jamo! {kc}"
    return sum(tp for tp, string in SETS.items() if kc in string)
    

def join_koreans_char(first, mid, last=None):
    """
    초성 중성 종성을 한 음절로 만들기
    """
    #print(first, mid, last)
    chars = (first, mid, last)

    for char in filter(None, chars):
        check(char, jamo_only=True)
    
    idx = tuple(INDICES[position][char] if char is not None else char for position, char in zip((FIRST, MIDDLE, LAST), chars))

    first_idx, mid_idx, last_idx = idx

    last_idx = 0 if last_idx is None else last_idx + 1 # 종성은 공백 포함해서 0 시작이기 때문에 + 1

    return chr(0xac00 + (588 * first_idx) + (28 * mid_idx) + (last_idx))

def join_koreans(string):
    """
    자음 모음을 합쳐서 음절을 만들고 그 음절들로 한글 문장 만들기
    """
    last_t = 0
    q = []
    result_string = ""

    #print(string)

    def flush(n=0):
        new_q = []
        #print(q)
        while len(q) > n:
            new_q.append(q.pop())
        if len(new_q) == 1:
            result = new_q[0]
        elif len(new_q) >= 2:
            try:
                result = join_koreans_char(*new_q)
            except (ValueError, KeyError):
                result = "".join(new_q)
        else:
            result = None
        return result

    for char in string:
        #print(char)
        if char not in SET:
            if q:
                new_char = flush() + char
            else:
                new_char = char
            last_t = 0
        else:
            t = get_type(char)
            new_char = None
            if t & LAST == LAST:
                if not (last_t == MIDDLE):
                    new_char = flush()
            elif t == FIRST:
                new_char = flush()
            elif t == MIDDLE:
                if last_t & FIRST == FIRST:
                    new_char = flush(1)
                else:
                    new_char = flush()

            last_t = t
            q.insert(0, char)
        if new_char:
            result_string += new_char
    if q:
        result_string += flush()
    
    return result_string