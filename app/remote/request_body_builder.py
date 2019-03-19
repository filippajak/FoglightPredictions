import json


class RequestbodyBuilder:


    def build_request_body_for_devices(self, countries, handsets):
        request_body = {'countries': countries, 'handsets': handsets}
        return json.dumps(request_body)

    def build_request_body_for_desktop_operating_systems(self, countries, desktop_operating_systems):
        request_body = {'countries': countries, 'operatingSystems': desktop_operating_systems}
        return json.dumps(request_body)
