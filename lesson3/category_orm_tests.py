from database import Category, get_session

session = get_session()
categories = session.query(Category).all()
print(categories)
for category in categories:
    print(category)
category: Category = session.query(Category).get(1)
print(category)
print(category.films[0].title)
category = session.query(Category).where(Category.id == 3).one()
print(category)

# new_category = Category(title="психодел")
# session.add(new_category)
# session.commit()

category = session.query(Category).where(Category.id == 10).one()
category.title = "детские"
session.commit()

category = session.query(Category).where(Category.id == 10).one()
session.delete(category)
session.commit()



session.close()
