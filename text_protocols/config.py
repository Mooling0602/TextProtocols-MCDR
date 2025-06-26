from pydantic import BaseModel


class PluginConfig(BaseModel):
    chat_image: bool = True

