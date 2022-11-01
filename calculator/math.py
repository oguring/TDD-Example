class Calculator:
    def min(self, left_val: int, right_val: int):
        if not isinstance(left_val, int) or not isinstance(right_val, int):
            raise TypeError
        return left_val if left_val < right_val else right_val
