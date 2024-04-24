#                        
#　　　　　　　　　　_,.. -──- ､,
#　　　　　　　　,　'" 　 　　　 　　 `ヽ.
#　　　　　　 ／/¨7__　　/ 　 　 i　 _厂廴
#　　　　　 /￣( ノ__/　/{　　　　} ｢　（_冫}
#　　　　／￣l＿// 　/-|　 ,!　 ﾑ ￣|＿｢ ＼＿_
#　　. イ　 　 ,　 /!_∠_　|　/　/_⊥_,ﾉ ハ　 イ 
#　　　/ ／ / 　〃ん心 ﾚ'|／　ｆ,心 Y　i ＼_＿＞　
#　 ∠イ 　/　 　ﾄ弋_ツ　　 　 弋_ﾂ i　 |　 | ＼
#　 _／ _ノ|　,i　⊂⊃　　　'　　　⊂⊃ ./　 !､＿ン
#　　￣　　∨|　,小、　　` ‐ ' 　　 /|／|　/
#　 　 　 　 　 Y　|ﾍ＞ 、 ＿ ,.　イﾚ|　 ﾚ'
#　　　　　　 r'.| 　|;;;入ﾞ亠―亠' );;;;;! 　|､
#　　　　　 ,ノ:,:|.　!|く　__￣￣￣__У　ﾉ|:,:,ヽ
#　　　　　(:.:.:.:ﾑ人!ﾍ　 　` ´ 　　 厂|ノ:.:.:丿 by @RomSTil

""" Приложение погоды на Flet """


#Модули
import flet
from flet import *
import requests
import  datetime


#Все входные данные из weather app 
user_data = "Tula"
API_Key = "8be419cae5fba5e8aa4f5c1dd81143a8"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={user_data}&appid={API_Key}&units=metric"
res = requests.get(URL).json()
temp = res['main']['temp']
wind = res['wind']['speed']
weather = res['weather'][0]['main']
description = res['weather'][0]['description']
humidity = res['main']['humidity']
city = res['name']
country = res['sys']["country"]
feels_like = res['main']['feels_like']
visibility = res['visibility'] / 1000




weather_image = ["", "Clear_sky.png", "Few_clouds.png", "Overcast_clouds.png", "Drizzle.png", "Rain.png", "Shower_rain.png", "Snow.png", "Mist.png"]
index = 1

if str(weather) == "Clear sky":
    index = 1
elif str(weather) == "Few clouds":
    index = 2
elif str(weather) == "Overcast clouds":
    index = 3
elif str(weather) == "Drizzle":
    index = 4
elif str(weather) == "Rain":
    index = 5
elif str(weather) == "Shower rain":
    index = 6    
elif str(weather) == "Snow":
    index = 7
elif str(weather) == "Mist":
    index = 8
else:
    print("Начался апокалипсис")
   

def _current_extra():
        _extra_info = []

        _extra = [
            [
                #Влажность
                int(res['visibility']) / 1000,
                "Km",
                "visibility",
                "visibility.png"
            ],
            [
                #Давление
                round(res['main']['pressure']) ,
                "inHg",
                "pressure",
                "barometer.png"
            ],
            [
                #Давление
                datetime.datetime.fromtimestamp(
                res['sys']['sunset']
                ).strftime("%I: %M %p"),
                "",
                "Sunset",
                "sunset.png"
            ],
            [
                #Давление
                datetime.datetime.fromtimestamp(
                res['sys']['sunrise']
                ).strftime("%I: %M %p"),
                "",
                "Sunrise",
                "Sunrise.png"
            ],

            ]

        for data in _extra:

                _extra_info.append(
                    Container(
                        bgcolor='white10',
                        border_radius=12,
                        alignment=alignment.center,
                        content=Column(
                            alignment='center',
                            horizontal_alignment="center",
                            spacing=25,
                            controls=[
                                 Container(
                                    alignment=alignment.center,
                                    content=Image(
                                        src=data[3],
                                        color='white',

                                    ),
                                    width=32, 
                                    height=32,
                                 ),
                                 Container(
                                      content=Column(
                                           alignment='center',
                                           horizontal_alignment="center",
                                           spacing=0,
                                           controls=[
                                            Text(
                                                str(
                                                    data[0]
                                                ) + " " + data[1], 
                                                size=14,
                                            ),
                                            Text(
                                                data[2], 
                                                size=11,
                                                color="white54"
                                            ),
                                           ]
                                      )
                                 )
                            ]
                        )
                    )
                )
        return _extra_info


