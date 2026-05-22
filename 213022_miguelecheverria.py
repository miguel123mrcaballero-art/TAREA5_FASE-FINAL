# ==============================
# MENÚ DE RESTAURANTE
# ==============================

# Matriz de productos
# [Nombre del Producto, Categoría, Precio Base]

menu = [
    ["Hamburguesa", "Comida rápida", 8000],
    ["Pizza", "Comida rápida", 12000],
    ["Ensalada", "Saludable", 7000],
    ["Salmón", "Gourmet", 18000],
    ["Pasta", "Italiana", 11500],
    ["Jugo Natural", "Bebidas", 4500]
]

# =========================================
# FUNCIÓN PARA CALCULAR EL PRECIO FINAL
# =========================================

def calcular_precio_final(producto, categoria_objetivo, umbral):
    
    # Extraer datos del producto
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    # Verificar si aplica descuento
    if categoria.lower() == categoria_objetivo.lower() and precio_base > umbral:
        
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
    
    else:
        precio_final = precio_base

    return precio_final


def obtener_categorias(menu):
    categorias = []
    for producto in menu:
        categoria = producto[1]
        if categoria not in categorias:
            categorias.append(categoria)
    return categorias


def solicitar_datos_promocion(menu):
    categorias = obtener_categorias(menu)
    print("Categorías disponibles:")
    for categoria in categorias:
        print("-", categoria)

    categoria_objetivo = ""
    while not categoria_objetivo:
        categoria_objetivo = input("Ingrese la categoría de promoción: ").strip()
        if not categoria_objetivo:
            print("La categoría no puede estar vacía.")
        elif categoria_objetivo not in categorias and categoria_objetivo.lower() not in [c.lower() for c in categorias]:
            print("Categoría no válida. Elija una de las categorías mostradas arriba.")
            categoria_objetivo = ""

    while True:
        try:
            umbral = float(input("Ingrese el umbral de precio para aplicar el descuento: "))
            break
        except ValueError:
            print("Valor inválido. Ingrese un número para el umbral.")

    return categoria_objetivo, umbral


# =========================================
# CONFIGURACIÓN DE LA PROMOCIÓN (DATOS SOLICITADOS)
# =========================================

categoria_objetivo, umbral = solicitar_datos_promocion(menu)


# =========================================
# MOSTRAR RESULTADOS
# =========================================

print("========= MENÚ DEL RESTAURANTE =========\n")

for producto in menu:

    precio_final = calcular_precio_final(
        producto,
        categoria_objetivo,
        umbral
    )

    print("Producto:", producto[0])
    print("Categoría:", producto[1])
    print("Precio base: $", producto[2])
    print("Precio final: $", round(precio_final, 2))
    print("----------------------------------")