from database import Category, get_session, Film

session = get_session()
category: Category = session.query(Category).get(1)
film: Film = session.query(Film).get(3)
print(category)
print(film)
# film.category = category
# film.category_id = category.id
# session.commit()
# category.films.append(film)
# session.commit()
