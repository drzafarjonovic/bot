from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Disease:
    """
    Stomatologik kasallikning ma'lumotlar modeli.
    
    Attributes:
        name: Kasallikning nomi.
        category: Kasallik toifasi (masalan, "mucosa", "tooth").
        core_features: Asosiy belgilar (yuqori vaznga ega).
        optional_features: Qo'shimcha, yordamchi belgilar.
        negative_features: Agar ushbu belgilar mavjud bo'lsa, kasallik ehtimolini pasaytiradi.
        discriminators: O'zbek tilidagi klinik ajratuvchi ta'riflar.
        red_flags: Xavfli holatlar (zudlik bilan shifokorga murojaat qilish uchun).
    """
    name: str
    category: str
    core_features: Dict[str, bool]
    optional_features: Dict[str, bool]
    negative_features: Dict[str, bool]
    discriminators: List[str]
    red_flags: List[str]
