
def person_profile(**kwargs):

    return f"Имя: {kwargs['name']}, Фамилия: {kwargs['surname']}, E-mail: {kwargs['email']}"

print(person_profile(name="Dmitrii", surname="Bykov", email="dobhran@mail.ru"))