import main


# SETTING UP LIBRARIES AND TEST VALUES 
from main import Error

# Create a Position instance
pos_start = main.Position(0, 0, 'test', 'test.txt', 'ftxt')
pos_end = main.Position(0, 4, 'test', 'test.txt', 'ftxt')


def test_lexer():
    text = "var x: int = 5"
    lexer = main.Lexer("test", text)
    tokens, error = lexer.make_tokens()
    assert error is None
    assert len(tokens) == 7


def test_parser():
    # Define some code to parse
    lexer = main.Lexer('<stdin>', 'var a: INT = 10\nvar b: INT = 20\nreturn a + b')

    # Get tokens from lexer
    tokens, error = lexer.make_tokens()
    if error:
        return None, error

    # Import the parser

    # Create parser instance
    parser = main.Parser(tokens)

    # Parse the code
    ast = parser.parse()
    return ast.node, ast.error


# def test_error_classes():
#     # Test IllegalCharError instantiation and attributes
#     pos_start = main.Position(0, 1, 0, "test", "input")
#     pos_end = main.Position(1, 1, 1, "test", "input")
#     illegal_char_error = main.IllegalCharError(pos_start, pos_end, "Illegal character 'x'")
#     assert illegal_char_error.pos_start == pos_start
#     assert illegal_char_error.pos_end == pos_end
#     assert illegal_char_error.error_name == "Illegal Character"
#     assert illegal_char_error.details == "Illegal character 'x'"
#     assert illegal_char_error.as_string() == "Illegal Character: Illegal character 'x'\nFile test, line 1\n\ninput\n ^"
#
#     # Test ExpectedCharError instantiation and attributes
#     pos_start = main.Position(0, 1, 0, "test", "input")
#     pos_end = main.Position(1, 1, 1, "test", "input")
#     expected_char_error = main.ExpectedCharError(pos_start, pos_end, "Expected '='")
#     assert expected_char_error.pos_start == pos_start
#     assert expected_char_error.pos_end == pos_end
#     assert expected_char_error.error_name == "Expected Character"
#     assert expected_char_error.details == "Expected '='"
#     assert expected_char_error.as_string() == "Expected Character: Expected '='\nFile test, line 1\n\ninput\n ^"
#
#     # Test InvalidSyntaxError instantiation and attributes
#     pos_start = main.Position(0, 1, 0, "test", "input")
#     pos_end = main.Position(1, 1, 1, "test", "input")
#     invalid_syntax_error = main.InvalidSyntaxError(pos_start, pos_end, "Invalid Syntax")
#     assert invalid_syntax_error.pos_start == pos_start
#     assert invalid_syntax_error.pos_end == pos_end
#     assert invalid_syntax_error.error_name == "Invalid Syntax"
#     assert invalid_syntax_error.details == "Invalid Syntax"
#     assert invalid_syntax_error.as_string() == "Invalid Syntax: Invalid Syntax\nFile test, line 1\n\ninput\n ^"
#
#     # Test RTError instantiation and attributes
#     pos_start = main.Position(0, 1, 0, "test", "input")
#     pos_end = main.Position(1, 1, 1, "test", "input")
#     context = main.Context("Test Context", pos_start)
#     rt_error = main.RTError(pos_start, pos_end, "Runtime Error", context)
#     assert rt_error.pos_start == pos_start
#     assert rt_error.pos_end == pos_end
#     assert rt_error.error_name == "Runtime Error"
#     assert rt_error.details == "Runtime Error"
#     assert rt_error.context == context
#     assert rt_error.as_string() == "Traceback (most recent call last):\n  File test, line 1, in Test Context\nRuntime Error: Runtime Error\n\ninput\n ^"

# Test Error
def test_error_name_details():
    

    error = main.Error(pos_start, pos_end, 'Error Name', 'Error Details')
    assert str(error.error_name) == 'Error Name'
    assert str(error.details) == 'Error Details'

def test_illegal_char_error():
    # Test IllegalCharError
    illegal_char_error = main.IllegalCharError(pos_start, pos_end, 'Illegal character details')
    assert str(illegal_char_error.error_name) == 'Illegal Character'
    assert str(illegal_char_error.details) == 'Illegal character details'


