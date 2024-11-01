from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import nltk
nltk.download('punkt_tab')

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
    "saludo": [
        "Hola",
        "¡Hola! 😊 Bienvenido/a al asistente de cursos de inglés. ¿Te gustaría mejorar tu nivel de inglés?",
        "Buenos días",
        "¡Hola! 😊 Bienvenido/a al asistente de cursos de inglés. ¿Te gustaría mejorar tu nivel de inglés?",
        "¿Qué tal?",
        "¡Hola! 😊 Bienvenido/a al asistente de cursos de inglés. ¿Te gustaría mejorar tu nivel de inglés?"
    ],

    # Respuestas afirmativas al inicio
    "respuesta_afirmativa": [
        "Sí, me gustaría.",
        "¡Excelente! ¿Qué nivel de inglés tienes actualmente? (Principiante, Intermedio, Avanzado)",
        "Claro, quiero mejorar mi inglés.",
        "¡Excelente! ¿Qué nivel de inglés tienes actualmente? (Principiante, Intermedio, Avanzado)",
        "Sí, por favor.",
        "¡Excelente! ¿Qué nivel de inglés tienes actualmente? (Principiante, Intermedio, Avanzado)"
    ],

    # Nivel Principiante
    "nivel_principiante": [
        "Soy principiante.",
        "Tenemos un curso para empezar desde cero, aprenderás vocabulario básico, frases y gramática esencial. ¿Te gustaría conocer más sobre el contenido del curso y su duración?",
        "Nunca he estudiado inglés.",
        "Tenemos un curso para empezar desde cero, aprenderás vocabulario básico, frases y gramática esencial. ¿Te gustaría conocer más sobre el contenido del curso y su duración?"
    ],

    # Respuesta sobre contenido y duración para nivel Principiante
    "contenido_duracion_principiante": [
        "Sí, por favor.",
        "Nuestros cursos tienen una duración de 3 meses con clases interactivas dos veces por semana. Además, contarás con material adicional y sesiones de práctica. ¿Te gustaría saber sobre los precios?",
        "Cuéntame más.",
        "Nuestros cursos tienen una duración de 3 meses con clases interactivas dos veces por semana. Además, contarás con material adicional y sesiones de práctica. ¿Te gustaría saber sobre los precios?"
    ],

    # Nivel Intermedio
    "nivel_intermedio": [
        "Tengo un nivel intermedio.",
        "Perfecto para mejorar tu fluidez, expandir vocabulario y ganar confianza en tus conversaciones. ¿Te gustaría conocer más sobre el contenido del curso y su duración?",
        "He estudiado un poco.",
        "Perfecto para mejorar tu fluidez, expandir vocabulario y ganar confianza en tus conversaciones. ¿Te gustaría conocer más sobre el contenido del curso y su duración?"
    ],

    # Respuesta sobre contenido y duración para nivel Intermedio
    "contenido_duracion_intermedio": [
        "Sí, me interesa.",
        "Nuestros cursos tienen una duración de 3 meses con clases interactivas dos veces por semana. Además, contarás con material adicional y sesiones de práctica. ¿Te gustaría saber sobre los precios?",
        "Cuéntame sobre el curso.",
        "Nuestros cursos tienen una duración de 3 meses con clases interactivas dos veces por semana. Además, contarás con material adicional y sesiones de práctica. ¿Te gustaría saber sobre los precios?"
    ],

    # Nivel Avanzado
    "nivel_avanzado": [
        "Estoy en un nivel avanzado.",
        "Ideal para perfeccionar tu inglés y trabajar en la precisión gramatical, pronunciación y expresiones idiomáticas. ¿Te gustaría conocer más sobre el contenido del curso y su duración?",
        "Tengo un buen dominio del idioma.",
        "Ideal para perfeccionar tu inglés y trabajar en la precisión gramatical, pronunciación y expresiones idiomáticas. ¿Te gustaría conocer más sobre el contenido del curso y su duración?"
    ],

    # Respuesta sobre contenido y duración para nivel Avanzado
    "contenido_duracion_avanzado": [
        "Sí, quiero saber más.",
        "Nuestros cursos tienen una duración de 3 meses con clases interactivas dos veces por semana. Además, contarás con material adicional y sesiones de práctica. ¿Te gustaría saber sobre los precios?",
        "Me gustaría obtener más detalles.",
        "Nuestros cursos tienen una duración de 3 meses con clases interactivas dos veces por semana. Además, contarás con material adicional y sesiones de práctica. ¿Te gustaría saber sobre los precios?"
    ],

    # Pregunta sobre los precios del curso
    "pregunta_precios": [
        "Quiero conocer los precios.",
        "El costo es de [Insertar precio] por mes. También ofrecemos descuentos si pagas por el curso completo desde el inicio. Aceptamos pagos con tarjeta, transferencia y algunos métodos de pago digital. ¿Te gustaría inscribirte ahora o necesitas más información?",
        "Dime cuánto cuesta.",
        "El costo es de [Insertar precio] por mes. También ofrecemos descuentos si pagas por el curso completo desde el inicio. Aceptamos pagos con tarjeta, transferencia y algunos métodos de pago digital. ¿Te gustaría inscribirte ahora o necesitas más información?"
    ],

    # Respuesta para inscripción
    "respuesta_inscripcion": [
        "Estoy listo para inscribirme.",
        "¡Genial! Para finalizar la inscripción, por favor ingresa tu nombre completo y un número de contacto o correo electrónico.",
        "Quiero registrarme.",
        "¡Genial! Para finalizar la inscripción, por favor ingresa tu nombre completo y un número de contacto o correo electrónico."
    ],

    # Confirmación de inscripción
    "confirmacion_inscripcion": [
        "Ya he dado mis datos.",
        "Gracias, [Nombre del usuario]. En breve recibirás un mensaje con los detalles para completar tu inscripción. ¡Nos emociona que te unas a nuestra comunidad de estudiantes de inglés! ¿Te gustaría que te mantengamos informado/a de más cursos y promociones?",
        "He enviado mis datos.",
        "Gracias, [Nombre del usuario]. En breve recibirás un mensaje con los detalles para completar tu inscripción. ¡Nos emociona que te unas a nuestra comunidad de estudiantes de inglés! ¿Te gustaría que te mantengamos informado/a de más cursos y promociones?"
    ],

    # Respuesta de despedida
    "respuesta_despedida": {
        "no": [
            "No necesito más información.",
            "¡Gracias por tu tiempo! 😊 Si tienes alguna pregunta en el futuro, no dudes en escribirnos. ¡Éxito en tu aprendizaje de inglés!"
        ],
        "sí": [
            "Sí, quiero estar informado.",
            "¡Listo! Te mantendremos informado/a sobre nuevos cursos y promociones. ¡Nos vemos pronto!"
        ]
    }
}

for key, conversations in conversation_flow.items():
    trainer.train(conversations)