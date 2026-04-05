import json
import re

new_data_str = '''
[
  {
    "id": "spr1",
    "asset": "zloy.png",
    "x": 956,
    "y": 181,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.096,
    "zIndex": 0
  },
  {
    "id": "spr2",
    "asset": "skilz.png",
    "x": 144,
    "y": 523,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.096,
    "zIndex": 1
  },
  {
    "id": "spr3",
    "asset": "mokr.png",
    "x": 175,
    "y": 152,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.1,
    "zIndex": 2
  },
  {
    "id": "spr4",
    "asset": "gens.png",
    "x": 941,
    "y": 528,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.0953,
    "zIndex": 3
  },
  {
    "id": "spr5",
    "asset": "srart.png",
    "x": 1044,
    "y": 622,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.063,
    "zIndex": 4
  },
  {
    "id": "spr6",
    "asset": "bonus.png",
    "x": 997,
    "y": 615,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.063,
    "zIndex": 5
  },
  {
    "id": "spr7",
    "asset": "gift.png",
    "x": 955,
    "y": 604,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.0583,
    "zIndex": 6
  },
  {
    "id": "spr8",
    "asset": "portal.png",
    "x": 914,
    "y": 591,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.056,
    "zIndex": 7
  },
  {
    "id": "spr9",
    "asset": "portal.png",
    "x": 884,
    "y": 474,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.054,
    "zIndex": 8
  },
  {
    "id": "spr10",
    "asset": "1w.png",
    "x": 919,
    "y": 453,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.05,
    "zIndex": 9
  },
  {
    "id": "spr11",
    "asset": "fish.png",
    "x": 960,
    "y": 442,
    "rotationX": 37,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.048,
    "zIndex": 10
  },
  {
    "id": "spr12",
    "asset": "zadanie.png",
    "x": 997,
    "y": 435,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.052,
    "zIndex": 11
  },
  {
    "id": "spr13",
    "asset": "gift.png",
    "x": 1034,
    "y": 426,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.054,
    "zIndex": 12
  },
  {
    "id": "spr14",
    "asset": "dead.png",
    "x": 1052,
    "y": 399,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.05,
    "zIndex": 13
  },
  {
    "id": "spr15",
    "asset": "bonus.png",
    "x": 1015,
    "y": 388,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.055,
    "zIndex": 14
  },
  {
    "id": "spr16",
    "asset": "bonus.png",
    "x": 977,
    "y": 379,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.054,
    "zIndex": 15
  },
  {
    "id": "spr17",
    "asset": "1w.png",
    "x": 995,
    "y": 350,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.051,
    "zIndex": 16
  },
  {
    "id": "spr18",
    "asset": "zadanie.png",
    "x": 1027,
    "y": 333,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.051,
    "zIndex": 17
  },
  {
    "id": "spr19",
    "asset": "fish.png",
    "x": 991,
    "y": 318,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.042,
    "zIndex": 18
  },
  {
    "id": "spr20",
    "asset": "bonus.png",
    "x": 952,
    "y": 308,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.053,
    "zIndex": 19
  },
  {
    "id": "spr21",
    "asset": "bonus.png",
    "x": 916,
    "y": 293,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.053,
    "zIndex": 20
  },
  {
    "id": "spr22",
    "asset": "save.png",
    "x": 917,
    "y": 233,
    "rotationX": 37,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.054,
    "zIndex": 21
  },
  {
    "id": "spr23",
    "asset": "gift.png",
    "x": 885,
    "y": 221,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.052,
    "zIndex": 22
  },
  {
    "id": "spr24",
    "asset": "zadanie.png",
    "x": 846,
    "y": 226,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.05,
    "zIndex": 24
  },
  {
    "id": "spr25",
    "asset": "1w.png",
    "x": 804,
    "y": 216,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.053,
    "zIndex": 25
  },
  {
    "id": "spr26",
    "asset": "bonus.png",
    "x": 763,
    "y": 213,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.053,
    "zIndex": 27
  },
  {
    "id": "spr27",
    "asset": "bonus.png",
    "x": 727,
    "y": 206,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.053,
    "zIndex": 28
  },
  {
    "id": "spr28",
    "asset": "zadanie.png",
    "x": 694,
    "y": 196,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.043,
    "zIndex": 29
  },
  {
    "id": "spr29",
    "asset": "1w.png",
    "x": 661,
    "y": 181,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.044,
    "zIndex": 30
  },
  {
    "id": "spr30",
    "asset": "gift.png",
    "x": 631,
    "y": 170,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.046,
    "zIndex": 31
  },
  {
    "id": "spr31",
    "asset": "bonus.png",
    "x": 597,
    "y": 161,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.053,
    "zIndex": 32
  },
  {
    "id": "spr32",
    "asset": "bonus.png",
    "x": 560,
    "y": 153,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.053,
    "zIndex": 33
  },
  {
    "id": "spr33",
    "asset": "fish.png",
    "x": 524,
    "y": 145,
    "rotationX": 33,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.04,
    "zIndex": 34
  },
  {
    "id": "spr34",
    "asset": "zadanie.png",
    "x": 487,
    "y": 152,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.048,
    "zIndex": 35
  },
  {
    "id": "spr35",
    "asset": "dead.png",
    "x": 450,
    "y": 149,
    "rotationX": 28,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.05,
    "zIndex": 36
  },
  {
    "id": "spr36",
    "asset": "bonus.png",
    "x": 414,
    "y": 155,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.053,
    "zIndex": 37
  },
  {
    "id": "spr37",
    "asset": "zadanie.png",
    "x": 376,
    "y": 162,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.05,
    "zIndex": 38
  },
  {
    "id": "spr38",
    "asset": "bonus.png",
    "x": 337,
    "y": 166,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.056,
    "zIndex": 39
  },
  {
    "id": "spr39",
    "asset": "gift.png",
    "x": 310,
    "y": 187,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.053,
    "zIndex": 40
  },
  {
    "id": "spr40",
    "asset": "1w.png",
    "x": 272,
    "y": 197,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.056,
    "zIndex": 41
  },
  {
    "id": "spr41",
    "asset": "time.png",
    "x": 233,
    "y": 211,
    "rotationX": 30,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.058,
    "zIndex": 42
  },
  {
    "id": "spr42",
    "asset": "bonus.png",
    "x": 264,
    "y": 241,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.059,
    "zIndex": 44
  },
  {
    "id": "spr43",
    "asset": "bonus.png",
    "x": 291,
    "y": 265,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.059,
    "zIndex": 45
  },
  {
    "id": "spr44",
    "asset": "zadanie.png",
    "x": 328,
    "y": 266,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.051,
    "zIndex": 46
  },
  {
    "id": "spr45",
    "asset": "zadanie.png",
    "x": 366,
    "y": 268,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.051,
    "zIndex": 47
  },
  {
    "id": "spr46",
    "asset": "gift.png",
    "x": 398,
    "y": 287,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.053,
    "zIndex": 48
  },
  {
    "id": "spr47",
    "asset": "1w.png",
    "x": 360,
    "y": 295,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.052,
    "zIndex": 49
  },
  {
    "id": "spr48",
    "asset": "bonus.png",
    "x": 322,
    "y": 316,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.062,
    "zIndex": 50
  },
  {
    "id": "spr49",
    "asset": "bonus.png",
    "x": 362,
    "y": 330,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.062,
    "zIndex": 51
  },
  {
    "id": "spr50",
    "asset": "fish.png",
    "x": 398,
    "y": 347,
    "rotationX": 32,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.047,
    "zIndex": 52
  },
  {
    "id": "spr51",
    "asset": "gift.png",
    "x": 358,
    "y": 369,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.06,
    "zIndex": 53
  },
  {
    "id": "spr52",
    "asset": "zadanie.png",
    "x": 313,
    "y": 376,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.056,
    "zIndex": 54
  },
  {
    "id": "spr53",
    "asset": "dead.png",
    "x": 271,
    "y": 376,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.055,
    "zIndex": 55
  },
  {
    "id": "spr54",
    "asset": "bonus.png",
    "x": 228,
    "y": 382,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.063,
    "zIndex": 56
  },
  {
    "id": "spr55",
    "asset": "bonus.png",
    "x": 199,
    "y": 407,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.063,
    "zIndex": 57
  },
  {
    "id": "spr56",
    "asset": "zadanie.png",
    "x": 236,
    "y": 426,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.056,
    "zIndex": 58
  },
  {
    "id": "spr57",
    "asset": "bonus.png",
    "x": 270,
    "y": 449,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.063,
    "zIndex": 59
  },
  {
    "id": "spr58",
    "asset": "bonus.png",
    "x": 307,
    "y": 467,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.063,
    "zIndex": 60
  },
  {
    "id": "spr59",
    "asset": "gift.png",
    "x": 348,
    "y": 481,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.06,
    "zIndex": 61
  },
  {
    "id": "spr60",
    "asset": "1w.png",
    "x": 395,
    "y": 487,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.06,
    "zIndex": 62
  },
  {
    "id": "spr61",
    "asset": "bonus.png",
    "x": 443,
    "y": 501,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.063,
    "zIndex": 63
  },
  {
    "id": "spr62",
    "asset": "zadanie.png",
    "x": 485,
    "y": 511,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.056,
    "zIndex": 64
  },
  {
    "id": "spr63",
    "asset": "fish.png",
    "x": 526,
    "y": 523,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.047,
    "zIndex": 65
  },
  {
    "id": "spr64",
    "asset": "bonus.png",
    "x": 545,
    "y": 555,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.062,
    "zIndex": 66
  },
  {
    "id": "spr65",
    "asset": "bonus.png",
    "x": 533,
    "y": 587,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.063,
    "zIndex": 67
  },
  {
    "id": "spr66",
    "asset": "gift.png",
    "x": 488,
    "y": 592,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.06,
    "zIndex": 68
  },
  {
    "id": "spr67",
    "asset": "bonus.png",
    "x": 445,
    "y": 577,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.063,
    "zIndex": 69
  },
  {
    "id": "spr68",
    "asset": "zadanie.png",
    "x": 405,
    "y": 562,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.056,
    "zIndex": 70
  },
  {
    "id": "spr69",
    "asset": "bonus.png",
    "x": 368,
    "y": 579,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.063,
    "zIndex": 71
  },
  {
    "id": "spr70",
    "asset": "bonus.png",
    "x": 362,
    "y": 610,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.063,
    "zIndex": 72
  },
  {
    "id": "spr71",
    "asset": "1w.png",
    "x": 354,
    "y": 637,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.06,
    "zIndex": 73
  },
  {
    "id": "spr72",
    "asset": "bonus.png",
    "x": 308,
    "y": 646,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.063,
    "zIndex": 74
  },
  {
    "id": "spr73",
    "asset": "zadanie.png",
    "x": 264,
    "y": 643,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.056,
    "zIndex": 75
  },
  {
    "id": "spr74",
    "asset": "gift.png",
    "x": 222,
    "y": 631,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.06,
    "zIndex": 76
  },
  {
    "id": "spr75",
    "asset": "dog.png",
    "x": 212,
    "y": 589,
    "rotationX": 26,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.06,
    "zIndex": 77
  },
  {
    "id": "spr76",
    "asset": "finish.png",
    "x": 246,
    "y": 560,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.088,
    "zIndex": 78
  },
  {
    "id": "spr77",
    "asset": "doghouse.png",
    "x": 304,
    "y": 512,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.088,
    "zIndex": 79
  },
  {
    "id": "spr78",
    "asset": "island.png",
    "x": 606,
    "y": 380,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.2095,
    "zIndex": 80
  },
  {
    "id": "spr79",
    "asset": "bonus.png",
    "x": 895,
    "y": 268,
    "rotationX": 0,
    "rotationY": 0,
    "rotationZ": 0,
    "scale": 0.056,
    "zIndex": 81
  }
]
'''

new_data = json.loads(new_data_str)
html_code = []

for sprite in new_data:
    line = f'    <img class="placed-sprite" data-id="{sprite["id"]}" src="{sprite["asset"]}" alt="" style="left: {sprite["x"]}px; top: {sprite["y"]}px; transform: translate(-50%, -50%) rotateX({sprite["rotationX"]}deg) rotateY({sprite["rotationY"]}deg) rotateZ({sprite["rotationZ"]}deg) scale({sprite["scale"]}); z-index: {sprite["zIndex"]};" />'
    html_code.append(line)

with open('c:/Users/alksv/OneDrive/Рабочий стол/test4/test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# replace the placed-sprite block
pattern = re.compile(r'(<img class="placed-sprite".*?>\s*)+', re.DOTALL)
match = pattern.search(content)

if match:
    new_content = content[:match.start()] + '\n'.join(html_code) + '\n' + content[match.end():]
    
    # Hide the tool panel
    new_content = new_content.replace('/* .tool-panel,', '.tool-panel,')
    new_content = new_content.replace('    } */', '    }')
    new_content = new_content.replace('    }*/', '    }')
    
    with open('c:/Users/alksv/OneDrive/Рабочий стол/test4/test.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replaced successfully")
else:
    print("Match failed")
