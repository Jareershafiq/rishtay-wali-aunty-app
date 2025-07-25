# rishtay_aunty.py

def rishtay_wali_aunty(gender):
    profiles = [
        {"name": "Ayesha Khan", "age": 25, "gender": "female", "city": "Lahore", "profession": "Doctor"},
        {"name": "Sara Ali", "age": 27, "gender": "female", "city": "Islamabad", "profession": "Teacher"},
        {"name": "Fatima Noor", "age": 24, "gender": "female", "city": "Karachi", "profession": "Software Engineer"},
        {"name": "Hira Sheikh", "age": 26, "gender": "female", "city": "Rawalpindi", "profession": "Designer"},
        {"name": "Mahnoor Tariq", "age": 29, "gender": "female", "city": "Faisalabad", "profession": "Pharmacist"},
        
        {"name": "Ali Raza", "age": 28, "gender": "male", "city": "Karachi", "profession": "Engineer"},
        {"name": "Bilal Ahmed", "age": 30, "gender": "male", "city": "Lahore", "profession": "Business Analyst"},
        {"name": "Usman Javed", "age": 26, "gender": "male", "city": "Islamabad", "profession": "Banker"},
        {"name": "Hamza Qureshi", "age": 27, "gender": "male", "city": "Multan", "profession": "Civil Engineer"},
        {"name": "Zain Ul Abideen", "age": 29, "gender": "male", "city": "Peshawar", "profession": "Marketing Manager"},
    ]

    print("\n👵 Rishtay Wali Aunty bol rahi hain...\n")

    matched = [p for p in profiles if p["gender"].lower() == gender.lower()]

    if not matched:
        print("Beta, aise koi rishtay nahi hain abhi.")
        return

    for p in matched:
        print(f"👤 {p['name']}, {p['age']} saal ka/ki, {p['profession']} from {p['city']}.")

    print("\n🧕 Allah naseeb achay kare beta. Aunty ki duaen tumhare saath hain.\n")


# ==== Program Start ====

print("🟢 Rishtay Wali Aunty Activated!")
gender_input = input("Beta, kis gender ke rishtay chahiye? (male/female): ")

rishtay_wali_aunty(gender_input)
