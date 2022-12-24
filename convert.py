digital_std = {
    ("before { top: 0; left: 0; right: 0; height: 1px; }", "after { top: 0; right: 0; bottom: 0; width: 1px; }"): "S1",
    ("before { top: 0; left: 0; right: 0; height: 1px;}", "after { top: 0; right: 0; bottom: 0; width: 1px; }", "em:after { top: 0; bottom: 0; left: 0; width: 1px; }"): "S2",
    ("after { top: 0; right: 0; bottom: 0; width: 1px; }", "em:before { right: 0; bottom: 0; left: 0; height: 1px; }"): "S3",
    ("after { right: 2px; bottom: 0; width: 2px; height: 2px;}",): "S4",
    ("em:before { right: 0; bottom: 0; left: 0; height: 1px; }", "em:after { top: 0; bottom: 0; left: 0; width: 1px;}"): "S5",
    ("before { top: 0; left: 0; right: 0; height: 1px; }", "em:before { right: 0; bottom: 0; left: 0; height: 1px; }", "em:after { top: 0; bottom: 0; left: 0; width: 1px;}"): "S6",
    ("before { top: 0; left: 0; right: 0; height: 1px;}", "after { top: 0; right: 0; bottom: 0; width: 1px; }", "em:before { right: 0; bottom: 0; left: 0; height: 1px; }"): "S7",
    ("before { top: 0; left: 0; right: 0; height: 1px; }", "after { top: 0; right: 0; bottom: 0; width: 1px; }", "em:before { right: 0; bottom: 0; left: 0; height: 1px; }", "em:after { top: 0; bottom: 0; left: 0; width: 1px;}"): "S8",
    ("after { top: 0; right: 0; bottom: 0; width: 1px;}", "em:before { right: 0; bottom: 0; left: 0; height: 1px; }", "em:after { top: 0; bottom: 0; left: 0; width: 1px; }"): "S9",
    ("after { top: 0; right: 0; bottom: 0; width: 1px;}",): "S10",
}

digits_digital = {
    ("S10", "S10"): "1",
    ("S7", "S5"): "2",
    ("S7", "S3"): "3",
    ("S9", "S10"): "4",
    ("S6", "S3"): "5",
    ("S5", "S9"): "6",
    ("S1", "S10"): "7",
    ("S8", "S9"): "8",
    ("S8", "S10"): "9",
    ("S2", "S9"): "0",
    ("*", "S4"): ".",
}

