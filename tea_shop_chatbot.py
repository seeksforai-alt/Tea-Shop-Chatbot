"""
===============================================================
  ☕  Manzoor Ahmad's Tea Shop Chatbot  ☕
  Assignment No 2 - Chatbot Based on Father's Profession
  Father's Name : Manzoor Ahmad
  Profession    : Tea Shop Owner
===============================================================
"""

import random
import sys

# ─────────────────────────────────────────────
#  TEA SHOP DATA
# ─────────────────────────────────────────────

SHOP_INFO = {
    "owner"       : "Manzoor Ahmad",
    "shop_name"   : "Manzoor Ahmad Tea House",
    "location"    : "Mailsi, Punjab, Pakistan",
    "opening_time": "6:00 AM",
    "closing_time": "11:00 PM",
    "specialty"   : "Doodh Patti (Milk Tea)",
}

MENU = {
    # Hot Drinks
    "doodh patti"        : {"price": 48,  "type": "hot",  "desc": "Classic Pakistani milk tea, strong & creamy"},
    "karak chai"         : {"price": 56,  "type": "hot",  "desc": "Extra-strong tea with condensed milk"},
    "green tea"          : {"price": 40,  "type": "hot",  "desc": "Light & refreshing green tea"},
    "kahwa"              : {"price": 64,  "type": "hot",  "desc": "Traditional green tea with cardamom & saffron"},
    "masala chai"        : {"price": 56,  "type": "hot",  "desc": "Spiced tea with ginger, cardamom & cinnamon"},
    "black tea"          : {"price": 32,  "type": "hot",  "desc": "Simple desi black tea with sugar"},
    # Cold Drinks
    "cold coffee"        : {"price": 128,  "type": "cold", "desc": "Chilled coffee with milk & ice"},
    "lassi"              : {"price": 96,  "type": "cold", "desc": "Fresh yoghurt-based drink (sweet or salted)"},
    "lemon soda"         : {"price": 80,  "type": "cold", "desc": "Fresh lemon with chilled soda water"},
    # Snacks / Food
    "rusk"               : {"price": 16,  "type": "snack","desc": "Crispy tea biscuit, perfect with chai"},
    "bun maska"          : {"price": 64,  "type": "snack","desc": "Soft bun with butter – a tea-time classic"},
    "samosa"             : {"price": 32,  "type": "snack","desc": "Crispy fried samosa (aloo or keema)"},
    "paratha"            : {"price": 80,  "type": "snack","desc": "Flaky fried bread, served with chutney"},
    "boiled egg"         : {"price": 40,  "type": "snack","desc": "Simple boiled egg – a desi breakfast staple"},
    "cake slice"         : {"price": 96,  "type": "snack","desc": "Homemade sponge cake, fresh daily"},
}

REQUIRED_ITEMS = {
    "Equipment": [
        "Large Milk Pot (degh)",
        "Gas Burner / Stove",
        "Tea Kettle",
        "Cups & Saucers (ceramic & disposable)",
        "Glass Cups (for karak)",
        "Strainer / Sieve",
        "Spoons & Ladles",
        "Refrigerator (for cold drinks & lassi)",
        "Blender (for cold coffee & lassi)",
        "Cash Box / Register",
        "Display Counter",
        "Dining Tables & Chairs",
        "Signboard",
        "Water Filter",
        "Generator (for load-shedding)",
    ],
    "Raw Materials": [
        "Loose Leaf Tea (Lipton / Tapal)",
        "Full-Cream Milk",
        "Sugar",
        "Cardamom (elaichi)",
        "Ginger (adrak)",
        "Cinnamon sticks",
        "Saffron (for kahwa)",
        "Green Tea Leaves",
        "Coffee Powder",
        "Yoghurt (for lassi)",
        "Lemons",
        "Butter & Bread",
        "Samosa Pastry & Filling",
        "Eggs",
        "Gas Cylinders",
    ],
    "Licenses / Legal": [
        "Trade License from local union council",
        "Health & Hygiene Certificate",
        "FSSAI / Food Safety Registration",
        "NTN (Tax Registration)",
        "Rent Agreement (if rented shop)",
    ],
}

PROMOTIONS = [
    {
        "level"      : "🥉 Small Tea Stall",
        "investment" : "Already achieved!",
        "description": "A basic roadside tea stall – where Manzoor Ahmad started.",
        "income"     : "~10,000 – 20,000 PKR/month",
    },
    {
        "level"      : "🥈 Proper Tea Shop (Current Stage)",
        "investment" : "~50,000 – 1,00,000 PKR",
        "description": "A dedicated shop with seating, proper counter, and full menu.",
        "income"     : "~30,000 – 60,000 PKR/month",
    },
    {
        "level"      : "🥇 Tea Café / Dhaba",
        "investment" : "~2,00,000 – 5,00,000 PKR",
        "description": "Expanded café with printed menu, WiFi, indoor seating, and delivery.",
        "income"     : "~80,000 – 1,50,000 PKR/month",
    },
    {
        "level"      : "🏅 Chain of Tea Shops (2–3 Branches)",
        "investment" : "~10,00,000+ PKR",
        "description": "Multiple branches in Mailsi under the same brand name.",
        "income"     : "~2,50,000 – 5,00,000 PKR/month",
    },
    {
        "level"      : "🏆 Franchise / Brand (Manzoor Tea House)",
        "investment" : "~30,00,000+ PKR",
        "description": "A recognised franchise brand sold to other entrepreneurs across Punjab.",
        "income"     : "Franchise fees + royalties — unlimited potential!",
    },
]

