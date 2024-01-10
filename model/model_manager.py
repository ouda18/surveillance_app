# model/model_manager.py

class SurveillanceModel:
    def __init__(self):
        self.cameras = []

    def add_camera(self, camera):
        self.cameras.append(camera)

    def remove_camera(self, camera):
        self.cameras.remove(camera)

    def get_cameras(self):
        return self.cameras