def main(page: Page):
    page.horizontal_alignment='center'
    page.vertical_alignment='center'



    #анимация
    def _expand(e):
        if e.data == "true":
            _c.content.controls[0].height = 560
            _c.content.controls[0].update()
        else:
            _c.content.controls[0].height = 700 * 0.4
            _c.content.controls[0].update()
    

    
    # Основной контейнер
    def _top():
        # 

        
        

        _today_extra = GridView(
            max_extent=150,
            expand=1,
            run_spacing=5,
            spacing=5,
        )

        for info in _current_extra():
             _today_extra.controls.append(info)

       
        

        top = Container(
                width=310, 
                height= 700 * 0.40,
                gradient=LinearGradient(
                    begin=alignment.bottom_left,
                    end=alignment.top_right,
                    colors=["lightblue600", "lightblue900"]
                ),
                border_radius=35,
                animate=animation.Animation(
                    duration=350, 
                    curve = "decelerate"),
                    on_hover= lambda e: _expand(e),
                padding=15,
                content=Column(
                    alignment='start',
                    spacing=10,
                    controls=[
                        Row(
                            alignment='center',
                            controls=[
                                Text(
                                    f'{city}, {country},',
                                    size=16,
                                    weight="w500",
                                    color='white'
                                )
                            ],
                        ),
                        Container(padding=padding.only(bottom=5)),
                        Row(
                            alignment='center',
                            spacing=30,
                            controls=[
                                Column(
                                    controls=[
                                        Container(
                                            width=125,
                                            height=125,
                                            content=Image(
                                                src=weather_image[index],
                                                color="white",
                                            ),
                                        ),
                                    ]
                                ),
                                Column(
                                spacing=5,
                                horizontal_alignment='center',
                                controls=[
                                    Text(
                                        "Today",
                                        color='white',
                                        size=16,
                                        text_align='center',
                                    ),
                                    Row(
                                        vertical_alignment='start',
                                        spacing=0,
                                        controls=[
                                            Container(
                                                content=Text(
                                                    #для requests
                                                    round(temp),
                                                    size = 52
                                                ),
                                            ),
                                            Container(
                                                content=Text(
                                                    "°",
                                                    size = 28,
                                                    text_align="center"
                                                )
                                            ),
                                        ],
                                    ),
                                    Text(
                                        f'{description}',
                                        size = 16,
                                        color="white25",
                                        text_align="center"
                                    ),
                                    
                                ],
                            ),
                        ],  
                    ),
                    Divider(height=8, color="white10"),
                    Row(
                        alignment="spaceAround", 
                        controls=[
                            Container(
                                content=Column(
                                    horizontal_alignment="center",
                                    spacing=2,
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            content=Image(
                                                src="blowing-winds-icon-vector.png",
                                                color="white",
                                            ),
                                            width=25,
                                            height=25,
                                        ),
                                        Text(
                                            f'{str(wind)} m/s',
                                            size = 11,
                                        ),
                                        Text(
                                            "wind",
                                            size=9,
                                            color="white54",
                                        )
                                    ]
                                )
                            ),
                            Container(
                                content=Column(
                                    horizontal_alignment="center",
                                    spacing=2,
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            content=Image(
                                                src="icons8-humidity.png",
                                                color="white",
                                            ),
                                            width=25,
                                            height=25,
                                        ),
                                        Text(
                                            f'{str(humidity)} %',
                                            size = 11,
                                        ),
                                        Text(
                                            "humidity",
                                            size=9,
                                            color="white54",
                                        )
                                    ]
                                )
                            ),
                            Container(
                                content=Column(
                                    horizontal_alignment="center",
                                    spacing=2,
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            content=Image(
                                                src="thermometer.png",
                                                color="white",
                                            ),
                                            width=25,
                                            height=25,
                                        ),
                                        Text(
                                            f'{str(feels_like)} °',
                                            size = 11,
                                        ),
                                        Text(
                                            "feels_like",
                                            size=9,
                                            color="white54",
                                        )
                                    ]
                                )
                            )
                        ]
                    ),
                    # 
                    _today_extra,
                ],
            ),
        )
        return top

    
    _c = Container(
        width=310, 
        height=660,
        border_radius=35,
        bgcolor='black',
        padding=10,
        content=Stack(
            width=210, 
            height=550, 
            controls=[

                _top(),
            ],
        ),
    )
    page.add(_c)
    


if __name__ == "__main__":
    flet.app(target=main, view=WEB_BROWSER, assets_dir='assets')