# ─────────────────────────────────────────────
#  HELPER FUNCTIONS
# ─────────────────────────────────────────────

def banner():
    print("\n" + "═" * 62)
    print("   ☕  Welcome to MANZOOR AHMAD'S TEA HOUSE  ☕")
    print("   📍  Mailsi, Punjab, Pakistan")
    print("   🕕  Open: 6:00 AM – 11:00 PM  |  7 Days a Week")
    print("═" * 62)
    print(" Hi! I am the Tea Shop Assistant Chatbot.")
    print(" I can tell you about our menu, shop info, required")
    print(" items, and how Manzoor Ahmad can grow his business!")
    print("═" * 62)
    print(" Type  'help'  to see all commands, or  'exit'  to quit.")
    print("═" * 62 + "\n")


def show_help():
    print("""
┌──────────────────────────────────────────────────────────┐
│                     📋  COMMANDS                         │
├──────────────────────────────────────────────────────────┤
│  menu          - Show the full menu with prices          │
│  hot drinks    - Show only hot beverages                 │
│  cold drinks   - Show only cold beverages                │
│  snacks        - Show all snacks & food items            │
│  order <item>  - Place an order (e.g.  order samosa)     │
│  shop info     - About Manzoor Ahmad's Tea House         │
│  owner         - Info about the owner (my father)        │
│  requirements  - Equipment & materials needed            │
│  promotion     - How the shop can grow (career path)     │
│  special       - Today's special offer                   │
│  help          - Show this menu again                    │
│  exit          - Goodbye!                                │
└──────────────────────────────────────────────────────────┘
""")


def show_menu(filter_type=None):
    type_labels = {"hot": "☕ Hot Drinks", "cold": "🥤 Cold Drinks", "snack": "🍽️  Snacks & Food"}
    current_type = None

    print("\n" + "─" * 50)
    print("       🧾  MANZOOR AHMAD'S TEA HOUSE – MENU")
    print("─" * 50)

    for item, details in MENU.items():
        if filter_type and details["type"] != filter_type:
            continue
        if details["type"] != current_type:
            current_type = details["type"]
            print(f"\n  {type_labels[current_type]}")
            print("  " + "─" * 62)
            print(f"  {'Item Name':<22} {'Price':<10} Description")
            print("  " + "─" * 62)
        print(f"  • {item.title():<22} Rs. {details['price']:<6}  {details['desc']}")

    print("\n" + "─" * 50 + "\n")


def place_order(item_name):
    item_name = item_name.lower().strip()
    if item_name in MENU:
        item   = MENU[item_name]
        thanks = random.choice([
            "Shukriya! Great choice!",
            "Coming right up! ☕",
            "Manzoor sahab will prepare it fresh!",
            "Excellent taste! Won't take long.",
        ])
        print(f"\n  ✅  Order received: {item_name.title()}")
        print(f"  💰  Price : Rs. {item['price']}")
        print(f"  📝  {item['desc']}")
        print(f"  😊  {thanks}\n")
    else:
        print(f"\n  ❌  Sorry, '{item_name}' is not on our menu.")
        print("      Type 'menu' to see what we offer.\n")


def shop_info():
    print(f"""
  ☕  Shop Name  : {SHOP_INFO['shop_name']}
  👤  Owner      : {SHOP_INFO['owner']}
  📍  Location   : {SHOP_INFO['location']}
  🕕  Hours      : {SHOP_INFO['opening_time']} – {SHOP_INFO['closing_time']}
  ⭐  Specialty  : {SHOP_INFO['specialty']}
  💬  Known for friendly service, fresh milk tea, and great taste!
""")


def owner_info():
    print("""
  👨  My Father: Manzoor Ahmad
  ─────────────────────────────────────────
  Manzoor Ahmad is a hardworking tea shop owner based in
  Mailsi, Punjab, Pakistan. He runs his own tea house where
  he serves fresh doodh patti, karak chai, snacks, and more.

  He starts work early at 6:00 AM and serves his customers
  with dedication until 11:00 PM every single day.

  His dream is to expand his tea business into a well-known
  brand across Punjab, and he is already on the right path!
  💪  We are proud of him!
""")


