import reflex as rx

from app.components.footer import EMAIL, footer
from app.components.navbar import navbar


def _block(title: str, *paragraphs: str) -> rx.Component:
    return rx.el.section(
        rx.el.h2(
            title,
            class_name="font-serif text-2xl text-stone-50 sm:text-3xl",
        ),
        rx.el.div(
            *[
                rx.el.p(
                    text,
                    class_name="mt-4 text-base leading-relaxed text-stone-400",
                )
                for text in paragraphs
            ],
        ),
        class_name="border-t border-white/10 py-10 first:border-t-0",
    )


def privacy_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Documento legal",
                        class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                    ),
                    rx.el.h1(
                        "Política de privacidad",
                        class_name="mt-4 font-serif text-5xl leading-tight text-stone-50 sm:text-6xl",
                    ),
                    rx.el.p(
                        "Lorenly Music · Lima, Perú",
                        class_name="mt-4 text-sm text-stone-500",
                    ),
                    class_name="mx-auto w-full max-w-3xl px-6 pb-12 pt-16",
                ),
                class_name="border-b border-white/10 bg-[#1a1615]",
            ),
            rx.el.article(
                _block(
                    "Quiénes somos",
                    "Este sitio pertenece a Lorenly Music, proyecto personal de producción musical VOCALOID. "
                    "La dirección de contacto para cualquier consulta sobre privacidad es "
                    f"{EMAIL}.",
                ),
                _block(
                    "Qué datos recogemos",
                    "No se solicitan datos personales para navegar por el sitio. Únicamente tratamos la "
                    "información que nos envías de forma voluntaria cuando escribes por correo electrónico, "
                    "teléfono o WhatsApp: nombre, datos de contacto y el contenido de tu mensaje.",
                    "No recogemos datos sensibles, ni realizamos perfiles automatizados, ni vendemos "
                    "información a terceros.",
                ),
                _block(
                    "Finalidad del tratamiento",
                    "Usamos tus datos exclusivamente para responder a tu consulta, preparar presupuestos de "
                    "servicios musicales y dar seguimiento a los proyectos acordados. Conservamos los "
                    "mensajes solo durante el tiempo necesario para esa finalidad.",
                ),
                _block(
                    "Contenido incrustado de otros sitios",
                    "Las páginas del sitio pueden incluir reproductores de YouTube u otros servicios de "
                    "vídeo y audio. Estos reproductores solo se cargan cuando los solicitas de forma "
                    "explícita mediante el botón correspondiente, para evitar que terceros recojan datos "
                    "sin tu conocimiento.",
                    "Cuando cargas un reproductor, el servicio externo puede recibir tu dirección IP y "
                    "utilizar sus propias cookies, según su política de privacidad.",
                ),
                _block(
                    "Cookies",
                    "El sitio no utiliza cookies publicitarias ni de seguimiento propias. Los servicios "
                    "incrustados que decidas cargar pueden establecer sus propias cookies técnicas.",
                ),
                _block(
                    "Tus derechos",
                    "Puedes solicitar en cualquier momento el acceso, la rectificación o la eliminación de "
                    f"los datos que nos hayas facilitado escribiendo a {EMAIL}. Atenderemos tu solicitud "
                    "en el plazo más breve posible.",
                ),
                _block(
                    "Seguridad y cambios",
                    "Aplicamos medidas razonables para proteger la información recibida. Si esta política "
                    "cambia, publicaremos la versión actualizada en esta misma página indicando la fecha "
                    "de revisión.",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.icon("arrow-left", class_name="h-4 w-4"),
                        "Volver a la portada",
                        href="/",
                        class_name="flex w-fit items-center gap-3 border border-white/20 px-5 py-3 text-xs uppercase tracking-[0.2em] text-stone-200 hover:border-[#ff5a4e] hover:text-[#ff5a4e] transition-colors",
                    ),
                    class_name="border-t border-white/10 pt-10",
                ),
                class_name="mx-auto w-full max-w-3xl px-6 py-16",
            ),
        ),
        footer(),
        class_name="min-h-screen bg-[#141110] font-['Inter'] antialiased",
    )
