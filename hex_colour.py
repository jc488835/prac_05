COLOUR_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
               "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
               "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "	#458b74", "azure1": "#f0ffff"}
code = input("Enter a colour:")
while code != "":
    if code in COLOUR_CODE:
        print(code, "is", COLOUR_CODE[code])
    else:
        print("Invalid colour")
    code = input("Enter a colour:")