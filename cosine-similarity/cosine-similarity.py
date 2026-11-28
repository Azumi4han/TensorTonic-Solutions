import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)

    # Avoiding dividing by 0
    if not a.any():
        return 0
    
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))