class NumberNode:
    """
    Nodes for representing Number Tokens i.e. TT_INT or TT_FLOAT
    """
    def __init__(self, num_token):
        """

        Args:
            num_token: Token object of TT_INT or TT_FLOAT
        """
        self.num_token = num_token
        self.pos_start = num_token.pos_start
        self.pos_end = num_token.pos_end

    def __repr__(self):
        """

        Returns: String representation of Node

        """
        return f'{self.num_token}'


class BinaryOperationNode:
    """
    Nodes for representing arithmetic operations +,-,*,/
    """
    def __init__(self, left_num_node, op_token, right_num_node):
        self.left_num_node = left_num_node
        self.op_token = op_token
        self.right_num_node = right_num_node

        self.pos_start = self.left_num_node.pos_start
        self.pos_end = self.right_num_node.pos_end

    def __repr__(self):
        return f'({self.left_num_node}, {self.op_token}, {self.right_num_node})'


class UnaryOperationNode:
    def __init__(self, op_token, node):
        self.op_token = op_token
        self.node = node

        self.pos_start = self.op_token.pos_start
        self.pos_end = self.node.pos_end

    def __repr__(self):
        return f'({self.op_token}, {self.node})'
