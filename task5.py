# tasks/task1.py



def solve():
# Ниже пишите решение задачии(Обязательно поставьте четыре пробела после функции Solve())
    numbers_input = input("Введите числа: ")
    numbers = list(map(int, numbers_input.split()))
    squares = list(map(lambda x: x * x, numbers))
    result = " ".join(map(str, squares))
    print("Результат:", result)
    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()