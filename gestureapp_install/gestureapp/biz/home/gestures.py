class GestureDAO:
    def __init__(self):
        self.gestures_data = [
            "good",
            "bad",
            "666",
            "yeah",
            "ok",
            "gun",
            "pray",
            "c",
            "fist",
            "love"
        ]    
    
    def validate(self, gesturename, gesturenum):
        return gesturename.lower() == self.gestures_data[gesturenum]