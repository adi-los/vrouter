# src/application/services/cluster_service.py
from vrouter.src.application.ports.vrouter_port import VrouterConfigPort
from vrouter.src.domain.models.vrouter import config_Router

class VrouterService:
    def __init__(self, vrouter_config_port: VrouterConfigPort):
        self.vrouter_config_port = vrouter_config_port

    def config_vrouter(self, request: config_Router) -> str:
        return self.vrouter_config_port.config_vrouter(request)

    def __call__(self):
        return self
