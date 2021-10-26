
print("Введи в меня деньги:")
a =float(input())

print("Сколько лет будешь хранить?:")
years = int(input())

def bank(a, years):
    i=0
    while i<years:
        a=a+a*0.1
        i=i+1
    return a



# def bank (b, years):
#     for i in range(years):
#         b = b + (b/100*10)
#
#              return (b)
#
# result = bank (float(input("Введите сумму вклада:")), int(input("На сколько лет:")))

if __name__ == '__main__':
    print(bank(a, years))