import text_protocols.runtime as rt
from typing import Optional
from mcdreforged.api.all import PluginServerInterface, RTextList
from text_protocols.config import PluginConfig
from text_protocols.mcdr.commands import command_register


def on_load(server: PluginServerInterface, _prev_module):
    rt.config = server.load_config_simple(target_class=PluginConfig)
    command_register(server)
    if server.is_server_startup():
        on_server_startup(server)


def on_server_startup(server: PluginServerInterface):
    message = show_support_status(pfx="----- TextProtocols Working Status -----")
    if message:
        server.broadcast(message)


def show_support_status(
    pfx: Optional[str] = None, efx: Optional[str] = None
) -> Optional[RTextList]:
    if rt.config is None:
        return
    result = []
    if pfx:
        result.append(pfx + "\n")
    if rt.config.chat_image:
        result.append("ChatImage: CICode protocol enabled." + "\n")
    if efx:
        result.append(efx + "\n")
    return RTextList(*result)
