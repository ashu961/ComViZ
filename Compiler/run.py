from Compiler.interpreter.context import Context
from Compiler.interpreter.data_types import Number
from Compiler.interpreter.interpreter import Interpreter
from Compiler.interpreter.symbol_table import SymbolTable
from Compiler.lexical_analyzer.lexer import Lexer
from Compiler.syntax_analyzer.parser import Parser
from Visualiser.visualise_st import visualise_st

global_symbol_table = SymbolTable()
global_symbol_table.set_var_value("NULL", Number(0), '<program>')
global_symbol_table.set_var_value("TRUE", Number(1), '<program>')
global_symbol_table.set_var_value("FALSE", Number(0), '<program>')
global_context = Context(
    curr_context_name='<program>',
    parent_context_name=None,
    context_change_pos=None,
)
global_context.symbol_table = global_symbol_table
visualise_st(context=global_context)


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
    parse_result = parser.parse_tokens()

    syntax_error = parse_result.error
    abstract_syntax_tree_root = parse_result.node
    trace = parser.trace

    if syntax_error:
        # if syntax_error, interpreter will not be used and directly error will be displayed
        return tokens, abstract_syntax_tree_root, syntax_error, None

    # Evaluate the abstract syntax tree obtained using interpreter
    interpreter = Interpreter()

    runtime_result = interpreter.evaluate_node(node=abstract_syntax_tree_root, context=global_context)

    if not runtime_result.error:
        return tokens, (abstract_syntax_tree_root, trace), None, runtime_result.result

    return tokens, (abstract_syntax_tree_root, trace), runtime_result.error, None
