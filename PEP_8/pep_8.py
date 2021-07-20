''' ----- Guia De Estilo PEP8 ----'''




# Alineado con delimitador de apertura.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Agregue 4 espacios (un nivel adicional de indentación) para distinguir los argumentos del resto.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Las indentaciones colgantes deben agregar un nivel.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)