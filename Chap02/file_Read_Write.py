''' 
open 함수를 사용해 읽기와 쓰기가 가능한 파일 객체를 생성 가능
파일 경로와 모드 2개의 인수가 필요, 모드의 초깃값은 읽기로 설정
모드는 파일 읽기 또는 쓰기 여부와 파일의 데이터가 텍스트 또는 바이너리인지를 지정
'''
file_path = 'book.txt' 
open_file = open(file_path, 'r') 

text = open_file.read() 

#print(len(text))
#print(text[15])
#print(open_file)

open_file.close()

# 작업이 끝난 파일은 close 처리해주는 습관을 들이는 것이 좋습니다.
# 파이썬은 더 이상 사용하지 않는 파일을 알아서 처리하는 기능이 있지만, 그때까지 리소스를 점유하게 되며 
# 다른 프로세스가 해당 파일을 열지 못하게 될 수도 있기 때문입니다. 

'''
readlines 메서드를 사용해 파일을 읽을 수도 있습니다.
이 메서드는 파일을 읽어서 그 내용을 개행한 문자(newline character) 기준으로 나눠 문자열 리스트를 반환해줍니다.
각 문자열은 원본 텍스트의 한 라인에 해당합니다.
'''

file_path = 'book2.txt'
open_file = open(file_path, 'r')
text = open_file.readlines() 
#print(len(text))
#print(text[0])
#print(text[1])
#print(text[2])

open_file.close()



