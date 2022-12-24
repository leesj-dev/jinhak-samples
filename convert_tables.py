digitalT_std = {
    (
        "before { top: 0; left: 0; right: 0; height: 1px; }",
        "after { top: 0; right: 0; bottom: 0; width: 1px; }",
        "em:before { right: 0; bottom: 0; left: 0; height: 1px; }",
        "em:after { top: 0; bottom: 0; left: 0; width: 1px; }",
    ): "T1",
    (
        "before { top: 0; left: 0; right: 0; height: 1px; }",
        "em:before { right: 0; bottom: 0; left: 0; height: 1px; }",
        "em:after { top: 0; bottom: 0; left: 0; width: 1px; }",
    ): "T2",
    (
        "before { top: 0; left: 0; right: 0; height: 1px; }",
        "after { top: 0; right: 0; bottom: 0; width: 1px; }",
    ): "T3",
    (
        "after { top: 0; right: 0; bottom: 0; width: 1px; }",
        "em:before { right: 0; bottom: 0; left: 0; height: 1px; }",
        "em:after { top: 0; bottom: 0; left: 0; width: 1px; }",
    ): "T4",
    ("after { right: 2px; bottom: 0; width: 2px; height: 2px; }",): "T5",
    ("em:after { top: 0; bottom: 0; left: 0; width: 1px; }",): "T6",
    ("after { top: 0; right: 0; bottom: 0; width: 1px; }",): "T7",
    (
        "before { top: 0; left: 0; right: 0; height: 1px; }",
        "em:after { top: 0; bottom: 0; left: 0; width: 1px; }",
    ): "T8",
    (
        "em:after { top: 0; bottom: 0; left: 0; width: 1px; }",
        "after { top: 0; right: 0; bottom: 0; width: 1px; }",
    ): "T9",
    (
        "before { top: 0; left: 0; right: 0; height: 1px; }",
        "after { top: 0; right: 0; bottom: 0; width: 1px; }",
        "em:after { top: 0; bottom: 0; left: 0; width: 1px; }",
    ): "T10",
    (
        "before { top: 0; left: 0; right: 0; height: 1px; }",
        "after { top: 0; right: 0; bottom: 0; width: 1px; }",
        "em:before { right: 0; bottom: 0; left: 0; height: 1px; }",
    ): "T11",
}

digits_digitalT = {
    ("T7", "T7"): "1",
    ("T3", "T2"): "2",
    ("T3", "T11"): "3",
    ("T9", "T3"): "4",
    ("T8", "T11"): "5",
    ("T6", "T1"): "6",
    ("T3", "T7"): "7",
    ("T10", "T1"): "8",
    ("T10", "T3"): "9",
    ("T10", "T4"): "0",
    ("*", "T5"): ".",
}
