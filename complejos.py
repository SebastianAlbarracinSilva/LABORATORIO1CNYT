import math

def sumacplx(a,b):
    return((a[0]+b[0],a[1]+b[1]))

def multcplx(a,b):
    return((a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]))

def restacplx(a,b):
    return((a[0]-b[0],a[1]-b[1]))

def modulocplx(a):
    return(math.sqrt(a[0]*a[0]+a[1]*a[1]))

def conjugadocplx(a):
    return(a[0],-a[1])


def divisioncplx(a, b):
    divisor = b[0]*b[0] + b[1]*b[1]
    b_conjugado = (b[0], -b[1])
    num = multcplx(a, b_conjugado)
    real = num[0] / divisor
    imaginario = num[1] / divisor
    return (real, imaginario)


def fasecplx(a):
    fase = math.atan2(a[1], a[0])
    return fase

def polar_a_cart(polar):
    r, theta = polar, 0
    real = r * math.cos(theta)
    imaginaria = r * math.sin(theta)
    return (real, imaginaria)

def cart_a_polar(cart):
    real, imaginaria = cart
    r = modulocplx(cart)
    theta = math.atan2(imaginaria, real)
    return (r, theta)


if __name__ == '__main__':
    #PRUEBAS EN CODIGO(TAMBIEN ESTAN EN LOS TEST)
    print("PRUEBAS SUMA")
    print(sumacplx((3.5,6),(-6.7,2)))
    print(sumacplx((5.5,32),(-8.7,24)))
    print("PRUEBAS MULTIPLICACION")
    print(multcplx((3.5,6),(-6.7,2)))
    print(multcplx((5.5,32),(-8.7,24)))
    print("PRUEBAS RESTA")
    print(restacplx((3.5,6),(-6.7,2)))
    print(restacplx((5.5,32),(-8.7,24)))
    print("PRUEBAS MODULO")
    print(modulocplx((2,3)))
    print(modulocplx((3,7)))
    print("PRUEBAS CONJUGADO")
    print(conjugadocplx((2,3)))
    print(conjugadocplx((3,7)))
    print("PRUEBAS DIVISION")
    print(divisioncplx((3.5,6),(-6.7,2)))
    print(divisioncplx((5.5,32),(-8.7,24)))
    print("PRUEBAS FASE")
    print(fasecplx((3, 3)))
    print(fasecplx((2, 6)))
    print("PRUEBAS POLAR A CART")
    print(polar_a_cart(13))
    print(polar_a_cart(24))
    print("PRUEBAS CART A POLAR")
    print(cart_a_polar((11, 0)))
    print(cart_a_polar((20, 0)))