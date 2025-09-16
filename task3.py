# tasks/task1.py



def solve():
# Ниже пишите решение задачии(Обязательно поставьте четыре пробела после функции Solve())
    weight = float(input("Введите вес (в кг): "))
    height = float(input("Введите рост (в метрах): "))
    bmi = weight / (height ** 2)
    print(f"Индекс массы тела (BMI): {bmi:.2f}")
   

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()