from Compiler.error_handler.runtime_err import InterpreterError


class Number:
    """
        To store numbers and operating on them with other numbers
    """

    def __init__(self, value):
        """
        Args:
            value: any number ( Token().value i.e. value part of a Token() object of type = INT or FLOAT )
        """
        self.value = value
        self.pos_start = None
        self.pos_end = None
        self.context = None
        self.set_context()
        self.set_pos()

    def set_pos(self, pos_start=None, pos_end=None):
        """
            To indicate position while showing error messages
        Args:
            pos_start: starting of the number
            pos_end: ending of the number

        Returns: self
        """
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    # Operations on Number data type:

    # When number represented by self is to be added to any other Number object with a number
    def added_to(self, other_operand):
        if isinstance(other_operand, Number):
            return Number(value=self.value + other_operand.value), None

    # When number represented by self is to be subtracted to any other Number object with a number
    def subtracted_by(self, other_operand):
        if isinstance(other_operand, Number):
            return Number(value=self.value - other_operand.value).set_context(context=self.context), None

    # When number represented by self is to be added to any other Number object with a number
    def multiplied_by(self, other_operand):
        if isinstance(other_operand, Number):
            return Number(value=self.value * other_operand.value).set_context(context=self.context), None

    # When number represented by self is to be added to any other Number object with a number
    def divided_by(self, other_operand):
        if isinstance(other_operand, Number):
            if other_operand.value == 0:
                return None, InterpreterError(
                    other_operand.pos_start, other_operand.pos_end,
                    'Division by zero',
                    context=self.context
                )
            return Number(value=self.value / other_operand.value).set_context(context=self.context), None

    # When number represented by self is to be raised to any other Number object with a number
    def raised_to(self, other_operand):
        if isinstance(other_operand, Number):
            return Number(value=self.value**other_operand.value).set_context(context=self.context), None

    def copy(self):
        copy = Number(self.value)
        copy.set_pos(pos_start=self.pos_start, pos_end=self.pos_end)
        copy.set_context(self.context)
        return copy

    # Comparison Operations ( True = 1 , False = 0 )

    def get_comparison_eq(self, other_operand):
        if isinstance(other_operand, Number):
            return Number(int(self.value == other_operand.value)).set_context(self.context), None

    def get_comparison_ne(self, other_operand):
        if isinstance(other_operand, Number):
            return Number(int(self.value != other_operand.value)).set_context(self.context), None

    def get_comparison_lt(self, other_operand):
        if isinstance(other_operand, Number):
            return Number(int(self.value < other_operand.value)).set_context(self.context), None

    def get_comparison_lte(self, other_operand):
        if isinstance(other_operand, Number):
            return Number(int(self.value <= other_operand.value)).set_context(self.context), None

    def get_comparison_gt(self, other_operand):
        if isinstance(other_operand, Number):
            return Number(int(self.value > other_operand.value)).set_context(self.context), None

    def get_comparison_gte(self, other_operand):
        if isinstance(other_operand, Number):
            return Number(int(self.value >= other_operand.value)).set_context(self.context), None

    def anded_by(self, other_operand):
        if isinstance(other_operand, Number):
            return Number(int(self.value and other_operand.value)).set_context(self.context), None

    def ored_by(self, other_operand):
        if isinstance(other_operand, Number):
            return Number(int(self.value or other_operand.value)).set_context(self.context), None

    def notted(self):
        return Number(1 if self.value == 0 else 0).set_context(self.context), None

    def is_true(self):
        return self.value != 0

    def __repr__(self):
        return str(self.value)

    def set_context(self, context=None):
        self.context = context
        return self
