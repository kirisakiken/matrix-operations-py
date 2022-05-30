import math
import numpy as np

from src.types.line2 import Line2
from src.types.vector2 import Vector2
from src.types.vector3 import Vector3


class VectorExtensions:
    def __init__(self):
        pass

    @staticmethod
    def get_dot_product(a: Vector2 | Vector3, b: Vector2 | Vector3) -> float:
        if type(a) == Vector2 and type(b) == Vector2:
            v_1_matrix = np.array([[a.x, a.y]])
            v_2_matrix = np.array([[b.x],
                                   [b.y]])
            return np.matmul(v_1_matrix, v_2_matrix)[0][0]
        elif type(a) == Vector3 and type(b) == Vector3:
            v_1_matrix = np.array([[a.x, a.y, a.z]])
            v_2_matrix = np.array([[b.x],
                                   [b.y],
                                   [b.z]])
            return np.matmul(v_1_matrix, v_2_matrix)[0][0]
        else:
            raise TypeError("Invalid argument types for method get_dot_product. Expected types: (Vector2 and "
                            "Vector2) or (Vector3 and Vector3)")

    @staticmethod
    def get_cross_product(a: Vector2 | Vector3, b: Vector2| Vector3) -> float:
        if type(a) == Vector2 and type(b) == Vector2:
            return np.linalg.det(np.array([[a.x, a.y],
                                           [b.x, b.y]]))
        elif type(a) == Vector3 and type(b) == Vector3:
            return np.linalg.det(np.array([[1, 1, 1],
                                          [a.x, a.y, a.z],
                                          [b.x, b.y, b.z]]))
        else:
            raise TypeError("Invalid argument types for method get_dot_product. Expected types: (Vector2 and "
                            "Vector2) or (Vector3 and Vector3)")

    @staticmethod
    def get_distance(a: Vector2 | Vector3, b: Vector2 | Vector3) -> float:
        if type(a) == Vector2 and type(b) == Vector2:
            return math.sqrt(((a.x - b.x) ** 2) + ((a.y - b.y) ** 2))
        elif type(a) == Vector3 and type(b) == Vector3:
            return math.sqrt(((a.x - b.x) ** 2) + ((a.y - b.y) ** 2) + ((a.z + b.z) ** 2))
        else:
            raise TypeError("Invalid argument types for method get_distance. Expected types: (Vector2 and "
                            "Vector2) or (Vector3 and Vector3)")

    @staticmethod
    def get_lerp(a: Vector2 | Vector3, b: Vector2 | Vector3) -> Vector2 | Vector3:
        raise NotImplementedError("VectorExtensions.get_lerp not implemented")

    @staticmethod
    def get_perpendicular_distance_2d(vector: Vector2, line: Line2) -> float:
        return abs((vector.x * line.a) + (vector.y * line.b) + line.c) / line.get_magnitude()

    @staticmethod
    def vector2_to_matrix_1x2(vector_2: Vector2):
        return np.array([[vector_2.x],
                         [vector_2.y]])

    @staticmethod
    def vector2_to_matrix_1x3(vector_2: Vector2):
        return np.array([[vector_2.x],
                         [vector_2.y],
                         [1]])

    @staticmethod
    def vector3_to_matrix_1x3(vector_3: Vector3):
        return np.array([[vector_3.x],
                         [vector_3.y],
                         [vector_3.z]])

    @staticmethod
    def vector3_to_matrix_1x4(vector_3: Vector3):
        return np.array([[vector_3.x],
                         [vector_3.y],
                         [vector_3.z],
                         [1]])
