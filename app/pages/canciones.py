import reflex as rx

from app.components.footer import footer
from app.components.navbar import navbar
from app.states.videoteca_state import VideoItem, VideoState


def videos_header() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Videoteca",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h1(
                    rx.el.span("Canciones", class_name="block"),
                    rx.el.span(
                        "en video", class_name="block italic text-[#ff5a4e]"
                    ),
                    class_name="mt-5 font-serif text-5xl leading-[0.95] text-stone-50 sm:text-6xl lg:text-7xl",
                ),
                rx.el.p(
                    "Los videos mas relevantes publicados en el canal de Lorenly.",
                    class_name="mt-7 max-w-xl text-lg leading-relaxed text-stone-300",
                ),
                class_name="lg:col-span-7 lg:pr-12",
            ),
            rx.el.div(
                rx.el.p(
                    VideoState.total_count.to_string(),
                    class_name="font-serif text-6xl text-[#ff5a4e]",
                ),
                rx.el.p(
                    "piezas en la videoteca",
                    class_name="mt-2 text-[11px] uppercase tracking-[0.24em] text-stone-300",
                ),
                rx.el.p(
                    "Canciones con voces sintetizadas y colaboraciones.",
                    class_name="mt-3 text-sm text-stone-500",
                ),
                class_name="mt-12 border-l border-[#ff5a4e]/60 pl-6 lg:col-span-5 lg:mt-0",
            ),
            class_name="mx-auto grid w-full max-w-7xl grid-cols-1 items-start gap-6 px-6 pb-20 pt-16 lg:grid-cols-12",
        ),
        class_name="border-b border-white/10 bg-[#141110]",
    )


def videos_controls() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.label(
                "Buscar por título o artista",
                html_for="buscar-video",
                class_name="block text-[11px] uppercase tracking-[0.24em] text-stone-400",
            ),
            rx.el.div(
                rx.icon(
                    "search",
                    class_name="pointer-events-none absolute left-4 top-1/2 h-4 w-4 -translate-y-1/2 text-stone-500",
                ),
                rx.el.input(
                    id="buscar-video",
                    type="search",
                    placeholder="Ej. Silvana, Miku, Achirana…",
                    default_value=VideoState.query,
                    on_change=VideoState.set_query.debounce(300),
                    class_name="w-full border border-white/20 bg-[#1a1615] py-3 pl-11 pr-4 text-base text-stone-100 placeholder:text-stone-500 focus:border-[#ff5a4e] focus:outline-none focus:ring-1 focus:ring-[#ff5a4e]",
                ),
                class_name="relative mt-3",
            ),
            class_name="w-full lg:max-w-sm",
        ),
        class_name="flex flex-col gap-8 border border-white/10 bg-[#1a1615] p-6",
    )


def _video_frame(video: VideoItem) -> rx.Component:
    return rx.el.div(
        rx.el.iframe(
            src=video["embed"],
            title=f"Video de {video['title']}",
            loading="lazy",
            allow="accelerometer; clipboard-write; encrypted-media; picture-in-picture",
            allow_full_screen=True,
            class_name="absolute inset-0 h-full w-full border-0",
        ),
        class_name="relative aspect-video w-full bg-black",
    )


def _video_thumb(video: VideoItem) -> rx.Component:
    return rx.el.button(
        rx.el.img(
            src=video["thumb"],
            alt=f"Miniatura del video {video['title']}",
            loading="lazy",
            referrer_policy="no-referrer",
            class_name="absolute inset-0 h-full w-full object-cover grayscale-[25%] group-hover:grayscale-0 transition-all duration-500",
        ),
        rx.el.span(
            rx.icon("play", class_name="h-6 w-6 text-[#141110]"),
            class_name="relative flex h-14 w-14 items-center justify-center rounded-full bg-[#ff5a4e] group-hover:bg-[#ff7468] transition-colors",
        ),
        on_click=lambda: VideoState.play(video["key"]),
        aria_label=f"Reproducir {video['title']} de {video['artist']}",
        class_name="group relative flex aspect-video w-full items-center justify-center overflow-hidden bg-[#1c1817] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#ff5a4e]",
    )


