import my_module # 같은 디렉토리에 있는 파일을 불러옴

my_module.greeting()
my_module.greeting('이주호')

from my_module import greeting
greeting('이재찬')

from my_module import pi as p
print(my_module.pi)
print(p)
