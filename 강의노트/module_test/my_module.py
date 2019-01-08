def greeting(name='아이유'):
    print(f'안녕, {name}')

pi = 3.141592

if __name__ == '__main__': # 직접 불렀으면 name이 main이 되는 듯.
    print('main : 직접 실행되었습니다.')
    print(__name__)
else:
    print('모듈로 불러져서 실행되었습니다.')
    print(__name__)

# $ python a.py 하면 모듈로 불려져서 실행되었다고 뜸
# $ python my_module.py 하면 직접 실행되었다고 뜸

