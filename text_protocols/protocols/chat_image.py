from typing import Optional, Callable
from logging import Logger


class CICode:
    def __init__(
        self,
        url: str,
        nsfw: Optional[bool] = None,
        name: Optional[str] = None,
        pre: Optional[str] = None,
        suf: Optional[str] = None,
        logger: Optional[Logger | Callable] = None,
    ) -> None:
        _type_check: bool = True
        _warning: str = "Adfixes are imcomplete!"
        self.url: str = url
        self.nsfw: bool = nsfw if nsfw else False
        self.name: str = name if name else "Image"
        self.pre: str = ""
        self.suf: str = ""
        self.logger = logger
        self._warning: Optional[str] = None
        match pre, suf:
            case pre, suf if pre == "," or suf == ",":
                _type_check = False
            case pre, suf if (pre is None) != (suf is None):
                self._warning = _warning
            case pre, suf if pre is None and suf is None:
                self.pre = "["
                self.suf = "]"
        if self._warning:
            if logger:
                if getattr(logger, "warning") or isinstance(logger, Logger):
                    logger.warning(self._warning)  # type: ignore
                else:
                    logger(self._warning)  # type: ignore
        if not _type_check:
            raise TypeError('Argument "pre" and "suf" can\'t be ","!')

    def __str__(self) -> str:
        return "[[{},{},{},{},{},{}]]".format(
            self.__class__.__name__,
            f"url={self.url}",
            f"nsfw={str(self.nsfw).lower()}",
            f"name={self.name}",
            f"pre={self.pre}",
            f"suf={self.suf}",
        )


if __name__ == "__main__":
    image: CICode = CICode("https://example.com/image.png")
    print("Correct example: " + str(image))
    # print("Error example: ")
    # print(CICode("https://example.com/image.png", pre=",", suf=","))
