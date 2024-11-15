def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
        raise ValueError("The length of the height and weight lists must be the same")
    
    if not all(isinstance(h, (int, float)) for h in height):
        raise ValueError("The height list must contain only integers or floats")
    
    if not all(isinstance(w, (int, float)) for w in weight):
        raise ValueError("The weight list must contain only integers or floats")
    
    bmi = []
    
    for h, w in zip(height, weight):
        if h <= 0 or w <= 0:
            raise ValueError("The height and weight must be greater than 0")
        
        bmi.append(w / (h ** 2))
       
    return bmi

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if len(bmi) == 0:
        raise ValueError("The BMI list must not be empty")
    
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise ValueError("The BMI list must contain only integers or floats")
    
    if not isinstance(limit, int):
        raise ValueError("The limit must be an integer")
    
    return [b > limit for b in bmi]