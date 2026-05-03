from typing import Dict, Any

def is_mucosa(symptoms: Dict[str, Any]) -> bool:
    """
    Shilliq qavat (mucosa) kasalliklari belgilarini tekshirish.
    Yara, oq qatlam yoki pufakchalar mavjudligini qaraydi.
    """
    return (
        symptoms.get("ulcer", False) or 
        symptoms.get("white_patch", False) or 
        symptoms.get("blisters", False)
    )

def is_jaw(symptoms: Dict[str, Any]) -> bool:
    """
    Jag' (jaw) kasalliklari belgilarini tekshirish.
    Shish va isitma bir vaqtda kelganini qaraydi.
    """
    return (
        symptoms.get("swelling", False) and 
        symptoms.get("fever", False)
    )

def is_periodontal(symptoms: Dict[str, Any]) -> bool:
    """
    Periodontal (milk) kasalliklari belgilarini tekshirish.
    Milk qonashi yoki milk shishishini qaraydi.
    """
    return (
        symptoms.get("gum_bleeding", False) or 
        symptoms.get("gum_swelling", False)
    )

def classify_category(symptoms: Dict[str, Any]) -> Dict[str, Any]:
    """
    Simptomlarga asosan stomatologik kasallik toifasini aniqlaydi.
    
    Qat'iy ustuvorlik (Strict Priority):
    1. MUCOSA (Eng yuqori ustuvorlik)
    2. JAW
    3. PERIODONTAL
    4. TOOTH (Birlamchi - Default)
    
    Args:
        symptoms (Dict[str, Any]): Bemorning simptomlari lug'ati (bool qiymatlarda).
        
    Returns:
        Dict[str, Any]: Kategoriya, ishonchlilik darajasi (confidence) va izoh.
    """
    
    # 1. MUCOSA tekshiruvi (Eng yuqori ustuvorlik)
    if is_mucosa(symptoms):
        return {
            "category": "mucosa",
            "confidence": 0.9,
            "reason": "Og‘izda yara yoki oq qatlam aniqlangan — shilliq qavat kasalligi ehtimoli yuqori"
        }
        
    # 2. JAW tekshiruvi
    elif is_jaw(symptoms):
        return {
            "category": "jaw",
            "confidence": 0.9,
            "reason": "Shish va isitma mavjud — jag‘ kasalligi ehtimoli yuqori"
        }
        
    # 3. PERIODONTAL tekshiruvi
    elif is_periodontal(symptoms):
        return {
            "category": "periodontal",
            "confidence": 0.8,
            "reason": "Milk bilan bog‘liq belgilar mavjud — periodontal kasallik ehtimoli yuqori"
        }
        
    # 4. TOOTH (Qolgan barcha holatlar - Default)
    else:
        return {
            "category": "tooth",
            "confidence": 0.6,
            "reason": "Asosiy belgilar tish bilan bog‘liq — tish kasalligi ehtimoli yuqori"
        }
