﻿# Определение персонажей игры.
# Персонажи-минутки
define m = Character('Мама')
define sistem = Character('Система')
define s = Character('Соседка?')
define s1 = Character('Сосед 1')
define s2 = Character('Сосед 2')
define kl = Character('Елена Васильевна')

# Второстепенные персонажи
define kom = Character('Галина Олеговна')
define v = Character('Ваня')
define vd = Character('Ваcя')

# Главные герои
define mc = Character('Рома')
define a = Character('Алиса')
define o = Character('Олег')

#Персонажи в телефоне
define mc_nvl = Character("Рома", kind=nvl, image="mc", callback=Phone_SendSound)
define Vanya_nvl = Character("Ваня", kind=nvl, callback=Phone_ReceiveSound)
define kl_nvl = Character("Елена Васильевна", kind=nvl)

# Определение Бэков.
image bedroom_Irk = im.Scale("bg/bedroom_Irk.png",1920,1080)

#просто обновить картинки, меняя только файлы в папке, оставляя такое же название. ai на картинке я уберу
image coridorday = im.Scale("bg/bg upd/coridor_day.png",1920,1080) #Коридор день
image coridorev = im.Scale("bg/coridor_ev.png",1920,1080) #Коридор вечер
image coridornight = im.Scale("bg/bg upd/coridor_night.png",1920,1080) #Коридор ночь

image room_511_night = im.Scale("bg/bg upd/511_night.png", 1920, 1080)
image room_511_night_pent = ("bg/bg upd/511_night_pent.png")
image room_511_day = im.Scale("bg/bg upd/511_day.png",1920,1080)

image room_510_bed_night  = im.Scale("bg/bg upd/510_day.png",1920,1080) #сменить на ночной
image room_510_bed_day  = im.Scale("bg/bg upd/510_day.png",1920,1080)


#градиент и виньетки

image gradient = "bg/bg upd/blackgradient.png"  # Ваш файл градиента

#     im.MatrixColor(
#         "bg/bg upd/blackgradient.png",  # Исходное изображение
#         # Умножаем альфа-канал (чтобы черные области стали прозрачными)
#         # и добавляем затемнение (например, умножая на 0.5 в темных зонах)
#         matrixcolor Matrix(
#             # R, G, B, A (альфа)
#             [1.0, 0.0, 0.0, 0.0,  # Красный канал
#             0.0, 1.0, 0.0, 0.0,   # Зеленый канал
#             0.0, 0.0, 1.0, 0.0,   # Синий канал
#             0.0, 0.0, 0.0, 0.5]  # Альфа-канал (уменьшаем прозрачность там, где маска черная)
#         )
#     )
#     # Делаем плавное появление
#     alpha 0.0
#     linear 2.0 alpha 1.0
#     repeat

# Определение Спрайтов Алисы.
image Alice_normal = im.Scale("sprites/Alice/Alice_normal.png",559,946)
image Alice_smile = im.Scale("sprites/Alice/Alice_smile.png",559,946)
image Alice_talk = im.Scale("sprites/Alice/Alice_talk.png",559,946)
image Alice_discontent = im.Scale("sprites/Alice/Alice_discontent.png",559,946) #недовольна
image Alice_surprise = im.Scale("sprites/Alice/Alice_surprise.png",559,946) #удивлена
image Alice_smirk = im.Scale("sprites/Alice/Alice_smirk.png",559,946) #Ухмыляется
image Alice_roll_eyes = im.Scale("sprites/Alice/Alice_roll_eyes.png",559,946) #Закатила глаза
image Alice_sulk = im.Scale("sprites/Alice/Alice_sulk.png",559,946) #Надула щёки
image Alice_angry = im.Scale("sprites/Alice/Alice_angry.png",559,946)
image Alice_fear = im.Scale("sprites/Alice/Alice_fear.png",559,946)
image Alice_before_cry = im.Scale("sprites/Alice/Alice_before_cry.png",559,946)
image Alice_cry = im.Scale("sprites/Alice/Alice_cry.png",559,946)

# Определение эффекта сердцебиения НУЖНО ДОПИЛИТЬ ЗАТЕМНЕНИЕ
transform heartbeat_advanced:
    # Пульсация + дрожание
    parallel:
        zoom 1.0
        ease 0.15 zoom 1.03
        ease 0.3 zoom 0.99
        ease 0.15 zoom 1.02
        ease 0.4 zoom 1.0
        repeat
    parallel:  # Добавляем вибрацию
        xoffset 0
        ease 0.05 xoffset 3
        ease 0.05 xoffset -3
        ease 0.05 xoffset 0
        repeat

