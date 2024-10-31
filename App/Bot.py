from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import nltk
nltk.download('punkt_tab')

chat = ChatBot('chatbot')
trainer = ListTrainer(chat)

conversation_flow = {
    "start": {
        "message": "¡Hola! 😊 Bienvenido/a al asistente de cursos de inglés. ¿Te gustaría mejorar tu nivel de inglés?",
        "responses": {
            "sí": "english_level",
            "no": "farewell"
        }
    },
    "english_level": {
        "message": "¡Excelente! ¿Qué nivel de inglés tienes actualmente? (Principiante, Intermedio, Avanzado)",
        "responses": {
            "principiante": "beginner_info",
            "intermedio": "intermediate_info",
            "avanzado": "advanced_info"
        }
    },
    "beginner_info": {
        "message": "Tenemos un curso para empezar desde cero, aprenderás vocabulario básico, frases y gramática esencial. ¿Te gustaría conocer más sobre el contenido del curso y su duración?",
        "responses": {
            "sí": "course_details",
            "no": "farewell"
        }
    },
    "intermediate_info": {
        "message": "Perfecto para mejorar tu fluidez, expandir vocabulario y ganar confianza en tus conversaciones. ¿Te gustaría conocer más sobre el contenido del curso y su duración?",
        "responses": {
            "sí": "course_details",
            "no": "farewell"
        }
    },
    "advanced_info": {
        "message": "Ideal para perfeccionar tu inglés y trabajar en la precisión gramatical, pronunciación y expresiones idiomáticas. ¿Te gustaría conocer más sobre el contenido del curso y su duración?",
        "responses": {
            "sí": "course_details",
            "no": "farewell"
        }
    },
    "course_details": {
        "message": "Nuestros cursos tienen una duración de 3 meses con clases interactivas dos veces por semana. Además, contarás con material adicional y sesiones de práctica. ¿Te gustaría saber sobre los precios?",
        "responses": {
            "sí": "price_info",
            "no": "farewell"
        }
    },
    "price_info": {
        "message": "El costo es de [Insertar precio] por mes. También ofrecemos descuentos si pagas por el curso completo desde el inicio. Aceptamos pagos con tarjeta, transferencia y algunos métodos de pago digital. ¿Te gustaría inscribirte ahora o necesitas más información?",
        "responses": {
            "inscribirme": "registration",
            "más información": "farewell"
        }
    },
    "registration": {
        "message": "¡Genial! Para finalizar la inscripción, por favor ingresa tu nombre completo y un número de contacto o correo electrónico.",
        "responses": {
            "datos_proporcionados": "registration_confirmation"
        }
    },
    "registration_confirmation": {
        "message": "Gracias, [Nombre del usuario]. En breve recibirás un mensaje con los detalles para completar tu inscripción. ¡Nos emociona que te unas a nuestra comunidad de estudiantes de inglés! ¿Te gustaría que te mantengamos informado/a de más cursos y promociones?",
        "responses": {
            "sí": "farewell_with_updates",
            "no": "farewell"
        }
    },
    "farewell": {
        "message": "¡Gracias por tu tiempo! 😊 Si tienes alguna pregunta en el futuro, no dudes en escribirnos. ¡Éxito en tu aprendizaje de inglés!"
    },
    "farewell_with_updates": {
        "message": "¡Listo! Te mantendremos informado/a sobre nuevos cursos y promociones. ¡Nos vemos pronto!"
    }
}

for step, info in conversation_flow.items():
    trainer.train([info['message']] + list(info.get('responses', {}).keys()))