def test_expected_char_error():
    # Test ExpectedCharError
    expected_char_error = main.ExpectedCharError(pos_start, pos_end, 'Expected character details')
    assert str(expected_char_error.error_name) == 'Expected Character'
    assert str(expected_char_error.details) == 'Expected character details'

def test_invalid_syntax_error():
    # Test InvalidSyntaxError
    invalid_syntax_error = main.InvalidSyntaxError(pos_start, pos_end, 'Invalid syntax details')
    assert str(invalid_syntax_error.error_name) == 'Invalid Syntax' 
    assert str(invalid_syntax_error.details) == 'Invalid syntax details'

# def test_RTError():
#     # Test RTError
#     context = main.Context('<program>')
#     context.symbol_table = main.SymbolTable()
#     context.symbol_table.set('a', main.Number(5))
#     rt_error = main.RTError(pos_start, pos_end, 'Runtime error details', context)
#     assert str(rt_error).startswith('Traceback (most recent call last):\n  File test.txt, line 1, '
#                                     'in <program>\nRuntime Error: Runtime error details')

def test_token_class():
    pos_start = main.Position(0, 1, 0, "test", "input")
    pos_end = main.Position(1, 1, 1, "test", "input")
    token = main.Token(main.TT_INT, 10, pos_start, pos_end)
    assert str(token.type) in str(main.TT_INT)
    assert token.value == 10
    # assert token.pos_start == pos_start
    # assert token.pos_end == pos_end

def test_node_classes():
    tok = main.Token(main.TT_INT, 10, None, None)
    number_node = main.NumberNode(tok)
    assert number_node.tok == tok

    string_node = main.StringNode(tok)
    assert string_node.tok == tok

    bin_op_node = main.BinOpNode(number_node, main.Token(main.TT_PLUS), number_node)
    assert bin_op_node.left_node == number_node
    assert bin_op_node.op_tok.type == main.TT_PLUS
    assert bin_op_node.right_node == number_node

    unary_op_node = main.UnaryOpNode(main.Token(main.TT_MINUS), number_node)
    assert unary_op_node.op_tok.type == main.TT_MINUS
    assert unary_op_node.node == number_node

    var_access_node = main.VarAccessNode(tok)
    assert var_access_node.var_name_tok == tok

    var_assign_node = main.VarAssignNode(tok, number_node, main.TT_INT, "int")
    assert var_assign_node.var_name_tok == tok
    assert var_assign_node.value_node == number_node
    assert var_assign_node.type == main.TT_INT
    assert var_assign_node.var_type == "int"


def test_position_class():
    pos = main.Position(0, 1, 0, "test", "input")
    assert pos.idx == 0
    assert pos.ln == 1
    assert pos.col == 0
    assert pos.fn == "test"
    assert pos.ftxt == "input"


def test_call_node_class():
    tok = main.Token(main.TT_INT, 10, None, None)
    call_node = main.CallNode(main.VarAccessNode(tok), [])
    assert call_node.node_to_call.var_name_tok == tok
    assert call_node.arg_nodes == []


def test_return_node_class():
    tok = main.Token(main.TT_INT, 10, None, None)
    return_node = main.ReturnNode(main.NumberNode(tok), None, None)
    assert return_node.node_to_return.tok == tok


def test_continue_node_class():
    cont_node = main.ContinueNode(None, None)
    assert cont_node.pos_start is None
    assert cont_node.pos_end is None


def test_break_node_class():
    break_node = main.BreakNode(None, None)
    assert break_node.pos_start is None
    assert break_node.pos_end is None


