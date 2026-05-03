from typing import Dict, Any, Optional

def apply_rules(symptoms: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Qat'iy mantiqiy qoidalar (strict rules) asosida aniq va tezkor tashxis qo'yish.
    Agar bemor simptomlari klassik kasallik kartinasiga 100% mos kelsa,
    shu funksiya javob qaytaradi va keyingi murakkab tahlillarga hojat qolmaydi.
    
    Args:
        symptoms (Dict[str, Any]): Bemorning simptomlari lug'ati (bool qiymatlarda).
        
    Returns:
        Optional[Dict[str, Any]]: Agar qoidaga mos kelsa tashxis lug'ati, aks holda None.
    """
    
    # 1. CANDIDIASIS (Og'iz bo'shlig'i kandidozi)
    if symptoms.get("white_patch", False) and symptoms.get("removable", False):
        return {
            "diagnosis": "Oral kandidiaz",
            "confidence": 0.9,
            "reason": "Oq qatlam artib tushmoqda — kandidiaz ehtimoli yuqori"
        }
        
    # 2. HERPETIC STOMATITIS (Gerpetik stomatit)
    if symptoms.get("blisters", False) and symptoms.get("fever", False):
        return {
            "diagnosis": "Gerpetik stomatit",
            "confidence": 0.9,
            "reason": "Pufakchalar va isitma mavjud — gerpetik stomatit ehtimoli yuqori"
        }
        
    # 3. ACUTE PULPITIS (O'tkir pulpit)
    if symptoms.get("spontaneous_pain", False) and symptoms.get("night_pain", False):
        return {
            "diagnosis": "O'tkir pulpit",
            "confidence": 0.9,
            "reason": "Spontan va tunda kuchayuvchi og‘riq — pulpit ehtimoli yuqori"
        }
        
    # 4. PERIODONTITIS (Periodontit)
    # Eslatma: Ushbu belgi o'rtacha ishonchlilikka (Medium -> 0.85) ega
    if symptoms.get("percussion_pain", False):
        return {
            "diagnosis": "Periodontit",
            "confidence": 0.85,
            "reason": "Tishga bosganda og‘riq — periodontit ehtimoli yuqori"
        }
        
    # Agar hech qaysi qat'iy qoida mos kelmasa
    return None
