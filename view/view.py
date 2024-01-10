# view/view.py

class SurveillanceView:
    def show_cameras(self, cameras):
        for camera in cameras:
            print(f"{camera.brand} {camera.model} - {camera.ip_address}")

    def show_surveillance_started(self):
        print("Surveillance started.")
