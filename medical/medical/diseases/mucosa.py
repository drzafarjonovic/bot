from medical.disease_model import Disease

# Aftoz stomatit (Aphthous stomatitis)
aphthous_stomatitis = Disease(
    name="Aphthous stomatitis",
    category="mucosa",
    core_features={"ulcer": True, "pain": True},
    optional_features={"recurrent": True},
    negative_features={"fever": True},
    discriminators=[
        "og‘riqli yara",
        "oq markaz, qizil halqa",
        "isitmasiz kechadi"
    ],
    red_flags=[
        "2 haftadan ortiq bitmaydi"
    ]
)

# Gerpetik stomatit (Herpetic stomatitis)
herpetic_stomatitis = Disease(
    name="Herpetic stomatitis",
    category="mucosa",
    core_features={"blisters": True, "fever": True},
    optional_features={"multiple": True},
    negative_features={},
    discriminators=[
        "ko‘p pufakchalar",
        "isitma bilan boshlanadi"
    ],
    red_flags=[
        "yuqori isitma",
        "ovqat yeyolmaslik"
    ]
)

# Og'iz bo'shlig'i kandidozi (Oral candidiasis)
oral_candidiasis = Disease(
    name="Oral candidiasis",
    category="mucosa",
    core_features={"white_patch": True},
    optional_features={"burning": True},
    negative_features={},
    discriminators=[
        "oq qatlam artib tushadi"
    ],
    red_flags=[
        "keng tarqalishi"
    ]
)

# Ushbu fayldagi barcha kasalliklar ro'yxati (Export)
DISEASES = [
    aphthous_stomatitis,
    herpetic_stomatitis,
    oral_candidiasis
]
