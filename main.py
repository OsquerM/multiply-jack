#Variables globales
result = 0
#Funciones
def run(n: int) -> int:
    # TODO
    global result
    #Variables locales
    elevado = 5 ** (len(str(n)))
    result = n * elevado
    return result

#Codigo Principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(result)