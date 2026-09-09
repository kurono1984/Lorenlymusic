from typing import TypedDict

import reflex as rx

YOUTUBE_EMBED = "https://www.youtube-nocookie.com/embed/"
YOUTUBE_WATCH = "https://www.youtube.com/watch?v="


class VideoItem(TypedDict):
    key: str
    title: str
    artist: str
    embed: str
    external: str
    thumb: str


VIDEO_SOURCES: list[tuple[str, str, str]] = [
    ("OrPIl5IJ4fA", 'Silvana & Ernesto - "Sí"', "Silvana y Ernesto"),
    ("TRwN0MwPUJE", "Luna a cuestas (feat Hatsune Miku)", "Lorenly"),
    ("xfl9sL0TyAM", "Cactus Triste (feat Maika & Megpoid)", "Lorenly"),
    ("-CJbaF69YPo", "Luz (feat Megpoid Gumi)", "Lorenly"),
    ("RczjTRbr4x4", "Harawikunaq Wasin (feat Megpoid)", "Lorenly"),
    ("YZ4RPaGOyKo", "Fly Away (feat Megpoid English)", "Fleur Du Vent"),
    (
        "_erOnyjtqT4",
        "Natividad (feat. Hatsune Miku, Megpoid Gumi, Kagamine Rin)",
        "Lorenly & Subliminal Sound Engine",
    ),
    ("_ITVlfs1t04", "秘密の水 · Himitsu no Mizu (feat Megpoid)", "Lorenly"),
    (
        "UDx04id7wac",
        "Life / Mi vida sin tu amor (feat Hatsune Miku)",
        "Lorenly",
    ),
    ("_WZ5Pw0EYjI", "Cálida Esperanza (feat Megpoid)", "Lorenly"),
    ("Rmjxdd_Y_8w", "Corazón de Fuego (feat Len Kagamine)", "Lorenly"),
    (
        "iDDkUrZzKiI",
        "Rosas Frescas en tu Puerta (feat Silvana Aritani)",
        "Lorenly",
    ),
    ("9bXmMol4JaA", "El cóndor pasa (feat Megpoid)", "Lorenly"),
    ("1IaHtOrKDDg", "Días grises, días de color (feat Maika)", "Lorenly"),
    ("lf9KkoPaYAQ", "Sujétate de mi (feat Tohoku Zunko)", "Lorenly"),
    (
        "sQXCX_vmFj0",
        "A las 2:30 pm (feat Hatsune Miku & Subliminal Sound Engine)",
        "Lorenly",
    ),
    ("RLM3ylQlC48", "La Achirana", "Lorenly"),
]


def build_video(video_id: str, title: str, artist: str) -> VideoItem:
    return {
        "key": video_id,
        "title": title,
        "artist": artist,
        "embed": f"{YOUTUBE_EMBED}{video_id}",
        "external": f"{YOUTUBE_WATCH}{video_id}",
        "thumb": f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg",
    }


class VideoState(rx.State):
    """Videoteca real publicada en el canal de Lorenly."""

    query: str = ""
    playing: list[str] = []

    videos: list[VideoItem] = [
        build_video(video_id, title, artist)
        for video_id, title, artist in VIDEO_SOURCES
    ]

    @rx.var
    def total_count(self) -> int:
        return len(self.videos)

    @rx.var
    def filtered_videos(self) -> list[VideoItem]:
        text = self.query.strip().lower()
        result: list[VideoItem] = []
        for video in self.videos:
            if (
                text
                and text not in video["title"].lower()
                and text not in video["artist"].lower()
            ):
                continue
            result.append(video)
        return result

    @rx.var
    def filtered_count(self) -> int:
        return len(self.filtered_videos)

    @rx.var
    def has_results(self) -> bool:
        return len(self.filtered_videos) > 0

    @rx.var
    def is_filtered(self) -> bool:
        return bool(self.query.strip())

    @rx.event
    def set_query(self, value: str):
        self.query = value

    @rx.event
    def clear_filters(self):
        self.query = ""

    @rx.event
    def play(self, key: str):
        if key not in self.playing:
            self.playing.append(key)

    @rx.event
    def stop(self, key: str):
        if key in self.playing:
            self.playing.remove(key)