#     parallel:
#         # Создаем черный круг с прозрачным центром
#         mesh True
#         #shader """
#             #vec4 vignette(vec2 uv) {
#                 #float d = distance(uv, vec2(0.5, 0.5));
#                 #float radius = 0.5;
#                 #float softness = 0.02;
#                 #float alpha = smoothstep(radius, radius-softness, d);
#                 #return vec4(0.0, 0.0, 0.0, (1.0 - alpha) * 0.7);
#             #}
#             #uniform float u_alpha;
#             #vec4 effect(vec4 color, Image texture, vec2 uv, vec2 screen_coords) {
#                 #return vignette(uv) * u_alpha;
#             #}
#         #"""
#         alpha 0.0  # Начальная прозрачность
#         #Синхронизация с сердцебиением
#         ease 0.15 alpha 0.4  # Пик затемнения при ударе
#         ease 0.3 alpha 0.1   # Ослабление
#         ease 0.15 alpha 0.3  # Второй удар
#         ease 0.4 alpha 0.0   # Возврат к прозрачности
#         repeat

    #scene ***** at heartbeat_advanced
    #play sound "heartbeat.wav" loop

# Игра начинается здесь (день 1):
label start:
    ##Картинка-переход 17.06.2024, родной город ГГ
    scene bedroom_Irk with dissolve

    m "ДА КАКОЕ ЖЕ ТЫ НЕБЛАГОДАРНОЕ ГОВ-..."
    play sound "door.mp3"
    with hpunch
    with vpunch

    "Как же мне это осточертело. Постоянно споры, ссоры. А главное, из-за всякой херни!"
    "Ох... ладно..."

    play sound "vk.mp3"
    "*бззз*"
    nvl_narrator "11A"
    kl_nvl "Ребята, пришли результаты ЕГЭ по информатике! Хвастайтесь!"
    "Вовремя блин…"
    "Ладно... посмотрим, что тут у нас..."
    #*Можно нарисовать арт с ноутом, где будут отображены госуслуги или чекегэ*
    "Таак… получается в сумме 253... Ну, как я и ожидал..."
    "*Пока я взглянул на вид из окна, и плавно перевел взгляд на дверь, в моей голове уже возникло точное решение.*"
    "К черту. Здесь я учиться точно не намерен."
    "Но куда тогда поступать? Едва ли моих баллов хватит на московский или питерский ВУЗ..."
    "Пу-пу-пу... Думаю... Да, наверное мне стоит просто написать кому-нибудь из кентов."

    #Разговор реализован в телефоне
    nvl clear
    nvl_narrator "Вано"

    mc_nvl "Вань, здаров. Видел уже свои результаты? Куда поступать планируешь?"
    Vanya_nvl "Привет! У меня 247. Буду кидать оригиналы в Томский Политех. У тебя что по планам?"
    mc_nvl "Да я думаю вот, куда мне податься. 253 балла. Ты же на программную инженерию?"
    Vanya_nvl "Yep. Помчали со мной в Томск? Там общагу всем дают, и стипендия около десятки высокобалльникам, как мы."
    mc_nvl "Нуу..."
    "Предложение конечно интересное, но... Томск?"
    mc_nvl "Я подумаю еще, но в ТПУ копию кину."
    Vanya_nvl "Окей. Жду вестей!"
    "*Я откатился от компьютерного стола и начал обдумывать план дальнейших действий*"
    "Политех значит... Ну, не то чтобы у меня было много вариантов..."
    "Ладно, посмотрим, что тут у нас..."

    scene black with dissolve
    "Картинка-переход 10.07.2024, родной город Романа"
    #10.07.2024, родной город ГГ
    scene bedroom_Irk with dissolve
    #На экране ноутбука рандомный видосик с ютуба
    play sound "vk.mp3"
    "*бззз*"
    nvl clear
    nvl_narrator "11A"
    kl_nvl "Ребята, здравствуйте! Как у вас дела? В какие ВУЗы подали документы?"
    "Точно. Сегодня же оригиналы уже надо подать…"
    #На экране появляется заставка Госуслуг
    "*Я открыл Госуслуги и начал проверять свои заявления в ВУЗы*"
    "Ну, как я и думал, о Москве можно и не мечтать..."
    "А вот Томск ждет меня с распростертыми объятиями, ха..."
    "Ладно... Видимо придется все же сделать выбор."
    menu:
        "ТПУ":
            scene black with dissolve
            jump TPU3108
        "ТУСУР":
            sistem "НУ И ВАЛИ В СВОЙ ТУСУР."
            return
            #pass
            #КНОПКА None(Null action) ОТКАЗЫВАЕТСЯ РАБОТАТЬ Я НЕ МОГУ Я ПРОСИДЕЛ С ЭТОЙ ФИГНЕЙ ЧАСА 2
#Картинка-переход (дата)

#Тут должен быть кусок сюжета (Вставка из новостей, переживания ГГ)

