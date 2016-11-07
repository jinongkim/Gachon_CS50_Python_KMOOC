# my_file = open("i_have_a_dream.txt", "r")
# contents = my_file.read()
# print (type(contents), contents)

with open("i_have_a_dream.txt", "r") as my_file:
    contents = my_file.read()
    print (type(contents), contents)

with open("i_have_a_dream.txt", "r") as my_file:
    content_list = my_file.readlines() #파일 전체를 list로 반환
    print(type(content_list)) #Type 확인
    print(content_list) #리스트 값 출력

with open("i_have_a_dream.txt", "r") as my_file:
    i = 0
    while 1:
        line = my_file.readline().replace("\n","")
        if line.strip() == "":
            continue
        if not line: break
        print (str(i) + " === " + line)	 #한줄씩 값 출력
        i = i + 1


with open("i_have_a_dream.txt", "r") as my_file:
    contents = my_file.read()
    word_list = contents.split(" ")	 #빈칸 기준으로 단어를 분리 리스트
    line_list = contents.split("\n")	 #한줄 씩 분리하여 리스트

print("Total Number of Characters :", len(contents))
print("Total Number of Words:", len(word_list))
print("Total Number of Lines :", len(line_list))
