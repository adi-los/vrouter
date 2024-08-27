from vrouter.src.application.services.vrouter_svc import VrouterService
from vrouter.src.adapters.out_process.vrouter.vrouter_adapter import VrouterConfigAdapter

# Dependency injection
vrouter_service = VrouterService(
    vrouter_config_adapter=VrouterConfigAdapter()
)

