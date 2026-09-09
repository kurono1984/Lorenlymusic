from typing import TypedDict

import reflex as rx

from app.states.site_content_state import PERFORMANCE_ONE, PERFORMANCE_TWO

PHONE_PRIMARY = "+51965048629"
PHONE_PRIMARY_DISPLAY = "+51 965 048 629"
CONTACT_EMAIL = "lorenly75@gmail.com"
WHATSAPP_URL = "https://wa.me/51965048629"
KOFI_URL = "https://ko-fi.com/lorenly"

LORENLY_COVER = (
    "https://lorenlymusic.com/wp-content/uploads/2020/06/"
    "Lorenly-Went-Down-To-Jamaica-HD2-768x432.png"
)
LORENLY_PORTRAIT = (
    "https://lorenlymusic.com/wp-content/uploads/2020/07/"
    "19225771_215731622282044_4219852396290415515_n.jpg"
)


class TimelineItem(TypedDict):
    year: str
    title: str
    detail: str


class VoicebankItem(TypedDict):
    name: str
    engine: str
    detail: str


class StagePhoto(TypedDict):
    key: str
    caption: str
    place: str
    src: str


class ServiceItem(TypedDict):
    key: str
    number: str
    icon: str
    title: str
    summary: str
    detail: str
    includes: list[str]


