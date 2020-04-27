class Disc:

    def __init__(self, id_disc=-1, title="", performer="", music_style="", tracks=0, email="",
                 price=0.0):
        self.id_disc = id_disc
        self.title = title
        self.performer = performer
        self.music_style = music_style
        self.tracks = tracks
        self.email = email
        self.price = price
        return

    def to_string(self):
        text = ("id: {:d} - Titulo: {} - Interprete: {} - Estilo: {} - Número de pistas: {:d} - "
                "Precio: {:.2f} - email: {}")
        text = text.format(self.id_disc, self.title, self.performer, self.music_style, self.tracks,
                           self.price, self.email)
        return text
