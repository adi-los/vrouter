from abc import ABC, abstractmethod
from vrouter.src.domain.models.vrouter import config_Router

class VrouterConfigPort(ABC):
    @abstractmethod
    def config_vrouter(self, request: config_Router) -> str:
        pass
