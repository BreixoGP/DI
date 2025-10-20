
from operaciones import suma, resta, multiplicación, división

def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    while True:
        print("\n=== Calculadora ===")
        num1 = pedir_numero("Introduce el primer número: ")
        num2 = pedir_numero("Introduce el segundo número: ")

        print("\nElige una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")

        opcion = input("Opción (1/2/3/4): ")

        if opcion == "1":
            resultado = suma(num1, num2)
        elif opcion == "2":
            resultado = resta(num1, num2)
        elif opcion == "3":
            resultado = multiplicación(num1, num2)
        elif opcion == "4":
            resultado = división(num1, num2)
        else:
            print("Opción no válida.")
            continue

        print(f"\nResultado: {resultado}")

        continuar = input("\n¿Quieres hacer otra operación? (s/n): ").lower()
        if continuar != "s":
            print("¡Hasta luego!")
            break


