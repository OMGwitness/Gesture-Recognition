from distutils.core import setup

setup(
    name="yoloface",
    version="1.0",
    description="人脸识别模块",
    author="张广杰，刘涛榕，刘子睿，仇钧超",
    packages=[
        "yolov4_face",
        "yolov4_face.data",
        "yolov4_face.utils"
    ],
    package_data={
        "yolov4_face.data":[
            "faces.names",
            "faces.pt",
            "yolov4-tiny.cfg"
        ]
    }
)