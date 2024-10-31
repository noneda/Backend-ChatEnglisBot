from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import nltk
nltk.download('punkt_tab')

chat = ChatBot('chatbot')
trainer = ListTrainer(chat)

conversation_flow = [
    # Saludos y comienzo de conversación
    "Hola",
    "¡Hola! 😊 Bienvenido/a al asistente de cursos de inglés. ¿Te gustaría mejorar tu nivel de inglés?",
    
    # Respuestas afirmativas al inicio
    "Sí",
    "¡Excelente! ¿Qué nivel de inglés tienes actualmente? (Principiante, Intermedio, Avanzado)",

    # Nivel Principiante
    "Principiante",
    "Tenemos un curso para empezar desde cero, aprenderás vocabulario básico, frases y gramática esencial. ¿Te gustaría conocer más sobre el contenido del curso y su duración?",
    "Sí",
    "Nuestros cursos tienen una duración de 3 meses con clases interactivas dos veces por semana. Además, contarás con material adicional y sesiones de práctica. ¿Te gustaría saber sobre los precios?",

    # Nivel Intermedio
    "Intermedio",
    "Perfecto para mejorar tu fluidez, expandir vocabulario y ganar confianza en tus conversaciones. ¿Te gustaría conocer más sobre el contenido del curso y su duración?",
    "Sí",
    "Nuestros cursos tienen una duración de 3 meses con clases interactivas dos veces por semana. Además, contarás con material adicional y sesiones de práctica. ¿Te gustaría saber sobre los precios?",

    # Nivel Avanzado
    "Avanzado",
    "Ideal para perfeccionar tu inglés y trabajar en la precisión gramatical, pronunciación y expresiones idiomáticas. ¿Te gustaría conocer más sobre el contenido del curso y su duración?",
    "Sí",
    "Nuestros cursos tienen una duración de 3 meses con clases interactivas dos veces por semana. Además, contarás con material adicional y sesiones de práctica. ¿Te gustaría saber sobre los precios?",

    # Pregunta sobre los precios del curso
    "Quiero saber los precios",
    "El costo es de [Insertar precio] por mes. También ofrecemos descuentos si pagas por el curso completo desde el inicio. Aceptamos pagos con tarjeta, transferencia y algunos métodos de pago digital. ¿Te gustaría inscribirte ahora o necesitas más información?",
    
    # Respuesta para inscripción
    "Quiero inscribirme",
    "¡Genial! Para finalizar la inscripción, por favor ingresa tu nombre completo y un número de contacto o correo electrónico.",

    # Confirmación de inscripción
    "Ya proporcioné mis datos",
    "Gracias, [Nombre del usuario]. En breve recibirás un mensaje con los detalles para completar tu inscripción. ¡Nos emociona que te unas a nuestra comunidad de estudiantes de inglés! ¿Te gustaría que te mantengamos informado/a de más cursos y promociones?",

    # Respuesta de despedida
    "No",
    "¡Gracias por tu tiempo! 😊 Si tienes alguna pregunta en el futuro, no dudes en escribirnos. ¡Éxito en tu aprendizaje de inglés!",
    "Sí",
    "¡Listo! Te mantendremos informado/a sobre nuevos cursos y promociones. ¡Nos vemos pronto!"
]

trainer.train(conversation_flow)
