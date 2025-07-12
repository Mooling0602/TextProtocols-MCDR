from mcdreforged.api.all import (
    CommandSource,
    CommandContext,
    SimpleCommandBuilder,
    PluginServerInterface,
    Text,
)
from text_protocols.protocols.chat_image import CICode

builder = SimpleCommandBuilder()


def command_register(server: PluginServerInterface):
    builder.arg("url", Text)
    builder.register(server)


@builder.command("!!text cicode <url>")
def on_node_text_cicode_url(src: CommandSource, ctx: CommandContext):
    url = ctx["url"]
    src.reply(str(CICode(url)))
