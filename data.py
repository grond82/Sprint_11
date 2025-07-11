class Data:
    MESSAGE_CREATE_SAME_COURIER = "Почта уже используется"
    AUTHORIZATION_DATA_FULL = {'email': 'timo123@yandex.ru', 'password': '1234'}
    DATA_ADVERT_1 = {'name': 'Tim1982_Auto',
                     'category': 'Авто',
                     'condition': 'Новый',
                     'city': 'Москва',
                     'description': 'Description',
                     'price': '200',
                     'images': ('avatar.jpeg', open('C:\Projects\\avatar.jpeg', 'rb'), 'image/jpeg')
                     }
    DATA_UPDATE_ADVERT_1 = {'name': 'Tim1982_Auto_1',
                     'category': 'Книги',
                     'condition': 'Б/У',
                     'city': 'Новосибирск',
                     'description': 'Description + Desc',
                     'price': '20025',
                     'images': ('eye.jpeg', open('C:\Projects\\eye.jpeg', 'rb'), 'image/jpeg')
                     }
    DATA_ADVERT_2 = {'name': 'TIm1982_Book', 'category': 'Книги', 'condition': 'Б/У', 'city': 'Санкт-Петербург', 'description': 'Description', 'price': '30'}
    DATA_ADVERT_3 = {'name': 'TIm1982_Garden', 'category': 'Садоводство', 'condition': 'Новый', 'city': 'Москва', 'description': 'Description', 'price': '200'}
    DATA_ADVERT_4 = {'name': 'TIm1982_Hobby', 'category': 'Хобби', 'condition': 'Новый', 'city': 'Москва','description': 'Description', 'price': '200'}
    DATA_ADVERT_5 = {'name': 'TIm1982_Techno', 'category': 'Технологии', 'condition': 'Новый', 'city': 'Москва','description': 'Description', 'price': '200'}
    MESSAGE_DELETE_ADVERT = "Объявление удалено успешно"
    ID_DIFFERENT_USER_ADVERT = "2222"
    MESSAGE_UPDATE_DIFFERENT_USER_ADVERT = "Оффер не найден или у вас нет прав на его редактирование"