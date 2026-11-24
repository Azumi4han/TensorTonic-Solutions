def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # f(x)=ax^2+bx+c
    # f'(x)=2ax+b
    def d_loss(x: float):
        return 2*a*x+b
    
    for i in range(steps):
        x0 = x0 - lr * d_loss(x0)
        
    return x0