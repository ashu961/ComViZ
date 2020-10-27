from Compiler.interpreter.interpreter import Interpreter
from Compiler.lexical_analyzer.lexer import Lexer
from Compiler.syntax_analyzer.parser import Parser


def run(file_name, text):
    """
    Args:
        file_name: File name where HLL program is written
        text: High Level Language

    Returns: ( tokens, abstract_syn_tree, error, runtime_result )
    """
    # Generate Tokens
    lexer = Lexer(file_name, text)
    tokens, lexical_error = lexer.make_token()

    if lexical_error:
        # if lexical_error, no abstract_syn_tree will be able to be formed thus return None for abstract_syn_tree
        return tokens, None, lexical_error, None

    # Parse tokens
    parser = Parser(token_list=tokens)

    # Generate Abstract Syntax Tree for Arithmetic Expression
    parse_result = parser.arith_exp_parser()

    syntax_error = parse_result.error
    abstract_syntax_tree_root = parse_result.node

    if syntax_error:
        # if syntax_error, interpreter will not be used and directly error will be displayed
        return tokens, abstract_syntax_tree_root, syntax_error, None

    # Evaluate the abstract syntax tree obtained using interpreter
    interpreter = Interpreter()
    runtime_result = interpreter.evaluate_node(node=abstract_syntax_tree_root)

    if not runtime_result.error:
        return tokens, abstract_syntax_tree_root, None, runtime_result.result

    return tokens, abstract_syntax_tree_root, runtime_result.error, None
