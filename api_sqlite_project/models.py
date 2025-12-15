from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Movie(Base):
    __tablename__ = "movies"

    movieId: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    genres: Mapped[str]


class Link(Base):
    __tablename__ = "links"

    movieId: Mapped[int] = mapped_column(primary_key=True)
    imdbId: Mapped[str]
    tmdbId: Mapped[str]


class Rating(Base):
    __tablename__ = "ratings"

    # prosty klucz główny sztuczny, żeby było łatwo
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    userId: Mapped[int]
    movieId: Mapped[int]
    rating: Mapped[float]
    timestamp: Mapped[int]


class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    userId: Mapped[int]
    movieId: Mapped[int]
    tag: Mapped[str]
    timestamp: Mapped[int]
