def add(a: int, b: int) -> int:
    """두 정수 a와 b를 더합니다."""
    return a + b

def multiply(a: float, b: float) -> float:
    """두 수 a와 b를 곱합니다."""
    return a * b

def divide(a: float, b: float) -> float:
    """a를 0이 아닌 b로 나눕니다."""
    if b == 0:
        raise ValueError('0으로 나눌 수 없습니다.')
    return a / b

TOOLS = [add, multiply, divide]
