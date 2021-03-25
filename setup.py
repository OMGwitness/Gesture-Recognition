from distutils.core import setup

setup(
    name="gesture_recognition",
    version="1.0",
    description="手势识别",
    author="张广杰，刘涛榕，刘子睿，仇钧超",
    packages=[
        "gestureapp",
        "gestureapp.biz",
        "gestureapp.biz.home",
        "gestureapp.biz.home.img",
        "gestureapp.biz.login",
        "gestureapp.devs",
        "gestureapp.devs.home",
        "gestureapp.devs.login",
        "gestureapp.guis",
        "gestureapp.guis.eval",
        "gestureapp.guis.home",
        "gestureapp.guis.login",
        "gestureapp.guis.tip"
    ],
    package_data={
        "gestureapp.biz.home.img":[
            "1.png",
            "2.png",
            "3.png",
            "4.png",
            "5.png",
            "6.png",
            "7.png",
            "666.png",
            "bad.png",
            "c.png",
            "fist.png",
            "good.png",
            "great.png",
            "gun.png",
            "love.png",
            "ok.png",
            "perfect.png",
            "pray.png",
            "sorry.png",
            "yeah.png"
        ],
        "gestureapp.guis":[
            "田氏颜体大字库.ttf"
        ],
        "gestureapp.guis.eval":[
            "background.png"
        ],
        "gestureapp.guis.home":[
            "background.png"
        ],
        "gestureapp.guis.login":[
            "background.png"
        ],
        "gestureapp.guis.tip":[
            "background.png"
        ]
    }
)