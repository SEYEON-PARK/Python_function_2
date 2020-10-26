def plus(a):
    if a<0:
        a=plus(int(input("양수만 입력하시오 : ")))
        return a;
    else:
        return a;

width=plus(int(input("삼각형의 밑변 : ")))
height=plus(int(input("삼각형의 높이 : ")))

print("면적= {}".format(width*height/2))
