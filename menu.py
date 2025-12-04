from admindatos import AdminDatos

df=AdminDatos.leer_csv("encautaciones_de_drogas.csv")
opci=-1
while(opci!="0"):
    print("Bienvenido al menú")
    print("1. Mostrar primeros y ultimos datos.")
    print("2. Mostrar estadisticas generales de los datos.")
    print("3. Buscar por codigo del DANE.")
    print("4. Incautación por departamento.")
    print("5. Incautación por municipio.")
    print("0. Salir")
    opci=input("Ingrese una opción del menú: ")
    if opci=="1":
        print(df)
    if opci=="2":
        AdminDatos.Estadisticas(df)
    if opci=="3":
        codigo=int(input("Ingrese el codigo del DANE que desea buscar: "))
        AdminDatos.buscarpordane(df,codigo)
    if opci=="4":
        pass
    if opci=="5":
        AdminDatos.mayor_municipio(df)
        AdminDatos.menor_municipio(df)
    if opci=="0":
        print("Adios.")
        break
    else:
        print("Opción Invalida")
    print("")