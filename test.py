import re

digitalT_std = {
    (
        "before { top: 0; left: 0; right: 0; height: 1px; } ",
        "after { top: 0; right: 0; bottom: 0; width: 1px; } ",
        "em:before { right: 0; bottom: 0; left: 0; height: 1px; } ",
        "em:after { top: 0; bottom: 0; left: 0; width: 1px; } ",
    ): "T1",
    (
        "before { top: 0; left: 0; right: 0; height: 1px; } ",
        "em:before { right: 0; bottom: 0; left: 0; height: 1px; } ",
        "em:after { top: 0; bottom: 0; left: 0; width: 1px; } ",
    ): "T2",
    (
        "before { top: 0; left: 0; right: 0; height: 1px; } ",
        "after { top: 0; right: 0; bottom: 0; width: 1px; } ",
    ): "T3",
    (
        "after { top: 0; right: 0; bottom: 0; width: 1px; } ",
        "em:before { right: 0; bottom: 0; left: 0; height: 1px; } ",
        "em:after { top: 0; bottom: 0; left: 0; width: 1px; } ",
    ): "T4",
    ("after { right: 2px; bottom: 0; width: 2px; height: 2px; } ",): "T5",
    ("em:after { top: 0; bottom: 0; left: 0; width: 1px; } ",): "T6",
    ("after { top: 0; right: 0; bottom: 0; width: 1px; } ",): "T7",
    (
        "before { top: 0; left: 0; right: 0; height: 1px; } ",
        "em:after { top: 0; bottom: 0; left: 0; width: 1px; } ",
    ): "T8",
    (
        "em:after { top: 0; bottom: 0; left: 0; width: 1px; } ",
        "after { top: 0; right: 0; bottom: 0; width: 1px; } ",
    ): "T9",
    (
        "before { top: 0; left: 0; right: 0; height: 1px; } ",
        "after { top: 0; right: 0; bottom: 0; width: 1px; } ",
        "em:after { top: 0; bottom: 0; left: 0; width: 1px; } ",
    ): "T10",
    (
        "before { top: 0; left: 0; right: 0; height: 1px; } ",
        "after { top: 0; right: 0; bottom: 0; width: 1px; } ",
        "em:before { right: 0; bottom: 0; left: 0; height: 1px; }",
    ): "T11",
}


# 긁어온 것 - driver.find_element(By.XPATH, "/html/body/style").get_attribute("innerHTML")
digitalT_scrape = ".digitalT .HIOL:before { top: 0; left: 0; right: 0; height: 1px; } .digitalT .HIOL:after { top: 0; right: 0; bottom: 0; width: 1px; } .digitalT .HIOL em:before { right: 0; bottom: 0; left: 0; height: 1px; } .digitalT .HIOL em:after { top: 0; bottom: 0; left: 0; width: 1px; } .digitalT .HJKP:before { top: 0; left: 0; right: 0; height: 1px; } .digitalT .HJKP em:before { right: 0; bottom: 0; left: 0; height: 1px; } .digitalT .HJKP em:after { top: 0; bottom: 0; left: 0; width: 1px; } .digitalT .HJOP:before { top: 0; left: 0; right: 0; height: 1px; } .digitalT .HJOP:after { top: 0; right: 0; bottom: 0; width: 1px; } .digitalT .HJOL:after { top: 0; right: 0; bottom: 0; width: 1px; } .digitalT .HJOL em:before { right: 0; bottom: 0; left: 0; height: 1px; } .digitalT .HJOL em:after { top: 0; bottom: 0; left: 0; width: 1px; } .digitalT .HIKL:after { right: 2px; bottom: 0; width: 2px; height: 2px; } .digitalT .HJKL em:after { top: 0; bottom: 0; left: 0; width: 1px; } .digitalT .UJKL:after { top: 0; right: 0; bottom: 0; width: 1px; } .digitalT .VBNM:before { top: 0; left: 0; right: 0; height: 1px; } .digitalT .VBNM em:after { top: 0; bottom: 0; left: 0; width: 1px; } .digitalT .UIOL em:after { top: 0; bottom: 0; left: 0; width: 1px; } .digitalT .UIOL:after { top: 0; right: 0; bottom: 0; width: 1px; } .digitalT .UIOP:before { top: 0; left: 0; right: 0; height: 1px; } .digitalT .UIOP:after { top: 0; right: 0; bottom: 0; width: 1px; } .digitalT .UIOP em:after { top: 0; bottom: 0; left: 0; width: 1px; } .digitalT .UJOL:before { top: 0; left: 0; right: 0; height: 1px; } .digitalT .UJOL:after { top: 0; right: 0; bottom: 0; width: 1px; } .digitalT .UJOL em:before { right: 0; bottom: 0; left: 0; height: 1px; }"

# 전처리
css_info = [
    re.split("\s|:", item[2:], 1)
    for item in digitalT_scrape.split(".digitalT")
    if item != ""
]
key, val = map(list, zip(*css_info))
css_dict = {}
for i in range(0, len(key) - 1):
    if key[i] != key[i + 1]:
        css_dict[key[i]] = ()
css_dict[key[len(key) - 1]] = ()
for i in range(0, len(key)):
    css_dict[key[i]] += (val[i],)
# css_dict = {y: x for x, y in css_dict.items()} -- 변환 용도 (사용 금지)

# main.py 91번 줄의 list 내의 각 class_name에 대하여 -> css 정보로 변환 -> 다시 Tx 표준형으로 변환 -> 해당되는 것으로 변환
try:
    class_id = digitalT_std[css_dict[class_name]]
except:  # 아무것도 없는 거는 애초에 CSS 정의가 안 되어있음
    class_id = "*"

digits_digitalT = {
    ("T1", "T1"): "1",
    ("T7", "T4"): "2",
    ("T7", "T3"): "3",
    ("T6", "T7"): "4",
    ("T9", "T3"): "5",
    ("T5", "T8"): "6",
    ("T7", "T1"): "7",
    ("T10", "T8"): "8",
    ("T10", "T7"): "9",
    ("T10", "T11"): "0",
    ("*", "T2"): ".",
}


def digit_to_int(classes: list) -> float:
    length = len(classes) // 2
    num = ""
    dictionary = digits_digitalT

    for item in zip(classes[:length], classes[length:]):
        num += dictionary[item]
    return float(num)


print(digit_to_int(classes))
