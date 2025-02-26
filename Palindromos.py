def is_palindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10  # Reducimos el número original

    return x == reversed_half or x == reversed_half // 10

# Bucle para ejecutar varias veces hasta que el usuario quiera salir
if __name__ == "__main__":
    while True:
        try:
            num = int(input("Ingresa un número entero: "))
            if is_palindrome(num):
                print(f"{num} es un palíndromo.")
            else:
                print(f"{num} no es un palíndromo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

        opcion = input("¿Quieres probar otro número? (s para sí, n para salir): ").strip().lower()
        if opcion == 'n':
            print("¡Hasta luego!")
            break
