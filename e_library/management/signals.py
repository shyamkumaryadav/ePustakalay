import data_list

def create_genre(sender, *args, **kwargs):
    for i in data_list.BOOK_GENRE:
        obj, _ = sender.models['genre'].objects.get_or_create(name=i[0])
        if _:
            print('Y ', end="\t")
    else:
        pass