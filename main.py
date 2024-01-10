# main.py
from model.model_manager import SurveillanceModel
from view.view import SurveillanceView
from controller.controller import SurveillanceController
from model.camera import Camera

def main():
    model = SurveillanceModel()
    view = SurveillanceView()
    controller = SurveillanceController(model, view)

    camera1 = Camera("Reolink", "Model1", "192.168.1.101", "user1", "pass1")
    camera2 = Camera("Ajhua", "Model2", "192.168.1.102", "user2", "pass2")

    controller.add_camera(camera1)
    controller.add_camera(camera2)

    controller.view_cameras()
    controller.start_surveillance()

if __name__ == "__main__":
    main()
