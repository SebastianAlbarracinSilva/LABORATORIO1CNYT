import unittest
import complejos as lc

class TestCplxOperations(unittest.TestCase):

    def test_cplxsum(self):
        self.assertEqual(lc.sumacplx((3.5,6),(-6.7,2)),(-3.2,8) )
        self.assertEqual(lc.sumacplx((5.5,32),(-8.7,24)),(-3.1999999999999993, 56))

    def test_cplxresta(self):
        self.assertEqual(lc.restacplx((3.5,6),(-6.7,2)),(10.2, 4) )
        self.assertEqual(lc.restacplx((5.5,32),(-8.7,24)),(14.2, 8))

    def test_cplxmulti(self):
        self.assertEqual(lc.multcplx((3.5,6),(-6.7,2)),(-35.45, -33.2) )
        self.assertEqual(lc.multcplx((5.5,32),(-8.7,24)),(-815.85, -146.39999999999998))

    def test_cplxdiv(self):
        self.assertEqual(lc.divisioncplx((3.5,6),(-6.7,2)),(-0.2341992227449376, -0.965432603804459))
        self.assertEqual(lc.divisioncplx((5.5,32),(-8.7,24)),(1.1050499470607191, -0.6297472724761773))

    def test_modulo(self):
        self.assertEqual(lc.modulocplx((2,3)), 3.605551275463989)
        self.assertEqual(lc.modulocplx((3,7)), 7.615773105863909)

    def test_conjugado(self):
        self.assertEqual(lc.conjugadocplx((2,3)), (2, -3))
        self.assertEqual(lc.conjugadocplx((3,7)), (3, -7))

    def test_fase(self):
        self.assertEqual(lc.fasecplx((3, 3)), 0.7853981633974483)
        self.assertEqual(lc.fasecplx((2, 6)), 1.2490457723982544)

    def test_polar_a_cart(self):
        self.assertEqual(lc.polar_a_cart(13), (13.0, 0.0))
        self.assertEqual(lc.polar_a_cart(24), (24.0, 0.0))

    def test_cart_a_polar(self):
        self.assertEqual(lc.cart_a_polar((11, 0)), (11.0, 0.0))
        self.assertEqual(lc.cart_a_polar((20, 0)), (20.0, 0.0))


if __name__ == '__main__':
    unittest.main()