# Игрок выбрал поступить в ТПУ, 31.08:
label TPU3108:
    "Картинка-переход 31.08.2024, Томск, общежитие №14"
    $ rep = 0
    scene coridorev with dissolve #поменять на день
    kom "Так, смотри, дубликат ключа надо сделать. Оригиналом. Я его дам.\
    Дубликат делает ключник. Он находится возле шаурмечки. Ключнику нужны деньги. Денег я не дам."
    "У меня стойкое ощущение дежавю..."
    kom "Держи-"
    "*Галина Олеговна протянула мне небольшой ключик. На бирке было написано «511»*"
    kom "Копию сделаешь, желательно сегодня, и сдашь его мне. Или на вахте оставишь."
    mc "Добро. Как сделаю копию – сразу к вам."
    "*Коменда одобрительно кивнула и повела меня к 511 комнате.*"
    "Комнате, где я, вероятно, проживу следующие 4 года..."

    "*Мы уже почти подошли к моей новой комнате, как вдруг… *"
    show Alice_normal with dissolve
    "*Из 510 комнаты вышла девушка, видимо, моя соседка.*"
    hide Alice_normal
    show Alice_talk
    s "О! Здрасте, Галин Олеговна. А я к вам как раз"
    hide Alice_talk
    show Alice_normal
    kom "Ой, здравствуй Алиса! Сейчас, я заселю человека... Твой сосед кстати, в 511 будет жить."
    "*Алиса перевела взгляд на меня и улыбнулась.*"
    hide Alice_normal
    show Alice_talk
    a "Привет! Меня Алиса зовут. Алиса Михайлова."
    "*Алиса протянула мне руку.*"
    menu:
        "*Улыбнуться в ответ и ответить на рукопожатие* Очень приятно. Я Рома.":
            $ rep+=1
            a "Взаимно. Рома, не прощаюсь, думаю сегодня ещё увидимся."
            a "Галина Олеговна, жду вас у кабинета."
            hide Alice_talk
            show Alice_normal
            hide Alice_normal with moveoutright
            "*Алиса поспешно удалилась.*"
            "*Коменда одобрительно на меня посмотрела.*"
            mc "Галина Олеговна, я пойду. Мне ещё дубликат надо успеть сделать."
            kom "Рома, я так подумала. Можешь не торопиться. 511 уже укомплектована, ключ пока не нужен.\
            Поэтому вернешь, как сделаешь."
            mc "Спасибо. Ладно, я пойду. Знакомиться с соседями."
            "*Я быстро прошмыгнул в свое новое жилье.*"

        "*Ответить на рукопожатие* Ага. Роман.":
            hide Alice_talk
            show Alice_discontent with dissolve
            "*Алиса посмотрела на меня, как будто хотела что-то добавить, однако в итоге промолчала.*"
            a "Галин Олеговна, я вас у кабинета подожду."
            hide Alice_discontent with moveoutright
            "*Алиса поспешно удалилась.*"
            kom "Зря ты так, она же к тебе по доброму."
            mc "Галина Олеговна, я пойду. Мне ещё дубликат делать."
            "*Пока коменда не успела опомниться, я быстро прошмыгнул в свое новое жилье.*"
    scene room_511_day with dissolve #ЗАГЛУШКА+-
    "*Зайдя внутрь комнаты, я не был удивлен. Вполне обычная студенческая комната, как я себе и представлял*"
    #Show Oleg_normal
    s1 "О, свежая кровь. Приветствую, как звать?"
    #Show Vanya
    v "Окак, и ты здесь! Здарова, Ром."
    if rep == 1:
        scene black with dissolve
        jump Sep1time419Alice
    else:
        return
label Sep1time419Alice:
    "Картинка-переход 01.09.2024, Общежитие №14, комната 510"
    "Таймскип"
    scene room_510_bed_day with dissolve
    mc "Агх..."
    "*Невольно, мои руки моментально прикоснулись к голове*"
    mc "Нда... Видать вчера я все-таки перебрал..."
    mc "Где это я? Сколько сейчас времени?"
    "*Мои глаза пробежались по комнате*"
    mc "А, точно..."
    "*Голову, кажется, стало потихноньку отпускать*"
    scene room_510_bed_night
    "*Я заметил Алису, мирно посапывающую в своей постели*"
    "*Достав свой телефон я посмотрел на красующиеся там цифры. 4.19*"
    "*Аккуратно, чтобы не разбудить свою новую знакомую, я поднялся с кровати и побрел в нашу с парнями комнату*"
    scene coridornight with dissolve  #поменять на ночной корридор
    "Интересный у меня первый день в этом городе получился, ничего не скажешь…"
    scene black
    "Ладно, щас водички попить и…- {nw}"

    scene room_511_night_pent
    play music "spook.ogg"
    pause
    mc "AAAAAA...-"
    "*За дверью, я узрел ужасающую картину: Комната была в полнейшем беспорядке, на стенах была размазана кровь, а на полу начерчена пентаграмма*"
    "*Я быстро захлопнул дверь и отпрыгнул от неё*"
    scene coridornight at heartbeat_advanced
    play sound "heartbeat.mp3" loop
    show gradient:
        alpha 0.0
        linear 0.6 alpha 0.5
        linear 0.6 alpha 0.0
        repeat
    with hpunch
    with vpunch

    "*Сердце бешено колотилось*"
    "КАКОГО!?"

    #stop music fadein (0.5)