digitalT_std = {
    ("before { top: 0; left: 0; right: 0; height: 1px; }", "after { top: 0; right: 0; bottom: 0; width: 1px; }", "em:before { right: 0; bottom: 0; left: 0; height: 1px; }", "em:after { top: 0; bottom: 0; left: 0; width: 1px; }"): "T1",
    ("before { top: 0; left: 0; right: 0; height: 1px; }", "em:before { right: 0; bottom: 0; left: 0; height: 1px; }", "em:after { top: 0; bottom: 0; left: 0; width: 1px; }"): "T2",
    ("before { top: 0; left: 0; right: 0; height: 1px; }", "after { top: 0; right: 0; bottom: 0; width: 1px; }"): "T3",
    ("after { top: 0; right: 0; bottom: 0; width: 1px; }", "em:before { right: 0; bottom: 0; left: 0; height: 1px; }", "em:after { top: 0; bottom: 0; left: 0; width: 1px; }"): "T4",
    ("after { right: 2px; bottom: 0; width: 2px; height: 2px; }",): "T5",
    ("em:after { top: 0; bottom: 0; left: 0; width: 1px; }",): "T6",
    ("after { top: 0; right: 0; bottom: 0; width: 1px; }",): "T7",
    ("before { top: 0; left: 0; right: 0; height: 1px; }", "em:after { top: 0; bottom: 0; left: 0; width: 1px; }"): "T8",
    ("em:after { top: 0; bottom: 0; left: 0; width: 1px; }", "after { top: 0; right: 0; bottom: 0; width: 1px; }"): "T9",
    ("before { top: 0; left: 0; right: 0; height: 1px; }", "after { top: 0; right: 0; bottom: 0; width: 1px; }", "em:after { top: 0; bottom: 0; left: 0; width: 1px; }"): "T10",
    ("before { top: 0; left: 0; right: 0; height: 1px; }", "after { top: 0; right: 0; bottom: 0; width: 1px; }", "em:before { right: 0; bottom: 0; left: 0; height: 1px; }"): "T11",
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

digitalM_std = {
    ("after { top: 50%; right: 0; bottom: 0; width: 1px; }", "em:after { top: 0; bottom: 0; left: 0; width: 1px; }", "em:before { right: 0; bottom: 35%; left: 0; height: 1px; }"): "M1",
    ("before { top: 0; left: 0; right: 0; height: 1px; }", "after { top: 0; right: 0; bottom: 0; width: 1px; }", "em:after { top: 0; bottom: 0; left: 0; width: 1px; }"): "M2",
    ("after { top: 0; right: 0; bottom: 50%; width: 1px; }", "em:after { top: 50%; bottom: 0%; left: 0; width: 1px; }", "em:before { right: 0; bottom: 35%; left: 0; height: 1px; }"): "M3",
    ("after { top: 0; right: 0; bottom: 0; width: 1px; }", "em:before { right: 0; bottom: 35%; left: 0; height: 1px; }"): "M4",
    ("after { top: 0; right: 0; bottom: 0; width: 1px; }", "em:before { right: 0; bottom: 0; left: 0; height: 1px; }", "em:after { top: 0; bottom: 0; left: 0; width: 1px; }"): "M5",
    ("after { right: 2px; bottom: 0; width: 2px; height: 2px; }",): "M6",
    ("em:after { top: 0; bottom: 0; left: 0; width: 1px; }",): "M7",
    ("after { top: 50%; right: 0; bottom: 0; width: 1px; }", "em:after { top: 0; bottom: 50%; left: 0; width: 1px; }", "em:before { right: 0; bottom: 35%; left: 0; height: 1px; }"): "M8",
    ("before { top: 0; left: 0; right: 0; height: 1px; }", "em:after { top: 0; bottom: 0; left: 0; width: 1px; }"): "M9",
    ("after { top: 0; right: 0; bottom: 0; width: 1px; }", "em:after { top: 0; bottom: 0; left: 0; width: 1px; }", "em:before { right: 0; bottom: 35%; left: 0; height: 1px; }"): "M10",
    ("after { top: 0; right: 0; bottom: 0; width: 1px; }",): "M11",
    ("after { top: 0; right: 0; bottom: 0; width: 1px; }", "em:after { top: 0; bottom: 50%; left: 0; width: 1px; }", "em:before { right: 0; bottom: 35%; left: 0; height: 1px; }"): "M12",
    ("after { top: 0; right: 0; bottom: 0; width: 1px; }", "em:before { right: 0; bottom: 0; left: 0; height: 1px; }"): "M13",
    ("em:before { right: 0; bottom: 0; left: 0; height: 1px; }", "em:after { top: 0; bottom: 0; left: 0; width: 1px; }"): "M14",
    ("before { top: 0; left: 0; right: 0; height: 1px; }", "after { top: 0; right: 0; bottom: 0; width: 1px; }"): "M15",
    ("after { top: 0; right: 0; bottom: 0; width: 1px; }", "em:after { top: 0; bottom: 0; left: 0; width: 1px; }"): "M16",
}

digits_digitalM = {
    ("M11", "M11", "M11"): "1",
    ("M15", "M3", "M14"): "2",
    ("M15", "M4", "M13"): "3",
    ("M16", "M12", "M11"): "4",
    ("M9", "M8", "M13"): "5",
    ("M7", "M1", "M5"): "6",
    ("M15", "M11", "M11"): "7",
    ("M2", "M10", "M5"): "8",
    ("M2", "M12", "M11"): "9",
    ("M2", "M16", "M5"): "0",
    ("*", "*", "M6"): ".",
}

digital_dict = {
    "digital": [digital_std, digits_digital, 2],
    "digitalT": [digitalT_std, digits_digitalT, 2],
    "digitalM": [digitalM_std, digits_digitalM, 3],
}
