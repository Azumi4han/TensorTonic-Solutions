import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    
    sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    return float(np.nan_to_num(sim, nan=0.0))