def test_parse_result_class():
    # Create a ParseResult object
    result = main.ParseResult()

    # Test if the initial state is correct
    assert result.error is None
    assert result.node is None
    assert result.last_registered_advance_count == 0
    assert result.advance_count == 0
    assert result.to_reverse_count == 0

    # Test register_advancement method
    result.register_advancement()
    assert result.last_registered_advance_count == 1
    assert result.advance_count == 1

    # Test register method
    child_result = main.ParseResult()
    child_result.register_advancement()
    child_result.register_advancement()
    child_result.node = main.NumberNode(main.Token(main.TT_INT, 5))
    child_result.error = main.Error(
        main.Position(1, 1, 1, "test", "input"),
        main.Position(1, 1, 1, "test", "input"),
        "Test error",
        "Test error details"  # Add the details argument here
    )
    registered_node = result.register(child_result)

    # Assert the state after registration
    assert result.last_registered_advance_count == 2
    assert result.advance_count == 3

    # Debugging output to inspect node attributes
    print("Result node:", result.node)
    print("Child result node:", child_result.node)
    print("Registered node:", registered_node)

    # Assert that the node attribute is correctly set
    assert result.node == child_result.node == registered_node


def test_parser_parse():
    # Define some sample tokens for testing
    tokens = [
        main.Token(main.TT_INT, '10', pos_start=main.Position(1, 1, 0, fn="example.txt", ftxt="10 + 5\n"),
                   pos_end=main.Position(1, 3, 2, fn="example.txt", ftxt="10 + 5\n")),
        main.Token(main.TT_PLUS, '+', pos_start=main.Position(1, 4, 3, fn="example.txt", ftxt="10 + 5\n"),
                   pos_end=main.Position(1, 4, 3, fn="example.txt", ftxt="10 + 5\n")),
        main.Token(main.TT_INT, '5', pos_start=main.Position(1, 5, 4, fn="example.txt", ftxt="10 + 5\n"),
                   pos_end=main.Position(1, 5, 4, fn="example.txt", ftxt="10 + 5\n")),
        main.Token(main.TT_NEWLINE, '\n', pos_start=main.Position(1, 6, 5, fn="example.txt", ftxt="10 + 5\n"),
                   pos_end=main.Position(1, 6, 5, fn="example.txt", ftxt="10 + 5\n")),
        main.Token(main.TT_EOF, '', pos_start=main.Position(2, 1, 6, fn="example.txt", ftxt="10 + 5\n"),
                   pos_end=main.Position(2, 1, 6, fn="example.txt", ftxt="10 + 5\n"))
    ]

    # Initialize the parser with the sample tokens
    parser = main.Parser(tokens)

    # Call the parse method and assert the result
    result = parser.parse()
    assert not result.error  # Ensure no error occurred during parsing
    assert parser.current_tok.type == main.TT_EOF  # Ensure the current token is EOF after parsing


def test_rtresult():
    # Test resetting the RTResult object
    result = main.RTResult()
    result.error = main.Error(
        main.Position(1, 1, 1, "test", "input"),  # Provide pos_end
        main.Position(1, 1, 1, "test", "input"),  # Provide error_name
        "Test Error",  # Provide error_name
        "Test error details"  # Provide details
    )
    result.func_return_value = "Return Value"
    result.loop_should_continue = True
    result.loop_should_break = True
    result.reset()
    assert result.error is None
    assert result.func_return_value is None
    assert result.loop_should_continue is False
    assert result.loop_should_break is False

    # Test success method
    result = main.RTResult().success(42)
    assert result.error is None
    assert result.func_return_value is None
    assert result.loop_should_continue is False
    assert result.loop_should_break is False
    assert result.value == 42

    # Test success_return method
    result = main.RTResult().success_return("Return Value")
    assert result.error is None
    assert result.value is None
    assert result.loop_should_continue is False
    assert result.loop_should_break is False
    assert result.func_return_value == "Return Value"

    # Test success_continue method
    result = main.RTResult().success_continue()
    assert result.error is None
    assert result.value is None
    assert result.func_return_value is None
    assert result.loop_should_break is False
    assert result.loop_should_continue is True

    # Test success_break method
    result = main.RTResult().success_break()
    assert result.error is None
    assert result.value is None
    assert result.func_return_value is None
    assert result.loop_should_continue is False
    assert result.loop_should_break is True

    # Test failure method
    result = main.RTResult().failure(main.Error(
        main.Position(1, 1, 1, "test", "input"),  # Provide pos_end
        main.Position(1, 1, 1, "test", "input"),  # Provide error_name
        "Test Error",  # Provide error_name
        "Test error details"  # Provide details
    ))
    assert result.value is None
    assert result.func_return_value is None
    assert result.loop_should_continue is False
    assert result.loop_should_break is False

    # Test should_return method
    result = main.RTResult()
    assert not result.should_return()

    result.error = main.Error(
        main.Position(1, 1, 1, "test", "input"),  # Provide pos_end
        main.Position(1, 1, 1, "test", "input"),  # Provide error_name
        "Test Error",  # Provide error_name
        "Test error details"  # Provide details
    )
    assert result.should_return()

    result.error = None
    result.func_return_value = "Return Value"
    assert result.should_return()

    result.func_return_value = None
    result.loop_should_continue = True
    assert result.should_return()

    result.loop_should_continue = False
    result.loop_should_break = True
    assert result.should_return()