class ProfileState(rx.State):
    """Datos verificados de la trayectoria de Lorenly y de sus servicios."""

    timeline: list[TimelineItem] = [
        {
            "year": "Desde los 8 años",
            "title": "Composición",
            "detail": "Lorenly compone música desde los ocho años de edad.",
        },
        {
            "year": "2011 – 2012",
            "title": "Animatissimo",
            "detail": "Integra Animatissimo entre 2011 y 2012.",
        },
        {
            "year": "Desde 2012",
            "title": "Luminus Hearts",
            "detail": "Forma parte de Luminus Hearts, fundado en septiembre de 2012.",
        },
        {
            "year": "Desde 2016",
            "title": "UCG",
            "detail": "Participa en UCG desde 2016.",
        },
        {
            "year": "Abril de 2017",
            "title": "VOCALOID",
            "detail": "Comienza a producir con voces sintetizadas VOCALOID en abril de 2017.",
        },
        {
            "year": "2019",
            "title": "VocaloP Hispanos",
            "detail": "Impulsa VocaloP Hispanos en 2019.",
        },
        {
            "year": "2020",
            "title": "MIKU EXPO 2020 Europe",
            "detail": "Obtiene una mención honorífica en MIKU EXPO 2020 Europe.",
        },
    ]

    voicebanks: list[VoicebankItem] = [
        {
            "name": "Hatsune Miku",
            "engine": "VOCALOID",
            "detail": "Voz de «Luna a cuestas», «Life / Mi vida sin tu amor» y «A las 2:30 pm».",
        },
        {
            "name": "Megpoid Gumi",
            "engine": "VOCALOID",
            "detail": "Voz de «Luz», «Cálida Esperanza», «Harawikunaq Wasin» y «El cóndor pasa».",
        },
        {
            "name": "Maika",
            "engine": "VOCALOID",
            "detail": "Voz de «Cactus Triste» y «Días grises, días de color».",
        },
        {
            "name": "Kagamine Rin y Len",
            "engine": "VOCALOID",
            "detail": "Voces de «Corazón de Fuego» y «Natividad».",
        },
        {
            "name": "Tohoku Zunko",
            "engine": "VOCALOID",
            "detail": "Voz de «Sujétate de mi».",
        },
        {
            "name": "Silvana Aritani",
            "engine": "UTAU",
            "detail": "Voicebank propio: «Rosas Frescas en tu Puerta», «Más cerca que antes» y «Sí».",
        },
    ]

    stage_photos: list[StagePhoto] = [
        {
            "key": "foto-portada",
            "caption": "Portada de «Lorenly Went Down To Jamaica»",
            "place": "Lanzamiento",
            "src": LORENLY_COVER,
        },
        {
            "key": "foto-directo-1",
            "caption": "Lorenly en una presentación en vivo",
            "place": "En directo",
            "src": PERFORMANCE_ONE,
        },
        {
            "key": "foto-directo-2",
            "caption": "Lorenly durante una actuación",
            "place": "En directo",
            "src": PERFORMANCE_TWO,
        },
    ]

    services: list[ServiceItem] = [
        {
            "key": "instrumental",
            "number": "01",
            "icon": "piano",
            "title": "Música instrumental e incidental",
            "summary": "Piezas sin voz para escenas, ambientes y proyectos audiovisuales.",
            "detail": "Composición de temas instrumentales y música incidental a medida: cortinas, fondos para narración, ambientes para videojuegos, teatro, podcasts y vídeos. Se trabaja a partir de la duración, el ánimo y las referencias que indiques.",
            "includes": [
                "Temas completos o cortinas breves",
                "Ajuste a la duración exacta de la escena",
                "Versiones alternativas de intensidad",
            ],
        },
        {
            "key": "canciones",
            "number": "02",
            "icon": "music",
            "title": "Canciones en géneros variados",
            "summary": "Canciones originales completas, del pop a la balada.",
            "detail": "Creación de canciones desde cero en el género que necesite tu proyecto. Incluye idea musical, estructura, letra, arreglo y mezcla final lista para publicar.",
            "includes": [
                "Composición y estructura completa",
                "Arreglo e instrumentación",
                "Mezcla final del tema",
            ],
        },
        {
            "key": "letras",
            "number": "03",
            "icon": "pen-line",
            "title": "Letras",
            "summary": "Letras en español escritas sobre tu idea, tema o melodía.",
            "detail": "Escritura de letras originales en español, cuidando la métrica, la rima y la cantabilidad. Puede partir de una idea, de un briefing temático o de una melodía ya existente que necesite texto.",
            "includes": [
                "Letra original a partir de tu idea",
                "Métrica adaptada a la melodía",
                "Revisiones acordadas del texto",
            ],
        },
        {
            "key": "melodia",
            "number": "04",
            "icon": "audio-waveform",
            "title": "Melodía e instrumentación",
            "summary": "Línea vocal y base instrumental para letras o proyectos existentes.",
            "detail": "Composición de la melodía vocal y de la instrumentación que la acompaña. Si ya tienes una letra o una maqueta, se construye la línea melódica y el acompañamiento completo alrededor de ella.",
            "includes": [
                "Melodía vocal cantable",
                "Base instrumental completa",
                "Guías de tonalidad y tempo",
            ],
        },
        {
            "key": "arreglos",
            "number": "05",
            "icon": "sliders-horizontal",
            "title": "Armonización, adaptaciones y arreglos",
            "summary": "Armonías, coros y nuevas versiones de temas ya escritos.",
            "detail": "Armonización de melodías, escritura de coros y segundas voces, adaptación de canciones a otra tonalidad, formato o estilo, y arreglos nuevos para temas propios o ajenos.",
            "includes": [
                "Armonización y coros",
                "Cambio de tonalidad o formato",
                "Arreglos acústicos u orquestales",
            ],
        },
        {
            "key": "infantil",
            "number": "06",
            "icon": "baby",
            "title": "Música infantil",
            "summary": "Canciones didácticas y alegres para niñas y niños.",
            "detail": "Canciones infantiles con letras claras, melodías fáciles de recordar y arreglos amables: material educativo, canciones para colegios, cuentos musicalizados y contenido para familias.",
            "includes": [
                "Letras sencillas y didácticas",
                "Melodías fáciles de cantar",
                "Versión con y sin voz",
            ],
        },
        {
            "key": "video-lyrics",
            "number": "07",
            "icon": "captions",
            "title": "Video lyrics",
            "summary": "Vídeos de letra sincronizados para publicar tu canción.",
            "detail": "Producción de vídeos de letra sincronizados con el audio, con tipografía legible y composición cuidada, listos para YouTube y redes sociales.",
            "includes": [
                "Sincronización de la letra",
                "Diseño tipográfico y de color",
                "Exportación lista para publicar",
            ],
        },
        {
            "key": "demos",
            "number": "08",
            "icon": "mic-vocal",
            "title": "Demos",
            "summary": "Maquetas para presentar o grabar después tu canción.",
            "detail": "Grabación de demos y maquetas de referencia: voz guía, acompañamiento y estructura definida para que puedas presentar la canción, ensayarla o grabarla luego con otra voz.",
            "includes": [
                "Voz guía de referencia",
                "Acompañamiento base",
                "Archivo de audio y guía de acordes",
            ],
        },
        {
            "key": "vocaloid",
            "number": "09",
            "icon": "audio-lines",
            "title": "Manipulación VOCALOID",
            "summary": "Afinación y edición de voces sintetizadas en español.",
            "detail": "Manipulación y afinación de bancos de voz VOCALOID y UTAU: edición fonética para el español, control de expresión, vibrato y dinámica, con el resultado exportado para tu propia mezcla o mezclado aquí.",
            "includes": [
                "Edición fonética para español",
                "Ajuste de expresión y vibrato",
                "Entrega de pistas o mezcla final",
            ],
        },
    ]
