from admindatos import AdminDatos
from graficas import Graficas
import os
df=AdminDatos.leer_csv("encautaciones_de_drogas.csv")
opci=-1
while(opci!="0"):
    print("Bienvenido al menú")
    print("1. Mostrar primeros y ultimos datos.")
    print("2. Mostrar estadisticas generales de los datos.")
    print("3. Buscar por codigo del DANE.")
    print("4. Incautación por departamento.")
    print("5. Incautación por municipio.")
    print("6. Sustancias mas y menos incautadas.")
    print("7. Graficas")
    print("0. Salir")
    opci=input("Ingrese una opción del menú: ")
    if opci=="1":
        os.system('cls')
        print(df)
        input("Presione Enter para continuar...")
        os.system('cls')
    elif opci=="2":
        os.system('cls')
        AdminDatos.Estadisticas(df)
        input("Presione Enter para continuar...")
        os.system('cls')
    elif opci=="3":
        os.system('cls')
        codigo=int(input("Ingrese el codigo del DANE que desea buscar: "))
        AdminDatos.buscarpordane(df,codigo)
        input("Presione Enter para continuar...")
        os.system('cls')
    elif opci=="4":
        os.system('cls')
        AdminDatos.mayor_departamento(df)
        AdminDatos.menor_departamento(df)
        input("Presione Enter para continuar...")
        os.system('cls')
    elif opci=="5":
        os.system('cls')
        AdminDatos.mayor_municipio(df)
        AdminDatos.menor_municipio(df)
        input("Presione Enter para continuar...")
        os.system('cls')
    elif opci=="6":
        os.system('cls')
        AdminDatos.mayor_sustancia(df)
        AdminDatos.menor_sustancia(df)
        input("Presione Enter para continuar...")
        os.system('cls')
    elif opci=="7":
        os.system('cls')
        print("Bienvenido al submenú de graficas")
        print("1. Incautaciones por dias")
        print("2. Municipios con mayores y menores incautaciones")
        print("3. Departamentos con mayores y menores incautaciones")
        print("4. Boxplot de incautaciones")
        print("5. Todas las graficas")
        opci2=input("Ingrese una opción del submenú: ")
        if opci2=="1":
            Graficas.pormesgra(df)
        elif opci2=="2":
            Graficas.GraficaMunicipios_Mayor(df)
            Graficas.GraficaMunicipios_Menor(df)
        elif opci2=="3":
            Graficas.Grafica_Departamento_Mayor(df)
            Graficas.Grafica_Departamento_Menor(df)
        elif opci2=="4":
            Graficas.Grafica_quartiles(df)
        elif opci2=="5":
            Graficas.Graficas_Todas(df)
        else:
            print("Opción Invalida")
            os.system('cls')
        os.system('cls')
    elif opci=="0":
        print("Adios.")
        break
    else:
        print("Opción Invalida")
    print("")
