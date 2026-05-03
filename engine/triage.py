from typing import Dict, Any

def get_mucosa_confidence(symptoms: Dict[str, Any]) -> float:
    """
    Shilliq qavat (mucosa) kasalliklari belgilarini tekshirish va ishonchlilikni hisoblash.
    1 ta belgi = 0.85, 2 ta belgi = 0.90, 3 ta belgi = 0.95
    """
    count = sum([
        bool(symptoms.get("ulcer", False)),
        bool(symptoms.get("white_patch", False)),
        bool(symptoms.get("blisters", False))
    ])
    
    if count == 1:
        return 0.85
    elif count == 2:
        return 0.90
    elif count == 3:
        return 0.95
    return 0.0

def get_periodontal_confidence(symptoms: Dict[str, Any]) -> float:
    """
    Periodontal (milk) kasalliklari belgilarini tekshirish va ishonchlilikni hisoblash.
    1 ta belgi = 0.75, 2 ta belgi = 0.85
    """
    count = sum([
        bool(symptoms.get("gum_bleeding", False)),
        bool(symptoms.get("gum_swelling", False))
    ])
    
    if count == 1:
        return 0.75
    elif count >= 2:
        return 0.85
    return 0.0

def is_jaw(symptoms: Dict[str, Any]) -> bool:
    """
    Jag' (jaw) kasalliklari belgilarini tekshirish.
    Shish va isitma bir vaqtda kelishi shart.
    """
    return bool(symptoms.get("swelling", False)) and bool(symptoms.get("fever", False))


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
    mucosa_conf = get_mucosa_confidence(symptoms)
    if mucosa_conf > 0:
        return {
            "category": "mucosa",
            "confidence": mucosa_conf,
            "reason": "Og‘izda yara yoki oq qatlam aniqlangan — shilliq qavat kasalligi ehtimoli yuqori"
        }
        
    # 2. JAW tekshiruvi
    if is_jaw(symptoms):
        return {
            "category": "jaw",
            "confidence": 0.9,
            "reason": "Shish va isitma mavjud — jag‘ kasalligi ehtimoli yuqori"
        }
        
    # 3. PERIODONTAL tekshiruvi
    perio_conf = get_periodontal_confidence(symptoms)
    if perio_conf > 0:
        return {
            "category": "periodontal",
            "confidence": perio_conf,
            "reason": "Milk bilan bog‘liq belgilar mavjud — periodontal kasallik ehtimoli yuqori"
        }
        
    # 4. TOOTH (Qolgan barcha holatlar - Default)
    return {
        "category": "tooth",
        "confidence": 0.6,
        "reason": "Asosiy belgilar tish bilan bog‘liq — tish kasalligi ehtimoli yuqori"
    }
