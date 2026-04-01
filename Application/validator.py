def validate_location(location: str) -> str:
    if not location or not location.strip():
        raise ValueError("Location cannot be empty")
 
    if len(location.strip()) < 2:
        raise ValueError("Location name too short")
 
    return location. Strip()
