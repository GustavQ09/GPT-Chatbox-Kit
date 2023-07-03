import openai
import os
from dotenv import load_dotenv
import chatbot
import clasificacion_texto
import crear_contenido
import resumir_contenido


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key


def mostrar_menu():
    print("Bienvenido al menú:")
    print("1. Preguntar a ChatGPT")
    print("2. Clasificar texto")
    print("3. Crear contenido")
    print("4. Resumir texto")
    print("5. Salir")

def ejecutar_opcion(opcion):
    if opcion == "1":
        preguntas_anteriores = []
        respuestas_anteriores = []

        print("Bienvenido al chatbot básico con chatGPT. Escribe 'salir' cuando desees terminar.")

        while True:
            conversacion_historica = ""
            ingreso_usuario = input("\nTú:")
            if ingreso_usuario.lower() == "salir":
                break

            for pregunta, respuesta in zip(preguntas_anteriores, respuestas_anteriores):
                conversacion_historica += f"El usuario pregunta: {pregunta}\n"
                conversacion_historica += f"ChatGPT responde: {respuesta}\n"

            prompt = f"El usuario pregunta: {ingreso_usuario}\n"
            conversacion_historica += prompt
            respuesta_gpt = chatbot.preguntar_chat_gpt(conversacion_historica)
            print(f"{respuesta_gpt}")

            preguntas_anteriores.append(ingreso_usuario)
            respuestas_anteriores.append(respuesta_gpt)

    elif opcion == "2":
        texto_para_clasificar = input("Ingresa un texto: ")
        clasificacion = clasificacion_texto.clasificar_texto(texto_para_clasificar)
        print(f"La clasificación es: {clasificacion}")

    elif opcion == "3":
        tema = input("Elija un tema para tu artículo: ")
        tokens = int(input("¿Cuántos tokens máximo tendrá tu artículo?: "))
        temperatura = int(input("Del 1 al 10, ¿qué tan creativo quieres que sea tu artículo?: ")) / 10

        articulo_creado = crear_contenido.crear_contenido(tema, tokens, temperatura)
        print(f"Artículo creado:\n{articulo_creado}")

    elif opcion == "4":
        original = input("Pega aquí el artículo que deseas resumir: ")
        tokens = int(input("¿Cuántos tokens máximos tendrá tu resumen?: "))
        temperatura = int(input("Del 1 al 10, ¿qué tan creativo quieres que sea tu resumen?: ")) / 10

        resumen = resumir_contenido.resumir_texto(original, tokens, temperatura)
        print(f"Resumen:\n{resumen}")

    elif opcion == "5":
        return True

    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")

    return False

def main():
    print("Bienvenido a nuestro chatbot básico. Escribe 'salir' cuando quieras terminar")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        salir = ejecutar_opcion(opcion)
        if salir:
            break

if __name__ == "__main__":
     main()

