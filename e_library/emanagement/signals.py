import data_list

def create_genre(sender, *args, **kwargs):
    is_create = False
    for i in data_list.BOOK_GENRE:
        _, create = sender.models['genre'].objects.get_or_create(name=i[0])
        if create:
            print('Y', end="")
            is_create = True
    if is_create:        
        print(f"\n------------------Done---------------------")