def test_value():
    # set position
    value = main.Value()
    value.set_pos(1, 2)
    assert value.pos_start == 1
    assert value.pos_end == 2
    # set context
    value = main.Value()
    value.set_context('test_context')
    assert value.context == 'test_context'
    # added to

    result, error = value.added_to('other')
    assert result is None
    assert error is not None

    # test subbed

    result, error = value.subbed_by('other')
    assert result is None
    assert error is not None

    # test multed by
    result, error = value.multed_by('other')
    assert result is None
    assert error is not None

    # test powed by
    result, error = value.powed_by('other')
    assert result is None
    assert error is not None

    # get comparison rq
    result, error = value.get_comparison_eq('other')
    assert result is None
    assert error is not None

    # get comparison ne
    result, error = value.get_comparison_ne('other')
    assert result is None
    assert error is not None

    # comparison lt

    result, error = value.get_comparison_lt('other')
    assert result is None
    assert error is not None

    # comparison gt
    result, error = value.get_comparison_gt('other')
    assert result is None
    assert error is not None

    # get comparison lte
    result, error = value.get_comparison_lte('other')
    assert result is None
    assert error is not None

    # test anded by
    result, error = value.anded_by('other')
    assert result is None
    assert error is not None

    #ored by
    result, error = value.ored_by('other')
    assert result is None
    assert error is not None

    # notted by
    result, error = value.notted('other')
    assert result is None
    assert error is not None

    # execute
    result = value.execute('args')
    assert result.error is not None

    # test copy
    try:
        value.copy()
        assert False, "Expected an Exception but didn't get one"
    except Exception as e:
        assert str(e) == 'No copy method defined'

    assert not value.is_true()


def test_number():
    # Create a Number instance
    number = main.Number(5)

    # Test __str__ and __repr__
    assert str(number) == '5'
    assert repr(number) == '5'

    # Test added_to
    result, error = number.added_to(main.Number(3))
    assert result.value == 8
    assert error is None

    # Test subbed_by
    result, error = number.subbed_by(main.Number(3))
    assert result.value == 2
    assert error is None

    # Test multed_by
    result, error = number.multed_by(main.Number(3))
    assert result.value == 15
    assert error is None

    # Test dived_by
    result, error = number.dived_by(main.Number(5))
    assert result.value == 1
    assert error is None

    # Test powed_by
    result, error = number.powed_by(main.Number(2))
    assert result.value == 25
    assert error is None

    # Test get_comparison_eq
    result, error = number.get_comparison_eq(main.Number(5))
    assert result.value == 1
    assert error is None

    # Test get_comparison_ne
    result, error = number.get_comparison_ne(main.Number(5))
    assert result.value == 0
    assert error is None

    # Test get_comparison_lt
    result, error = number.get_comparison_lt(main.Number(5))
    assert result.value == 0
    assert error is None

    # Test get_comparison_gt
    result, error = number.get_comparison_gt(main.Number(5))
    assert result.value == 0
    assert error is None

    # Test get_comparison_lte
    result, error = number.get_comparison_lte(main.Number(5))
    assert result.value == 1
    assert error is None

    # Test get_comparison_gte
    result, error = number.get_comparison_gte(main.Number(5))
    assert result.value == 1
    assert error is None

    # Test anded_by
    result, error = number.anded_by(main.Number(1))
    assert result.value == 1
    assert error is None

    # Test ored_by
    result, error = number.ored_by(main.Number(0))
    assert result.value == 5
    assert error is None

    # Test notted
    result, error = number.notted()
    assert result.value == 0
    assert error is None

    # Test copy
    copy = number.copy()
    assert copy.value == number.value
    assert copy.pos_start == number.pos_start
    assert copy.pos_end == number.pos_end
    assert copy.context == number.context

    # Test is_true
    assert number.is_true()

    # Test illegal_operation
    result, error = number.added_to('other')
    assert result is None
    assert isinstance(error, main.RTError)


