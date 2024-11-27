from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# Diccionario de categorías con palabras clave y respuestas
categorias = {
    "saludo": {
        "palabras_claves": ["hola", "buenos dias", "buenas tardes", "buenas noches", "que tal", "como estas", "saludos"],	
        "respuestas": ["Hola, ¿qué tal?", "Buenos días, un gusto saludarte", "Buenas tardes, un gusto saludarte", "Buenas noches, que descanses"]
    },
    "despedida": {
        "palabras_claves": ["adios", "chao", "hasta luego", "nos vemos", "bye", "gracias","suerte"],
        "respuestas": ["Gracias por su visita", "Un gusto atenderlo", "Que tenga un buen día", "Nos vemos pronto"]
    },
    "feliz": {
        "palabras_claves": ["me siento feliz", "estoy muy contento", "estoy alegre", "me siento de maravilla", "todo va bien", "feliz","dichoso", "contento", "satisfecho", "alegre", "boyante", "próspero", "afortunado", "ufano", "radiante", "bienaventurado"],
        "respuestas": ["¡Eso es genial! Me alegra escuchar eso.", "¡Qué bien! ¿Algo especial que haya pasado?", "¡Maravilloso! Cuéntame más sobre tu día.", "¡Genial! ¿Te gustaría compartir qué te hace sentir tan bien?"]
    },
    "triste":{
        "palabras_claves": ["me siento triste", "estoy deprimido", "no me siento bien", "me siento desanimado", "estoy muy mal","triste","afligido", "apenado", "entristecido", "apesadumbrado", "atribulado", "pesaroso", "mohíno", "mustio", "taciturno", "compungido", "lloroso", "cariacontecido","infausto", "funesto", "deplorable", "lamentable", "luctuoso", "tétrico", "lúgubre", "trágico", "aciago"],
        "respuestas": ["Lamento escuchar eso. ¿Quieres hablar al respecto?", "Siento que te sientas así. Estoy aquí para escucharte.", "Es normal sentirse triste a veces. ¿Hay algo que pueda hacer para ayudarte?", "Lo siento mucho. ¿Te gustaría compartir lo que te está pasando?"]
    },
     "enojado":{
        "palabras_claves": ["estoy enojado", "me siento furioso", "estoy muy molesto", "tengo mucha rabia", "me siento frustrado","enojado","airado" ,"alterado" , "áspero", "bravo", "cabreado" ,"carilargo" ,"colérico" ,"enfadado" ,"irritado" ,"mohíno", "molesto" ,"picado" ,"resentido"],
        "respuestas": ["Lamento que te sientas así. ¿Quieres hablar de lo que te hace sentir enojado?", "La rabia puede ser difícil de manejar. Estoy aquí para escucharte.", "Siento que estés pasando por esto. ¿Hay algo que pueda hacer para ayudarte?", "Es comprensible sentirse frustrado. Cuéntame más sobre lo que está pasando."]
    },
    "ansioso":{
        "palabras_claves": ["me siento ansioso", "estoy nervioso", "tengo mucha ansiedad", "me siento inquieto", "estoy preocupado","ansioso","nervioso"],
        "respuestas": ["Lo siento. La ansiedad puede ser abrumadora. ¿Hay algo específico que te preocupe?", "Entiendo que te sientas ansioso. ¿Quieres hablar de lo que te está causando ansiedad?", "Estoy aquí para ti. Cuéntame más sobre cómo te sientes.", "La preocupación puede ser difícil de manejar. ¿Hay algo que pueda hacer para ayudarte?"]
    },
    "estresado":{
        "palabras_claves": ["me siento estresado", "estoy bajo mucho estrés", "tengo mucho estrés", "me siento abrumado", "estoy muy estresado","estresado"],
        "respuestas": ["Siento que estés estresado. ¿Quieres hablar de lo que te está causando estrés?", "El estrés puede ser muy agotador. Estoy aquí para ayudarte.", "Lamento que te sientas abrumado. ¿Hay algo específico que te cause estrés?", "Estoy aquí para escucharte. Cuéntame más sobre lo que te está pasando."]
    }
    
}

# Clasificador de categorías
def clasificar_categoria(frase):
    frase = frase.lower()
    for categoria, data in categorias.items():
        if any(palabra_clave in frase for palabra_clave in data["palabras_claves"]):
            return categoria
    return "desconocido"

# Chatbot
def chatbot(frase_usuario):
    categoria = clasificar_categoria(frase_usuario)
    if categoria == "desconocido":
        return "Lo siento, no entendí tu pregunta. Por favor, sea más específico."
    return random.choice(categorias[categoria]["respuestas"])

# Modelo para entrada de datos
class FraseEntrada(BaseModel):
    frase: str

# Endpoint del chatbot
@app.post("/chatbot/")
def obtener_respuesta(entrada: FraseEntrada):
    respuesta = chatbot(entrada.frase)
    return {"respuesta": respuesta}