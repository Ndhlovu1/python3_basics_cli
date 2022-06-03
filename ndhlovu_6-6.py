fav_lang = {
    'jen':'python',
    'Julia':'C',
    'ken':'Java',
    'jeni':'C++',
}

candidates = ['jen','ken','tino','oscar','phoenix']

for candidate in candidates:
    if candidate in fav_lang:
        print(f"{candidate} Thank you for taking the poll!")
    else:
        print(f"{candidate} please take the favourite language poll")
