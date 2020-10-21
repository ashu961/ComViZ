from .Error import Error


class IllegalCharError(Error):
    """
      Raised when Lexer comes accros a char which is not supported by our language
    """

    def __init__(self, err_details):
        super().__init__(err_name="Illegal Character", err_details=err_details)
