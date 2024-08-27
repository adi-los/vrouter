import requests
from fastapi import HTTPException
from vrouter.src.application.ports.vrouter_port  import VrouterConfigPort
from vrouter.src.domain.models.vrouter import config_Router


class VrouterConfigAdapter(VrouterConfigPort):
    def __init__(self):
        
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

    def config_vrouter(self, request: config_Router) -> str:
        url = f'https://{request.router_ip}/configure'

        # Préparez toutes les opérations dans une liste
        data = [
            {"op": "set", "path": ["vrf", "name", request.vrf, "table", request.table]},
            {"op": "set", "path": ["interfaces", "ethernet", request.eth_vrf, "vrf", request.vrf]},
            {"op": "set", "path": ["interfaces", "ethernet", request.eth_vrf, "address", request.add_vrf]},
            {"op": "set", "path": ["interfaces", "ethernet", request.eth_interco, "vrf", request.vrf]},
            {"op": "set", "path": ["interfaces", "ethernet", request.eth_interco, "address", request.add_interco]},
            {"op": "set", "path": ["protocols", "bgp", "system-as", request.local_as]},
            {"op": "set", "path": ["vrf", "name", request.vrf, "protocols", "bgp", "system-as", request.local_as]},
            {"op": "set", "path": ["vrf", "name", request.vrf, "protocols", "bgp", "neighbor", request.ne, "remote-as", request.local_as]},
            {"op": "set", "path": ["vrf", "name", request.vrf, "protocols", "bgp", "neighbor", request.ne, "description", "IBGP"]},
            {"op": "set", "path": ["vrf", "name", request.vrf, "protocols", "bgp", "neighbor", request.ne, "update-source", request.update]},
            {"op": "set", "path": ["vrf", "name", request.vrf, "protocols", "bgp", "neighbor", request.ne, "address-family", "ipv4-unicast"]},
            {"op": "set", "path": ["vrf", "name", request.vrf, "protocols", "bgp", "neighbor", request.ne_intrco, "remote-as", request.remote_as]},
            {"op": "set", "path": ["vrf", "name", request.vrf, "protocols", "bgp", "neighbor", request.ne_intrco, "description", "EBGP"]},
            {"op": "set", "path": ["vrf", "name", request.vrf, "protocols", "bgp", "neighbor", request.ne_intrco, "update-source", request.update]},
            {"op": "set", "path": ["vrf", "name", request.vrf, "protocols", "bgp", "neighbor", request.ne_intrco, "password", "vyos12345vyos"]},
            {"op": "set", "path": ["vrf", "name", request.vrf, "protocols", "bgp", "neighbor", request.ne_intrco, "address-family", "ipv4-unicast"]},
            {"op": "set", "path": ["nat", "source", "rule", request.rule, "translation", "address", "masquerade"]},
            {"op": "set", "path": ["nat", "source", "rule", request.rule, "outbound-interface", "name", request.eth_interco]},
            {"op": "set", "path": ["nat", "source", "rule", request.rule, "source", "address", request.net]},
            {"op": "set", "path": ["high-availability", "vrrp", "group", request.vrf, "vrid", request.vrid]},
            {"op": "set", "path": ["high-availability", "vrrp", "group", request.vrf, "address", request.vip]},
            {"op": "set", "path": ["high-availability", "vrrp", "group", request.vrf, "interface", request.eth_vrf]},
            {"op": "set", "path": ["high-availability", "vrrp", "group", request.vrf, "priority", request.priority]}
        ]

        # Convertir les données en une chaîne JSON
        data_str = 'data=' + str(data).replace("'", '"')

        # Clé d'authentification
        key = 'MY-HTTPS-API-PLAINTEXT-KEY'
        key_str = 'key=' + key

        # Concaténer les données et la clé
        payload = data_str + '&' + key_str

        # Soumettez la requête POST avec les données et l'en-tête appropriés
        try:

            response = requests.post(url, headers=self.headers, data=payload, verify=False)
            return {"message": f"configuration with {response.text} created successfully!"}

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))