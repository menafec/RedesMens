import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Resultados hipotéticos
data = {
    'Sección 1: Datos Demográficos': {
        'Nivel de conocimiento sobre el ciclo menstrual': {
            'Poco': 20,
            'Moderado': 50,
            'Alto': 30,
        },
        'Uso actual de aplicaciones para el seguimiento del ciclo': {
            'Sí': 65,
            'No': 35,
        }
    },
    'Sección 2: Uso de Tecnología para el Monitoreo del Ciclo': {
        'Importancia del monitoreo del ciclo': {
            'Muy importante': 60,
            'Importante': 30,
            'Poco importante': 8,
            'No importante': 2,
        },
        'Interés en utilizar una aplicación basada en IA': {
            'Sí, definitivamente': 55,
            'Probablemente sí': 30,
            'No estoy segura': 10,
            'No, probablemente no': 5,
        },
        'Precisión esperada': {
            'Muy precisa (±1 día de error)': 70,
            'Moderadamente precisa (±3 días de error)': 25,
            'No me preocupa tanto la precisión': 5,
        }
    },
    'Sección 3: Opiniones sobre la Aplicación': {
        'Características adicionales deseadas': {
            'Recordatorios para la toma de anticonceptivos': 40,
            'Consejos personalizados sobre la salud femenina': 60,
            'Información educativa sobre las diferentes fases del ciclo': 50,
            'Integración con dispositivos de salud': 35,
        },
        'Facilidad de uso esperada': {
            'Muy fácil de usar': 80,
            'Moderadamente fácil de usar': 18,
            'Difícil de usar': 2,
        },
        'Preocupación por la privacidad de los datos': {
            'Sí, mucho': 50,
            'Moderadamente': 30,
            'Poco': 15,
            'No me preocupa': 5,
        }
    }
}

# Crear un archivo PDF
with PdfPages('resultados_encuesta.pdf') as pdf:
    # Crear gráficos
    for section, questions in data.items():
        for question, responses in questions.items():
            labels = responses.keys()
            values = responses.values()

            # Gráfico de barras
            plt.figure(figsize=(10, 6))
            plt.bar(labels, values, color='skyblue')
            plt.title(f'{section} - {question}')
            plt.xlabel('Opciones')
            plt.ylabel('Porcentaje (%)')
            plt.ylim(0, 100)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            pdf.savefig()  # Guardar la figura actual en el PDF
            plt.close()  # Cerrar la figura para liberar memoria

            # Gráfico de pastel (si hay más de dos categorías)
            if len(labels) > 2:
                plt.figure(figsize=(10, 6))
                plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
                plt.title(f'{section} - {question}')
                plt.axis('equal')  # Para que el gráfico de pastel sea circular
                pdf.savefig()  # Guardar la figura actual en el PDF
                plt.close()  # Cerrar la figura para liberar memoria

print("Los gráficos han sido guardados en 'resultados_encuesta.pdf'.")