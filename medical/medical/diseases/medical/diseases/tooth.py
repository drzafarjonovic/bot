from medical.disease_model import Disease

# Chuqur karies (Deep caries)
deep_caries = Disease(
    name="Deep caries",
    category="tooth",
    core_features={"cavity": True, "pain_triggered": True},
    optional_features={"sweet_pain": True},
    negative_features={"spontaneous_pain": True},
    discriminators=[
        "stimulusga bog‘liq og‘riq"
    ],
    red_flags=[
        "spontan og‘riq paydo bo‘lishi"
    ]
)

# O'tkir pulpit (Acute pulpitis)
acute_pulpitis = Disease(
    name="Acute pulpitis",
    category="tooth",
    core_features={"spontaneous_pain": True, "night_pain": True},
    optional_features={"thermal_pain": True},
    negative_features={"percussion_pain": True},
    discriminators=[
        "tunda kuchayadi",
        "spontan og‘riq"
    ],
    red_flags=[
        "og‘riq kuchayib boradi"
    ]
)

# Ushbu fayldagi barcha kasalliklar ro'yxati (Export)
DISEASES = [
    deep_caries,
    acute_pulpitis
]
