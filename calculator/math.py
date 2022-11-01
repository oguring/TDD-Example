class Calculator:
    def min(self, left_int_val: int, right_int_val: int):
        if (not isinstance(left_int_val, int)
                or not isinstance(right_int_val, int)):
            raise TypeError
        return left_int_val if left_int_val < right_int_val else right_int_val
