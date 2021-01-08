from django.core.management.base import BaseCommand, CommandError
from emanagement.models import Book, BookAuthor, BookPublish, Genre
from django.core.files.base import ContentFile
import faker
import requests
import uuid

class Command(BaseCommand):
    help = 'This Make fake data for you...'
    requires_migrations_checks = True


    def add_arguments(self, parser):
        parser.add_argument('-number', '--n', type=int,
                            help='A Number for Data.', default=1)

    def handle(self, *args, **kwargs):
        for _ in range(kwargs['n']):
            try:
                f = faker.Faker()
                genre = Genre.objects.filter(
                    name__in=f.random_elements(
                        [i[0] for i in Genre.name.field.choices[1:]], length=f.random_int(
                            min=1, max=30),
                        unique=True)
                )
                publish, _ = BookPublish.objects.get_or_create(
                    company_name=f.company(), website=f"http://{f.domain_name()}")
                publish.genre.set([*genre])
                author, _ = BookAuthor.objects.get_or_create(
                    first_name=f.first_name(),
                    middle_name=f.first_name(),
                    last_name=f.last_name(),
                    date_of_birth=f.date_of_birth(),
                    died=f.date_this_year(),
                    aboutAuthor=f.paragraph(nb_sentences=5)
                )
                author.genre.set([*genre])
                author.profile.save(f'{uuid.uuid4()}.jpg', ContentFile(
                        requests.get('https://picsum.photos/200').content))
                _, book = Book.objects.get_or_create(
                    name=f.name(),
                    author=author,
                    publish=publish,
                    # publish_date=f.date(),
                    language=f.random_element([i[0] for i in Book.language.field.choices[1:]]),
                    edition=f.random_element([i[0] for i in Book.edition.field.choices[1:]]),
                    cost=f.pydecimal(
                        right_digits=2, positive=True, min_value=100, max_value=9999
                    ),
                    page=f.pyint(),
                    description=f.paragraph(nb_sentences=10),
                    stock=f.pyint(),
                    rating=f.pydecimal(right_digits=1, positive=True,
                                        min_value=0, max_value=10),
                )
                if book:
                    _.genre.set([*genre][:f.random_int(max=9)])
                    _.save()
                    _.profile.save(f'{uuid.uuid4()}.jpg', ContentFile(
                        requests.get('https://picsum.photos/200/300').content))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"{e}"))
                kwargs['n'] -= 1
        if kwargs['n'] > 0:
            self.stdout.write(self.style.SUCCESS(
            f'{kwargs["n"]} Books is Created...'))