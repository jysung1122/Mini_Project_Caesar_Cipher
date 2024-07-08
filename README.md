# Mini_Project_Caesar_Cipher

## 카이사르 암호란?
카이사르 암호(Caesar cipher)는 고전 암호학에서 사용된 가장 오래된 암호 기법 중 하나로, 로마 황제 줄리어스 시저가 군사 통신에 사용했다고 알려져 있음. 이 암호화 방식은 알파벳을 일정한 수만큼 밀어내어 암호화함.

### 암호화 방법
- 키 설정: 한 자리의 숫자(일반적으로 1부터 25까지)를 키로 설정함
- 알파벳 이동: 평문(암호화되지 않은 텍스트)의 각 문자를 키 값만큼 오른쪽으로 이동시킴
- 예를 들어, 키가 3이라면 'A'는 'D', 'B'는 'E', 'C'는 'F'가 됨
- 순환 처리: 알파벳의 끝에 도달하면 처음으로 되돌아감
- 예를 들어, 'X'를 3만큼 이동하면 'A'가 됨
### 예시
- 평문: HELLO
- 키: 3
- 암호문: KHOOR
### 복호화 방법
- 암호문을 키 값만큼 왼쪽으로 이동시키면 원래의 평문을 얻을 수 있음

## 개발 순서
### 1. 암호화 함수 생성
```
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift) :
    cipher_text = ""
    for i in plain_text :
        position = alphabet.index(i) + shift
        if position > 25 :
            position = position % 26
        cipher_text += alphabet[position]
    print(f"The encoded text is {cipher_text}")
    
if direction == "encode" :
    encrypt(text, shift)
```

### 2. 복호화 함수 추가
```
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift) :
    cipher_text = ""
    for i in plain_text :
        position = alphabet.index(i) + shift
        if position > 25 :
            position = position % 26
        cipher_text += alphabet[position]
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift) :
    plain_text = ""
    for i in cipher_text :
        position = alphabet.index(i) - shift
        if position < 0 :
            position = position % 26
        plain_text += alphabet[position]
    print(f"The decoded text is {plain_text}")

if direction == "encode" :
    encrypt(text, shift)
elif direction == "decode" :
    decrypt(text, shift)
```

### 3. 코드 재구성
```
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction, text, shift) :
    change_text = ""
    if direction == "decode" :
        shift *= -1
    for i in text :
        position = alphabet.index(i) + shift
        if position > 25 or position < 0 :
            position = position % 26
        change_text += alphabet[position]
    print(f"The {direction} text is {change_text}")
    
caesar(direction, text, shift)
```

### 4. 유저 경험 개선
```
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

while True :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    def caesar(direction, text, shift) :
        change_text = ""
        if direction == "decode" :
            shift *= -1
        for i in text :
            if i not in alphabet :
                change_text += i
            else :
                position = alphabet.index(i) + shift
                if position > 25 or position < 0 :
                    position = position % 26
                change_text += alphabet[position]
        print(f"The {direction} text is {change_text}")
        
    caesar(direction, text, shift)
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no" :
        print("Goodbye")
        break
```
