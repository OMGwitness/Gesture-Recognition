from distutils.core import setup

setup(
    name="yologesture",
    version="1.0",
    description="手势识别模块",
    author="张广杰，刘涛榕，刘子睿，仇钧超",
    packages=[
        "yolov4_gesture",
        "yolov4_gesture.data",
        "yolov4_gesture.utils"
    ],
    package_data={
        "yolov4_gesture.data":[
            "gestures.names",
            "gestures.pt",
            "yolov4-tiny.cfg"
        ]
    }
)