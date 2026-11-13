import requests

def get_currency_rates():
    url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        print("\n=== O'ZBEKISTON RESPUBLIKASI MARKAZIY BANKI ===")
        
        target_currencies = ['USD', 'EUR', 'RUB']
        rates = {}
        
        for item in data:
            code = item.get('Ccy')
            if code in target_currencies:
                rate = float(item.get('Rate', 0))
                title = item.get('CcyNm_UZ', code)
                rates[code] = rate
                print(f"{title} ({code}): {rate} so'm")
                
        print("----------------------------------------------")
        
        if not rates:
            print("Xato: Valyuta ma'lumotlari topilmadi.")
            return

        # Foydalanuvchidan miqdor kiritishni so'rash
        user_input = input("Konvertatsiya qilish uchun so'm miqdorini kiriting: ")
        amount_uzs = float(user_input)
        
        print("\nNatija:")
        if 'USD' in rates:
            print(f"💵 {amount_uzs:,.2f} so'm = {amount_uzs / rates['USD']:.2f} USD")
        if 'EUR' in rates:
            print(f"💶 {amount_uzs:,.2f} so'm = {amount_uzs / rates['EUR']:.2f} EUR")
        if 'RUB' in rates:
            print(f"🇷🇺 {amount_uzs:,.2f} so'm = {amount_uzs / rates['RUB']:.2f} RUB")

    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

if __name__ == "__main__":
    get_currency_rates()

