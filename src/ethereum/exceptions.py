"""
Error types common across all Ethereum forks.
"""


class EthereumException(Exception):
    """
    Base class for all exceptions _expected_ to be thrown during normal
    operation.
    """


class InvalidBlock(EthereumException):
    """
    Thrown when a block being processed is found to be invalid.
    """


class InvalidTransaction(EthereumException):
    """
    Thrown when a transaction being processed is found to be invalid.
    """


class RLPDecodingError(EthereumException):
    """
    Indicates that RLP decoding failed.
    """


class RLPEncodingError(EthereumException):
    """
    Indicates that RLP encoding failed.
    """


class InvalidSenderError(InvalidTransaction):
    """
    Thrown when a transaction originates from an account that cannot send
    transactions.
    """