def test_string():
    # Create a String instance
    string = main.String("test")

    # Test __str__ and __repr__
    assert str(string) == 'test'
    assert repr(string) == '"test"'

    # Test added_to
    result, error = string.added_to(main.String("ing"))
    assert result.value == "testing"
    assert error is None

    # Test multed_by
    result, error = string.multed_by(main.Number(3))
    assert result.value == "testtesttest"
    assert error is None

    # Test is_true
    assert string.is_true()

    # Test copy
    copy = string.copy()
    assert copy.value == string.value
    assert copy.pos_start == string.pos_start
    assert copy.pos_end == string.pos_end
    assert copy.context == string.context

    # Test illegal_operation
    result, error = string.added_to('other')
    assert result is None
    assert isinstance(error, main.RTError)


# def test_list():
#     # Test initialization
#     elements = [main.Number(1), main.Number(2), main.Number(3)]
#     l = main.List(elements)
#     assert l.elements == elements
#
#     # Test setting position
#     l.set_pos(main.Position(1, 1, 1,fn="file_name", ftxt="file_text"), main.Position(1, 5, 5,fn="file_name", ftxt="file_text"))
#     assert l.pos_start == main.Position(1, 1, 1, fn="file_name", ftxt="file_text")
#     assert l.pos_end == main.Position(1, 5, 5,fn="file_name", ftxt="file_text")
#
#     # Test setting context
#     l.set_context("Test Context")
#     assert l.context == "Test Context"
#
#     # Test added_to method
#     new_element = main.Number(4)
#     result, error = l.added_to(new_element)
#     assert error is None
#     assert len(result.elements) == len(elements) + 1
#     assert result.elements[-1] == new_element
#
#     # Test subbed_by method
#     result, error = l.subbed_by(main.Number(1))  # Remove the element at index 1
#     assert error is None
#     assert len(result.elements) == len(elements) - 1  # Check if the length of the list has decreased by 1
#     assert [element.value for element in result.elements] == [1, 3]
#
#     # Test multed_by method with a Number
#     result, error = l.multed_by(main.Number(2))
#     assert error is None
#     assert len(result.elements) == len(elements) * 2
#     assert [element.value for element in result.elements] == [element.value for element in elements] * 2
#
#
#     # # Test multed_by method with another List
#     # other_elements = [main.Number(5), main.Number(6)]
#     # other_list = main.List(other_elements)
#     # result, error = l.multed_by(other_list)
#     # assert error is None
#     # assert len(result.elements) == len(elements) * len(other_elements)
#     # expected_elements = elements.copy()
#     # expected_elements += [element for _ in elements for element in other_elements]
#     #
#     # assert result.elements == expected_elements
#
#     # Test dived_by method
#     result, error = l.dived_by(main.Number(2))
#     assert error is None
#     assert result == elements[2]
#
#     # Test execute method
#     index = main.Number(1)
#     result, error = l.execute([index])
#     assert error is None
#     assert result == elements[index.value]
#
#     # Test execute method with invalid index
#     index = main.Number(10)
#     result, error = l.execute([index])
#     assert error.error_name == "Runtime Error"
#     assert error.details == "Element at this index could not be retrieved from list because index is out of bounds"

