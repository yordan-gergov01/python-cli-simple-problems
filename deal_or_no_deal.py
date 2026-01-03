import random

SUMS = [
    1, 5, 10, 25, 50, 75, 100, 200, 300, 400,
    500, 750, 1000, 2500, 5000, 10000, 25000, 50000, 75000, 100000
]

def clear_screen():
    print('\n' * 2)

def show_remaining_sums(opened_sums):
    """Показва останалите суми"""
    print("\n╔══════════════════════════════════╗")
    print("║    ОСТАНАЛИ СУМИ В КУТИИТЕ      ║")
    print("╠══════════════════════════════════╣")
    for sum in SUMS:
        if sum in opened_sums:
            print(f"║  {sum:>6} лв  ❌              ║")
        else:
            print(f"║  {sum:>6} лв  ✓              ║")
    print("╚══════════════════════════════════╝\n")

def calculate_offer(remaining_sums, round_num):
    """Изчислява офертата на банкера"""
    avg = sum(remaining_sums) / len(remaining_sums)

    factor = 0.3 + (round_num * 0.1)
    return int(avg * factor)

def play_game():
    print("╔═══════════════════════════════════════╗")
    print("║                                       ║")
    print("║       🎲 СДЕЛКА ИЛИ НЕ 🎲           ║")
    print("║                                       ║")
    print("╚═══════════════════════════════════════╝\n")
    
    boxes = {i: suma for i, suma in enumerate(random.sample(SUMS, len(SUMS)), 1)}
    
    print(f"Има {len(SUMS)} кутии с различни суми пари.")
    while True:
        try:
            my_box = int(input(f"\nИзбери своята кутия (1-{len(SUMS)}): "))
            if 1 <= my_box <= len(SUMS):
                break
            print(f"Моля избери число между 1 и {len(SUMS)}!")
        except:
            print("Моля въведи валидно число!")
    
    my_sum = boxes[my_box]
    remaining_boxes = [b for b in boxes.keys() if b != my_box]
    
    opened_sums = []
    
    print(f"\n✓ Избра си кутия номер {my_box}!")
    print("Нека видим какво има в другите кутии...\n")
    input("Натисни Enter за да продължиш...")
    
    rounds = [6, 5, 4, 3, 2, 1, 1, 1]
    
    round_num = 0
    
    for boxes_to_open in rounds:
        if not remaining_boxes:
            break
            
        round_num += 1
        clear_screen()
        print(f"\n{'='*40}")
        print(f"РУНД {round_num}")
        print(f"{'='*40}")
        
        show_remaining_sums(opened_sums)
        
        print(f"\nТрябва да отвориш {boxes_to_open} кутии.")
        
        for _ in range(min(boxes_to_open, len(remaining_boxes))):
            print(f"\nОстанали кутии: {remaining_boxes}")
            while True:
                try:
                    choice = int(input("Коя кутия да отворим?: "))
                    if choice in remaining_boxes:
                        break
                    print("Тази кутия не е налична!")
                except:
                    print("Моля въведи валидно число!")
            
            opened_sum = boxes[choice]
            remaining_boxes.remove(choice)
            opened_sums.append(opened_sum)
            
            print(f"\n🎁 Кутия {choice} съдържа: {opened_sum} лв")
            
            if opened_sum >= 50000:
                print("😱 Голяма сума излезе от играта!")
            elif opened_sum <= 100:
                print("😊 Малка сума - добре за теб!")
            
            if remaining_boxes:
                input("\nНатисни Enter за следващата кутия...")
        
        if remaining_boxes:
            clear_screen()
            show_remaining_sums(opened_sums)
            
            remaining_sums = [boxes[b] for b in remaining_boxes] + [my_sum]
            offer = calculate_offer(remaining_sums, round_num)
            
            print("\n" + "="*40)
            print("📞 ОБАЖДА СЕ БАНКЕРЪТ!")
            print("="*40)
            print(f"\n💰 ОФЕРТА: {offer} лв\n")
            
            while True:
                decision = input("СДЕЛКА или НЕ? (да/не): ").lower()
                if decision in ['да', 'da', 'yes', 'д', 'd']:
                    print("\n" + "="*40)
                    print("🤝 ПРИЕЛ СИ ОФЕРТАТА!")
                    print("="*40)
                    print(f"\n💵 Печелиш: {offer} лв")
                    print(f"\n📦 В твоята кутия {my_box} имаше: {my_sum} лв")
                    if offer > my_sum:
                        print("\n🎉 Добра сделка! Спечели си повече!")
                    else:
                        print("\n😔 Можеше да спечелиш повече...")
                    return
                elif decision in ['не', 'ne', 'no', 'н', 'n']:
                    print("\n❌ Отказа офертата! Играта продължава...\n")
                    input("Натисни Enter...")
                    break
                else:
                    print("Моля отговори с 'да' или 'не'")
    
    clear_screen()
    print("\n" + "="*40)
    print("🎊 КРАЙ НА ИГРАТА! 🎊")
    print("="*40)
    print(f"\n📦 Отваряме твоята кутия номер {my_box}...")
    input("\nНатисни Enter...")
    print(f"\n🎁🎁🎁 В нея има: {my_sum} лв! 🎁🎁🎁\n")
    print("="*40)

if __name__ == "__main__":
    play_game()
    print("\nБлагодаря за играта! 🎮")