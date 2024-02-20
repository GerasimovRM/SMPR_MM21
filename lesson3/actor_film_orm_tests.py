from database import Category, get_session, Film, Actor, FilmActor
from sqlalchemy import and_

session = get_session()


film: Film = session.query(Film).get(1)
actor: Actor = session.query(Actor).get(1)
# CREATE
# 1
# film_actor = FilmActor(actor_id=actor.id, film_id=film.id)
# session.add(film_actor)
# 2
# film_actor = FilmActor(film=film, actor=actor)
# session.add(film_actor)
# 3
# film_actor = FilmActor(film=film)
# film_actor.actor_id = actor.id
# session.add(film_actor)
# 4
# film_actor = FilmActor(film=film, actor=actor)
# film.film_actors.append(film_actor)
# session.commit()

# GET
film_actor = session.query(FilmActor).get((3, 1))
print(film_actor)
film_actor = session.query(FilmActor).where(and_(FilmActor.actor_id == 1, FilmActor.film_id == 3)).first()
print(film_actor)

# DELETE
# film_actor = session.query(FilmActor).get((3, 1))
# session.delete(film_actor)
# session.commit()

# 1
films_by_actor = []
for film_actor in film.film_actors:
    films_by_actor.append(film_actor.film)
print(films_by_actor)
# 2
print(list(map(lambda film_actor: film_actor.film, film.film_actors)))



