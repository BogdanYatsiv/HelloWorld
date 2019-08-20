def get_rec_square(a,b):
    return a*b

def get_triang_square(h,b):
    return (0.5*b)*h

def get_cir_square(r):
    return 3.14*(r**2)

choice = input('Make choice: rectangle, triangle or circle')
if choice == 'rectangle':
    side_a = float(input('Enter a side: '))
    side_b = float(input('Enter b side: '))
    print('Square = ',get_rec_square(side_a,side_b))
elif choice == 'triangle':
    high = float(input('Enter high of triangle: '))
    side = float(input('Enter side of triangle: '))
    print('Square = ',get_triang_square(high,side))
elif choice == 'circle':
    radius = float(input('Enter radius'))
    print('Square = ',get_cir_square(radius))