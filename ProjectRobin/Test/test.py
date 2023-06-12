import unittest

def turn(rotation_angle, angle):
    rotation_angle = (rotation_angle + angle) % 360

    directions = ["->", "↑", "<-", "↓"]

    direction_index = rotation_angle // 90
    direction = directions[direction_index]

    return rotation_angle, direction

class TestRobot(unittest.TestCase):

    def test_turn(self):
        # Caso de giro a 90 grados 
        rotation_angle, direction = turn(0, 90)
        self.assertEqual(rotation_angle, 90)
        self.assertEqual(direction, "↑")

        # Caso de giro a 180 grados
        rotation_angle, direction = turn(rotation_angle, 90)
        self.assertEqual(rotation_angle, 180)
        self.assertEqual(direction, "<-")

        # Caso de giro a 270 grados
        rotation_angle, direction = turn(rotation_angle, 90)
        self.assertEqual(rotation_angle, 270)
        self.assertEqual(direction, "↓")

        # Caso de giro a 360 grados
        rotation_angle, direction = turn(rotation_angle, 90)
        self.assertEqual(rotation_angle, 0)
        self.assertEqual(direction, "->")

        # Caso de giro a -90 grados (giro en sentido contrario)
        rotation_angle, direction = turn(rotation_angle, -90)
        self.assertEqual(rotation_angle, 270)
        self.assertEqual(direction, "↓")

        # Caso de giro a 180 grados (dos vueltas completas)
        rotation_angle, direction = turn(rotation_angle, 180)
        self.assertEqual(rotation_angle, 90)
        self.assertEqual(direction, "↑")

if __name__ == '__main__':
    unittest.main()
