from src.types.axis import (
    Axis2,
    Axis3,
)
from src.types.vector2 import Vector2
from src.types.vector3 import Vector3
from src.operations.transformation import TransformationOperator
from src.operations.translation import TranslationOperator
from src.operations.rotation import RotationOperator
from src.operations.scale import ScaleOperator


class MatrixOperator:
    def __init__(self):
        self.transformation_operator = TransformationOperator()
        self.translation_operator = TranslationOperator()
        self.rotation_operator = RotationOperator()
        self.scale_operator = ScaleOperator()

    def apply_transformation_2d(self, vector_2: Vector2, transformation_axis: Axis2) -> Vector2:
        return self.transformation_operator.get_transformation_2d(vector_2, transformation_axis)

    def apply_transformation_3d(self, vector_3: Vector3, transformation_axis: Axis3) -> Vector3:
        return self.transformation_operator.get_transformation_3d(vector_3, transformation_axis)

    def apply_translation_2d(self, vector_2: Vector2, translation_vector: Vector2) -> Vector2:
        return self.translation_operator.get_translation_2d(vector_2, translation_vector)

    def apply_rotation_2d(self, vector_2: Vector2, degree: float) -> Vector2:
        return self.rotation_operator.get_rotation_2d(vector_2, degree)

    def apply_scale_2d(self, vector_2: Vector2, scale_vector: Vector2) -> Vector2:
        return self.scale_operator.get_scale_2d(vector_2, scale_vector)
