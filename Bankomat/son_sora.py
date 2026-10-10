


def son_sora(number ):
    while True:
        try:
            son = input(number).strip()
            if not son:
                raise ValueError("Bo'sh bolmasligi kerak ")
            if not son.isdigit():
                raise ValueError("Faqat son kiritishingiz kerak ")
            son = int(son)
            if son <= 0 :
                raise ValueError("Musbat son bo'lishi kerak! ")
            return son
        except ValueError as e:
            print("Xato", e)