def _video_card(video: VideoItem, **props) -> rx.Component:
    return rx.el.article(
        rx.cond(
            VideoState.playing.contains(video["key"]),
            _video_frame(video),
            _video_thumb(video),
        ),
        rx.el.div(
            rx.el.h3(
                video["title"],
                class_name="mt-2 font-serif text-2xl leading-snug text-stone-50",
            ),
            rx.el.p(video["artist"], class_name="mt-1 text-sm text-stone-400"),
            rx.el.div(
                rx.cond(
                    VideoState.playing.contains(video["key"]),
                    rx.el.button(
                        rx.icon("eye-off", class_name="h-4 w-4"),
                        "Ocultar reproductor",
                        on_click=lambda: VideoState.stop(video["key"]),
                        class_name="flex items-center gap-2 text-[11px] uppercase tracking-[0.18em] text-stone-400 hover:text-[#ff5a4e] transition-colors",
                    ),
                    rx.el.button(
                        rx.icon("play", class_name="h-4 w-4"),
                        "Reproducir aquí",
                        on_click=lambda: VideoState.play(video["key"]),
                        class_name="flex items-center gap-2 text-[11px] uppercase tracking-[0.18em] text-stone-300 hover:text-[#ff5a4e] transition-colors",
                    ),
                ),
                rx.el.a(
                    rx.icon("arrow-up-right", class_name="h-4 w-4"),
                    "Ver en YouTube",
                    href=video["external"],
                    target="_blank",
                    rel="noopener noreferrer",
                    aria_label=f"Ver {video['title']} en YouTube",
                    class_name="flex items-center gap-2 text-[11px] uppercase tracking-[0.18em] text-stone-400 hover:text-[#ff5a4e] transition-colors",
                ),
                class_name="mt-5 flex flex-wrap items-center gap-x-6 gap-y-3 border-t border-white/10 pt-4",
            ),
            class_name="p-5",
        ),
        class_name="flex flex-col border border-white/10 bg-[#1a1615] hover:border-[#ff5a4e]/50 transition-colors",
        **props,
    )


def videos_empty() -> rx.Component:
    return rx.el.div(
        rx.icon("video-off", class_name="h-8 w-8 text-[#ff5a4e]"),
        rx.el.p(
            "No encontramos videos",
            class_name="mt-4 font-serif text-2xl text-stone-50",
        ),
        rx.el.p(
            "Prueba con otro título o artista.",
            class_name="mt-2 max-w-md text-sm text-stone-400",
        ),
        rx.el.button(
            rx.icon("rotate-ccw", class_name="h-4 w-4"),
            "Ver toda la videoteca",
            on_click=VideoState.clear_filters,
            class_name="mt-6 flex items-center gap-2 bg-[#ff5a4e] px-5 py-3 text-[11px] uppercase tracking-[0.18em] text-[#141110] hover:bg-[#ff7468] transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white",
        ),
        class_name="flex flex-col items-center justify-center border border-dashed border-white/20 bg-[#1a1615] px-6 py-20 text-center",
    )


def videos_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            videos_controls(),
            rx.el.div(
                rx.el.p(
                    rx.el.span(
                        VideoState.filtered_count.to_string(),
                        class_name="font-serif text-2xl text-stone-50",
                    ),
                    rx.el.span(
                        f" de {VideoState.total_count} videos",
                        class_name="text-sm text-stone-400",
                    ),
                    class_name="flex items-baseline gap-2",
                ),
                rx.cond(
                    VideoState.is_filtered,
                    rx.el.button(
                        rx.icon("x", class_name="h-4 w-4"),
                        "Limpiar filtros",
                        on_click=VideoState.clear_filters,
                        class_name="flex items-center gap-2 text-[11px] uppercase tracking-[0.18em] text-stone-400 hover:text-[#ff5a4e] transition-colors",
                    ),
                    rx.fragment(),
                ),
                class_name="mt-12 flex flex-wrap items-center justify-between gap-4 border-b border-white/10 pb-4",
                aria_live="polite",
            ),
            rx.cond(
                VideoState.has_results,
                rx.el.div(
                    rx.foreach(
                        VideoState.filtered_videos,
                        lambda video: _video_card(video, key=video["key"]),
                    ),
                    class_name="mt-10 grid grid-cols-1 gap-6 sm:grid-cols-2 xl:grid-cols-3",
                ),
                rx.el.div(videos_empty(), class_name="mt-10"),
            ),
            class_name="mx-auto w-full max-w-7xl px-6 py-20",
        ),
        id="videoteca",
        class_name="bg-[#141110]",
    )


def canciones_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(videos_header(), videos_section()),
        footer(),
        class_name="min-h-screen bg-[#141110] font-['Inter'] antialiased selection:bg-[#ff5a4e] selection:text-[#141110]",
    )
