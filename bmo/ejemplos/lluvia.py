def merge_sort(cards):
    if len(cards) > 1:
        mid = len(cards) // 2
        left_half = cards[:mid]
        right_half = cards[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                cards[k] = left_half[i]
                i += 1
            else:
                cards[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            cards[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            cards[k] = right_half[j]
            j += 1
            k += 1

def main():
    # Una baraja española tiene 48 cartas
    spanish_deck = list(range(1, 13)) * 4  # Cada número se repite 4 veces
    print("Lista de cartas sin ordenar:")
    print(spanish_deck)
    merge_sort(spanish_deck)

    # Mostrar la baraja ordenada
    print("Baraja de cartas española ordenada:")
    for card in spanish_deck:
        print(card, end=" ")
    print()

if __name__ == '__main__':
    main()