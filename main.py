import file_operations
import random
from faker import Faker
fake = Faker("ru_RU")


def main():
    for i in range(1, 11):
        skills = [
          "Стремительный прыжок",
          "Электрический выстрел",
          "Ледяной удар",
          "Стремительный удар",
          "Кислотный взгляд",
          "Тайный побег",
          "Ледяной выстрел",
          "Огненный заряд"
        ]
        skills_random = random.sample(skills, 3)
        skill_1 = skills_random[0]
        skill_2 = skills_random[1]
        skill_3 = skills_random[2]
        run_dict = {
          'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
          'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
          'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
          'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
          'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
          'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
          'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
          'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
          'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
          'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
          'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
          'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
          'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
          'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
          'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
          'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
          'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
          'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
          'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
          'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
          'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
          'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
          ' ': ' '
        }
        for key in run_dict.keys():
            skill_1 = skill_1.replace(key, str(run_dict[key]))
            skill_2 = skill_2.replace(key, str(run_dict[key]))
            skill_3 = skill_3.replace(key, str(run_dict[key]))
        file_name = 'cards/file{}.svg'.format(i)
        context = {
          "first_name": fake.first_name_male(),
          "last_name": fake.last_name_male(),
          "job": fake.job(),
          "town": fake.city(),
          "strength": random.randint(3, 18),
          "agility": random.randint(3, 18),
          "endurance": random.randint(3, 18),
          "intelligence": random.randint(3, 18),
          "luck": random.randint(3, 18),
          "skill_1": skill_1,
          "skill_2": skill_2,
          "skill_3": skill_3
        }
        file_operations.render_template("charsheet.svg", file_name, context)


if __name__ == '__main__':
    main()
 
