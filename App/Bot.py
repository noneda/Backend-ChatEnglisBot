import re
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import nltk
nltk.download('Assistant')

chat = ChatBot(
    'chatbot',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter'
)

trainer = ListTrainer(chat)

conversation_flow = {
    # Saludos y comienzo de conversación
    "saludo": {
        "patron": re.compile(r"\b(hola|buenos días|buenas tardes|qué tal)\b", re.IGNORECASE),
        "respuesta": "¡Hola! 😊 Bienvenido/a al asistente de cursos de inglés. ¿Te gustaría mejorar tu nivel de inglés?"
    },

    # Respuestas afirmativas al inicio
    "respuesta_afirmativa": {
        "patron": re.compile(r"\b(sí|claro|por supuesto|me gustaría)\b", re.IGNORECASE),
        "respuesta": "¡Excelente! ¿Qué nivel de inglés tienes actualmente? (Principiante, Intermedio, Avanzado)"
    },

    # Nivel Principiante
    "nivel_principiante": {
        "patron": re.compile(r"\b(principiante|nunca he estudiado inglés|nivel básico)\b", re.IGNORECASE),
        "respuesta": "Tenemos un curso para empezar desde cero, aprenderás vocabulario básico, frases y gramática esencial. ¿Te gustaría conocer más sobre el contenido del curso y su duración?"
    },

    # Respuesta sobre contenido y duración para nivel Principiante
    "contenido_duracion_principiante": {
        "patron": re.compile(r"\b(sí, por favor|cuéntame más|quiero saber más)\b", re.IGNORECASE),
        "respuesta": "Nuestros cursos tienen una duración de 3 meses con clases interactivas dos veces por semana. Además, contarás con material adicional y sesiones de práctica. ¿Te gustaría saber sobre los precios?"
    },

    # Nivel Intermedio
    "nivel_intermedio": {
        "patron": re.compile(r"\b(intermedio|he estudiado un poco|nivel medio)\b", re.IGNORECASE),
        "respuesta": "Perfecto para mejorar tu fluidez, expandir vocabulario y ganar confianza en tus conversaciones. ¿Te gustaría conocer más sobre el contenido del curso y su duración?"
    },

    # Respuesta sobre contenido y duración para nivel Intermedio
    "contenido_duracion_intermedio": {
        "patron": re.compile(r"\b(sí, me interesa|cuéntame sobre el curso|quiero más detalles)\b", re.IGNORECASE),
        "respuesta": "Nuestros cursos tienen una duración de 3 meses con clases interactivas dos veces por semana. Además, contarás con material adicional y sesiones de práctica. ¿Te gustaría saber sobre los precios?"
    },

    # Nivel Avanzado
    "nivel_avanzado": {
        "patron": re.compile(r"\b(avanzado|buen dominio|nivel alto)\b", re.IGNORECASE),
        "respuesta": "Ideal para perfeccionar tu inglés y trabajar en la precisión gramatical, pronunciación y expresiones idiomáticas. ¿Te gustaría conocer más sobre el contenido del curso y su duración?"
    },

    # Respuesta sobre contenido y duración para nivel Avanzado
    "contenido_duracion_avanzado": {
        "patron": re.compile(r"\b(sí, quiero saber más|quiero obtener más detalles)\b", re.IGNORECASE),
        "respuesta": "Nuestros cursos tienen una duración de 3 meses con clases interactivas dos veces por semana. Además, contarás con material adicional y sesiones de práctica. ¿Te gustaría saber sobre los precios?"
    },

    # Pregunta sobre los precios del curso
    "pregunta_precios": {
        "patron": re.compile(r"\b(precio|cuánto cuesta|quiero conocer los precios)\b", re.IGNORECASE),
        "respuesta": "El costo es de [Insertar precio] por mes. También ofrecemos descuentos si pagas por el curso completo desde el inicio. Aceptamos pagos con tarjeta, transferencia y algunos métodos de pago digital. ¿Te gustaría inscribirte ahora o necesitas más información?"
    },

    # Respuesta para inscripción
    "respuesta_inscripcion": {
        "patron": re.compile(r"\b(inscribirme|registrarme|estoy listo)\b", re.IGNORECASE),
        "respuesta": "¡Genial! Para finalizar la inscripción, por favor ingresa tu nombre completo y un número de contacto o correo electrónico."
    },

    # Confirmación de inscripción
    "confirmacion_inscripcion": {
        "patron": re.compile(r"\b(ya di mis datos|he enviado mis datos)\b", re.IGNORECASE),
        "respuesta": "Gracias, [Nombre del usuario]. En breve recibirás un mensaje con los detalles para completar tu inscripción. ¡Nos emociona que te unas a nuestra comunidad de estudiantes de inglés! ¿Te gustaría que te mantengamos informado/a de más cursos y promociones?"
    },

    # Respuesta de despedida
    "respuesta_despedida": {
        "patron_si": re.compile(r"\b(sí, quiero estar informado)\b", re.IGNORECASE),
        "patron_no": re.compile(r"\b(no necesito más información)\b", re.IGNORECASE),
        "respuesta_si": "¡Listo! Te mantendremos informado/a sobre nuevos cursos y promociones. ¡Nos vemos pronto!",
        "respuesta_no": "¡Gracias por tu tiempo! 😊 Si tienes alguna pregunta en el futuro, no dudes en escribirnos. ¡Éxito en tu aprendizaje de inglés!"
    }
}


if not chat.storage.filter():  # Verifica si la base de datos está vacía
    trainer = ListTrainer(chat)
    for key, conversations in conversation_flow.items():
        trainer.train(conversations)