def test_list_methods():
    list = main.List([1, 2, 3, 4, 5])

    # Test added_to method
    other = main.Number(6)
    new_list, error = list.added_to(other)
    # assert new_list.elements == [1, 2, 3, 4, 5, 6], "Test for added_to method failed"
    # assert error is None, "Test for added_to method failed"
    assert new_list.elements == [1, 2, 3, 4, 5,
                                 6], f"Test for added_to method failed: {new_list.elements} (types: {[type(el) for el in new_list.elements]}) != {[1, 2, 3, 4, 5, 6]} (types: {[type(el) for el in [1, 2, 3, 4, 5, 6]]})"

    # Test subbed_by method
    other = main.Number(1)
    new_list, error = list.subbed_by(other)
    assert new_list.elements == [1, 3, 4, 5], "Test for subbed_by method failed"
    assert error is None, "Test for subbed_by method failed"

    # Test multed_by method
    other = main.Number(2)
    new_list, error = list.multed_by(other)
    assert new_list.elements == [1, 2, 3, 4, 5, 1, 2, 3, 4, 5], "Test for multed_by method failed"
    assert error is None, "Test for multed_by method failed"

    # Test dived_by method
    other = main.Number(2)
    result, error = list.dived_by(other)
    assert result == 3, "Test for dived_by method failed"
    assert error is None, "Test for dived_by method failed"

    # Test copy method
    copy = list.copy()
    assert copy.elements == [1, 2, 3, 4, 5], "Test for copy method failed"


def test_base_function_methods():
    parent_context = main.Context("<module>")
    parent_context.symbol_table = main.SymbolTable()
    base_func = main.BaseFunction("test_func")
    base_func.context = parent_context

    # Test generate_new_context method
    new_context = base_func.generate_new_context()
    assert isinstance(new_context, main.Context), "Test for generate_new_context method failed"
    assert isinstance(new_context.symbol_table, main.SymbolTable), "Test for generate_new_context method failed"

    # Test check_args method
    res = base_func.check_args(["arg1", "arg2"], [main.Value(), main.Value()])
    assert res.success is not None, "Test for check_args method failed"

    # Test populate_args method
    exec_ctx = base_func.generate_new_context()
    base_func.populate_args(["arg1", "arg2"], [main.Value(), main.Value()], exec_ctx)
    assert "arg1" in exec_ctx.symbol_table.symbols, "Test for populate_args method failed"
    assert "arg2" in exec_ctx.symbol_table.symbols, "Test for populate_args method failed"

    # Test check_and_populate_args method
    res = base_func.check_and_populate_args(["arg1", "arg2"], [main.Value(), main.Value()], exec_ctx)
    assert res.success is not None, "Test for check_and_populate_args method failed"
    assert "arg1" in exec_ctx.symbol_table.symbols, "Test for check_and_populate_args method failed"
    assert "arg2" in exec_ctx.symbol_table.symbols, "Test for check_and_populate_args method failed"


def test_function_methods():
    parent_context = main.Context("<module>")
    parent_context.symbol_table = main.SymbolTable()
    base_func = main.BaseFunction("test_func")
    base_func.context = parent_context

    # create a numbernode instance
    number_token = main.Token(main.TT_INT, 123)
    body_node = main.NumberNode(number_token)

    # Create a Function instance
    func = main.Function(
        name="test_func", 
        body_node=body_node, arg_names=["arg1", "arg2"],
        arg_types=["str", "str"],
        return_type=False, 
        should_auto_return=False)
        
    func.context = parent_context
    # Test execute method
    args = [main.Value(), main.Value()]
    res = func.execute(args)
    assert isinstance(res, main.RTResult), "Test for execute method failed"
    assert isinstance(res.value, main.Number), "Test for execute method failed"
    assert res.value.value == 123, "Test for execute method failed"

    # Test copy method
    copy = func.copy()
    assert copy.name == func.name, "Test for copy method failed"
    assert copy.arg_names == func.arg_names, "Test for copy method failed"
    assert copy.should_auto_return == func.should_auto_return, "Test for copy method failed"

