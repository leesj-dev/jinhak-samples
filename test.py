UJOP = (
    "after { top: 0; righ...h: 1px; } ",
    "em:before { right: 0...t: 1px; } ",
    "em:after { top: 0; b...th: 1px; }",
)

HJKP = (
    "before { top: 0; lef...t: 1px; } ",
    "after { top: 0; righ...h: 1px; } ",
    "em:before { right: 0...t: 1px; } ",
)

T4 = (
    "after { top: 0; right: 0; bottom: 0; width: 1px; } ",
    "em:before { right: 0; bottom: 0; left: 0; height: 1px; } ",
    "em:after { top: 0; bottom: 0; left: 0; width: 1px; } ",
)

T11 = (
    "before { top: 0; left: 0; right: 0; height: 1px; } ",
    "after { top: 0; right: 0; bottom: 0; width: 1px; } ",
    "em:before { right: 0; bottom: 0; left: 0; height: 1px; }",
)
print(UJOP == T4)
print(HJKP == T11)
