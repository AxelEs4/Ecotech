import requests, json, os

def menu_indicadores():
    os.system("cls")
    while True:
        print("---- Consumiendo API indicadores economicos ----")
        print("1 U.F.")
        print("2 Dolar")
        print("3 Euro")
        print("4 IPC")
        print("5 Salir")
        print("-----------------------------------------------")

        try:
            opcion =int(input("Ingrese el número del indicador que desea consultar: "))

            if opcion==1:
                os.system("cls")
                fecha=input("Ingrese la fecha en formato DD-MM-AA: ")

                try:
                    url = requests.get(f"https://indicadores.cl/api/v1/historico/uf/{fecha[6:10]}.json", timeout=10)
                    url.raise_for_status
                    texto = url.text
                    datos = json.loads(texto)

                    for clave, valor in datos.items():
                        if clave == "serie":
                            encontrado = False
                            for registro in valor:
                                if registro["fecha"] == fecha[6:10] + "-" + fecha[3:5] + "-" + fecha[0:2]:
                                    print(f"El valor de la U.F. el dia {fecha} es: {registro["valor"]}")
                                    input("Presiona cualquier tecla para continuar...")
                                    os.system("cls")
                                    encontrado = True

                            if encontrado == False:
                                print("No existen datos para esta fecha")
                except requests.exceptions.RequestException:
                    print("Error al encontrar la API. Verifique su conexión")
                except json.JSONDecodeError:
                    print("Error al procesar los datos recibidos")
                except (KeyError, IndexError):
                    print("Error: No se encontraron datos para esa fecha.")

            elif opcion==2:
                os.system("cls")
                fecha=input("Ingrese la fecha en formato DD-MM-AA: ")
            
                try:
                    url = requests.get(f"https://indicadores.cl/api/v1/historico/dolar/{fecha[6:10]}.json", timeout=10)
                    url.raise_for_status
                    texto = url.text
                    datos = json.loads(texto)
                
                    for clave, valor in datos.items():
                        if clave == "serie":
                            encontrado = False
                            for registro in valor:
                                if registro["fecha"] == fecha[6:10] + "-" + fecha[3:5] + "-" + fecha[0:2]:
                                    print(f"El valor del Dolar el dia {fecha} es: {registro["valor"]}")
                                    input("Presiona cualquier tecla para continuar...")
                                    os.system("cls")
                                    encontrado = True
                            if encontrado == False:
                                print("No existen datos para esta fecha")
                except requests.exceptions.RequestException:
                    print("Error al encontrar la API. Verifique su conexión")
                except json.JSONDecodeError:
                    print("Error al procesar los datos recibidos")
                except (KeyError, IndexError):
                    print("Error: No se encontraron datos para esa fecha.")

            elif opcion==3:
                os.system("cls")
                fecha=input("Ingrese la fecha en formato DD-MM-AA: ")

                try:
                    url = requests.get(f"https://indicadores.cl/api/v1/euro/{fecha[6:10]}.json", timeout=10)
                    url.raise_for_status
                    texto = url.text
                    datos = json.loads(texto)

                    for clave, valor in datos.items():
                        if clave == "serie":
                            encontrado = False
                            for registro in valor:
                                if registro["fecha"] == fecha[6:10] + "-" + fecha[3:5] + "-" + fecha[0:2]:
                                    print(f"El valor del Euro el dia {fecha} es: {registro["valor"]}")
                                    input("Presiona cualquier tecla para continuar...")
                                    os.system("cls")
                                    encontrado = True

                            if encontrado == False:
                                print("No existen datos para esta fecha")

                except requests.exceptions.RequestException:
                    print("Error al encontrar la API. Verifique su conexión")
                except json.JSONDecodeError:
                    print("Error al procesar los datos recibidos")
                except (KeyError, IndexError):
                    print("Error: No se encontraron datos para esa fecha.")

            elif opcion==4:
                os.system("cls")
                fecha=input("Ingrese la fecha en formato AAAA-MM: ")

                try:
                    url = requests.get(f"https://indicadores.cl/api/v1/ips.json", timeout=10)
                    url.raise_for_status
                    texto = url.text
                    datos = json.loads(texto)

                    for clave, valor in datos.items():
                        if clave == "serie":
                            encontrado = False
                            for registro in valor:
                                if registro["fecha"] == fecha[0:4] + "-" + fecha[6:8]:
                                    print(f"El valor del Ips {fecha} es: {registro["validación mensual"]}")
                                    input("Presiona cualquier tecla para continuar...")
                                    os.system("cls")
                                    encontrado = True

                            if encontrado == False:
                                print("No existen datos para esta fecha")
                except requests.exceptions.RequestException:
                    print("Error al encontrar la API. Verifique su conexión")
                except json.JSONDecodeError:
                    print("Error al procesar los datos recibidos")
                except (KeyError, IndexError):
                    print("Error: No se encontraron datos para esa fecha.")

            elif opcion==5:
                os.system("cls")
                print("Saliendo del programa....")
                break
            else:
                print("Opción invalida. Por favor, ingrese un número del 1 al 5.")

        except ValueError:
            print("Error: Debe ingresar un número valido")
