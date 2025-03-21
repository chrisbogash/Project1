from faker import Faker
from application.app import init_app
from application.database import User, db

app = init_app()

def create_faker_users():
    faker = Faker('en')
    Faker.seed(4321)
    user_list = []
    number_of_users = 6

    with app.app_context():
        for i in range(number_of_users):
            user = User()
            user.name = faker.name()
            user.password = faker.password()
            user.email = faker.email()
            user.phone = faker.phone_number()
            user.address = faker.address()
            user_list.append(user)

        db.session.add_all(user_list)
        db.session.commit()

if __name__ == "__main__":

    with app.app_context():
        create_faker_users()
        # User.query.delete()
        # db.session.commit()
        for p in User.query.all():
            print(p.name, p.id)