def show_requirements():
    print("\n  🔧  ITEMS REQUIRED TO RUN A TEA SHOP\n")
    for category, items in REQUIRED_ITEMS.items():
        print(f"  📌  {category}:")
        for item in items:
            print(f"       ✔  {item}")
        print()


def show_promotions():
    print("\n  📈  HOW MANZOOR AHMAD CAN GROW HIS BUSINESS\n")
    print("  (Career / Promotion Path for a Tea Shop Owner)\n")
    for i, stage in enumerate(PROMOTIONS, 1):
        print(f"  Stage {i}: {stage['level']}")
        print(f"  💸  Investment   : {stage['investment']}")
        print(f"  📝  Description  : {stage['description']}")
        print(f"  💰  Est. Income  : {stage['income']}")
        print("  " + "─" * 50)
    print()


def todays_special():
    specials = [
        ("Doodh Patti + Rusk Combo", 56, "Save Rs. 5! Perfect morning deal."),
        ("Karak Chai + Samosa", 80, "Extra strong tea with hot samosa!"),
        ("Masala Chai + Bun Maska", 104, "Classic evening snack combo!"),
        ("Cold Coffee + Cake Slice", 192, "Cool treat for hot days!"),
    ]
    name, price, note = random.choice(specials)
    print(f"""
  🌟  TODAY'S SPECIAL OFFER
  ─────────────────────────────────────────
  🍽️   {name}
  💰  Only Rs. {price}
  📢  {note}
  ─────────────────────────────────────────
""")


# ─────────────────────────────────────────────
#  MAIN CHATBOT LOOP
# ─────────────────────────────────────────────

def chatbot():
    banner()

    while True:
        try:
            user_input = input("  You ➜  ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n\n  👋  Shukriya! Thank you for visiting Manzoor Ahmad's Tea House!\n")
            sys.exit(0)

        if not user_input:
            continue

        # ── Exit ──
        if user_input in ("exit", "quit", "bye", "khuda hafiz"):
            print("\n  👋  Shukriya! Thank you for visiting Manzoor Ahmad's Tea House!")
            print("      Do come again! Allah Hafiz 🙏\n")
            break

        # ── Help ──
        elif user_input == "help":
            show_help()

        # ── Full Menu ──
        elif user_input in ("menu", "show menu", "full menu"):
            show_menu()

        # ── Hot Drinks ──
        elif any(k in user_input for k in ("hot drink", "hot tea", "hot chai", "hot beverag")):
            show_menu(filter_type="hot")

        # ── Cold Drinks ──
        elif any(k in user_input for k in ("cold drink", "cold beverag", "iced")):
            show_menu(filter_type="cold")

        # ── Snacks ──
        elif any(k in user_input for k in ("snack", "food", "eat", "khana")):
            show_menu(filter_type="snack")

        # ── Order ──
        elif user_input.startswith("order "):
            item = user_input[6:]
            place_order(item)

        # ── Shop Info ──
        elif any(k in user_input for k in ("shop info", "about shop", "shop detail", "timing", "location", "address")):
            shop_info()

        # ── Owner Info ──
        elif any(k in user_input for k in ("owner", "father", "manzoor", "who runs", "about you")):
            owner_info()

        # ── Requirements ──
        elif any(k in user_input for k in ("requirement", "equipment", "material", "need", "items needed", "tools")):
            show_requirements()

        # ── Promotion / Growth ──
        elif any(k in user_input for k in ("promotion", "growth", "expand", "career", "grow", "future", "business plan")):
            show_promotions()

        # ── Special Offer ──
        elif any(k in user_input for k in ("special", "offer", "deal", "discount", "today")):
            todays_special()

        # ── Price Query ──
        elif "price" in user_input or "cost" in user_input or "kitna" in user_input:
            print("\n  💬  Type 'menu' to see all items with prices,")
            print("      or 'order <item>' to place your order.\n")

        # ── Greetings ──
        elif any(k in user_input for k in ("hi", "hello", "assalam", "salam", "hey")):
            greets = [
                "  Wa Alaikum Assalam! 😊 Welcome to Manzoor Ahmad's Tea House!",
                "  Hello! Welcome! How can I help you today? Type 'help' to begin.",
                "  Assalam o Alaikum! ☕ Come in and enjoy a hot cup of chai!",
            ]
            print("\n" + random.choice(greets) + "\n")

        # ── Thank You ──
        elif any(k in user_input for k in ("thank", "shukriya", "shukria", "jazak")):
            print("\n  😊  You're most welcome! Manzoor Ahmad is happy to serve!\n")

        # ── Unknown ──
        else:
            unknowns = [
                "  🤔  I didn't understand that. Type 'help' to see all commands.",
                "  ❓  Not sure what you mean. Try typing 'menu' or 'help'!",
                "  💬  Please type 'help' to see what I can do for you.",
            ]
            print("\n" + random.choice(unknowns) + "\n")


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    chatbot()
