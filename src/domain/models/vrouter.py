from pydantic import BaseModel

class config_Router(BaseModel):

    router_ip: str   # O SERVER router ID
    vrf: str         # le nom de la vrf
    table: str       # table de la vrf (un chiffre)
    eth_vrf: str     # interface vrf ( dans le cas dylk eth0)
    add_vrf: str     # add ip de l'interface eth0
    eth_interco: str # l'interface de l'interco (dans ton cas eth1)
    add_interco: str # l'address de l'interfece
    ne: str          # neighbor bgp core
    update: str      # router id
    ne_intrco: str   # neighbor EDGE 
    rule: str		 # la regle nat ( un chifre)
    net: str         # network à nater
    vip: str	     # l'address de vip pour la vrrp
    priority: str	 # priority de group vrrp (pour primary 200 et pour l'autre 150)
    vrid: str		 # un chiffre pour vrrp 
    local_as: str	 # local système autonome
    remote_as: str   # remote système autonome