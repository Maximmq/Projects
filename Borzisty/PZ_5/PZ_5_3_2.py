# Описать функцию TriangePS(параметры), вычисляющую по стороне а равностор.
# треугольника его периметр Р и площадь S. С помощью этой функции найти
# периметры и площади трех равносторонних треугольников с данными сторонами.
def TrianglePS(sides):
    for i in range(len(sides)):
        print(f'{'\n'}Периметр Δ{i+1}: {sides[i]*3:.3f}')
        print(f'Площадь Δ{i+1}: {sides[i]**2*0.75**0.5/2:.3f}')


try:
    sds = [float(i) for i in input("Ввод сторон Δ-ков через пробел: ").split()]
    TrianglePS(sds)
except ValueError:
    print('Неверный ввод!')
