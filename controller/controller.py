# controller/controller.py
from model.camera import Camera
from view.view import SurveillanceView

class SurveillanceController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_camera(self, camera):
        self.model.add_camera(camera)

    def remove_camera(self, camera):
        self.model.remove_camera(camera)

    def view_cameras(self):
        cameras = self.model.get_cameras()
        self.view.show_cameras(cameras)

    def start_surveillance(self):
        cameras = self.model.get_cameras()
        for camera in cameras:
            camera.connect()
            # Ajouter une logique pour afficher le flux vidéo en direct, enregistrement, etc.
            # en fonction des besoins spécifiques
        self.view.show_surveillance_started()
