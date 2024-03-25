import vk_api
import xlsxwriter

# Авторизация в ВКонтакте
token = ''
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

def get_friends_by_id(id):
    return vk.friends.get(user_id=id)['items']

def get_info_by_id(id):
    return vk.users.get(user_id=id, fields='city,bdate,counters, education,has_photo,last_seen,sex,status')

def write_users_in_excel(users):
    workbook = xlsxwriter.Workbook('users2.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, 'ID')
    worksheet.write(0, 1, 'Имя Фамилия')
    worksheet.write(0, 2, 'Дата Рождения')
    worksheet.write(0, 3, 'Статус')
    worksheet.write(0, 4, 'Пол')
    worksheet.write(0, 5, 'Город')
    worksheet.write(0, 6, 'Кол-во друзей')
    worksheet.write(0, 7, 'Кол-во подарков')
    i = 1
    for item in users:
        item = item[0]

        worksheet.write(i, 0, item["id"])
        worksheet.write(i, 1, item["first_name"] + " " + item["last_name"])
        if 'bdate' in item:
            worksheet.write(i, 2, item["bdate"])
        if 'status' in item:
            worksheet.write(i, 3, item["status"])

        if 'sex' in item:
            if item['sex'] == 1:
                worksheet.write(i, 4, "Жен")
            else:
                worksheet.write(i, 4, "Муж")

        if "city" in item:
            worksheet.write(i, 5, item["city"]['title'])

        if 'counters' in item:
            if "friends" in item['counters']:
                worksheet.write(i, 6, item['counters']['friends'])

            if "gifts" in item['counters']:
                worksheet.write(i, 7, item['counters']['gifts'])

        i += 1
    workbook.close()

user_id = "dj_sabnock"
user = vk.users.get(user_ids=user_id, fields='nickname')
friends = vk.friends.get(user_id=493562022)['items']
friends_info = []


x = 1
for i in friends[0:1000]:
    print(f"{x/1000*100}%")
    friends_info.append(get_info_by_id(i))
    x+=1
write_users_in_excel(friends_info)