"""Arbitrary utils placeholder"""

# Base error classes
class DomainError(Exception):
    """Raised when domain is not valid"""
    def __init__(self, message=None):
        if message:
            super().__init__(f'[Domain Error] {message}')
        else:
            super().__init__('[Domain Error] Differential privacy parameter '
                             'domain is invalid.')


# Derived error classes
class NotNatural(DomainError):
    """Raised when a value is not a natural number"""
    def __init__(self, message=None):
        if message:
            super().__init__(f'[Not Natural] {message}')
        else:
            super().__init__('[Not Natural] Differential privacy parameter '
                             'must be a natural number (i.e. ∈ ℕ).')

class Negative(DomainError):
    """Raised when a value is not a nonnegative number"""
    def __init__(self, message=None):
        if message:
            super().__init__(f'[Negative] {message}')
        else:
            super().__init__('[Negative] Differential privacy parameter '
                             'must be a nonnegative number (i.e. ≥ 0).')

class NotInteger(DomainError):
    """Raised when a value is not an integer"""
    def __init__(self, message=None):
        if message:
            super().__init__(f'[Not Integer] {message}')
        else:
            super().__init__('[Not Integer] Differential privacy parameter '
                             'must be an integer (i.e. ∈ ℤ).')

class Complex(DomainError):
    """Raised when a value is not a real number"""
    def __init__(self, message=None):
        if message:
            super().__init__(f'[Complex] {message}')
        else:
            super().__init__('[Complex] Differential privacy parameter '
                             'must be a real number (i.e. ∈ ℝ).')

class NotScalar(DomainError):
    """Raised when a value is not a scalar"""
    def __init__(self, message=None):
        if message:
            super().__init__(f'[Not Scalar] {message}')
        else:
            super().__init__('[Not Scalar] Differential privacy parameter '
                             'must be a scalar and real (i.e. ∈ ℝ).')
