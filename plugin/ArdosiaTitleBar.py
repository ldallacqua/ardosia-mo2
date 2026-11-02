# Pinta a barra de título do MO2 nas cores do Ardósia, porque ela é nativa do Windows e fica fora do QSS.
# Instalação: copie este arquivo para <MO2>/plugins/ e reinicie o MO2. Só age com um tema Ardósia ativo.
# A cor exata exige Windows 11; no Windows 10 recente, a barra fica só no escuro padrão do sistema.
import ctypes
from ctypes import wintypes

from PyQt6.QtWidgets import QApplication

import mobase

DWMWA_USE_IMMERSIVE_DARK_MODE = 20
DWMWA_BORDER_COLOR = 34
DWMWA_CAPTION_COLOR = 35
DWMWA_TEXT_COLOR = 36
DWMWA_COLOR_DEFAULT = 0xFFFFFFFF


def colorref(rgb):
    """#RRGGBB -> COLORREF (0x00BBGGRR)."""
    r, g, b = (int(rgb[i:i + 2], 16) for i in (1, 3, 5))
    return r | (g << 8) | (b << 16)


ARDOSIA = {
    DWMWA_USE_IMMERSIVE_DARK_MODE: 1,
    DWMWA_CAPTION_COLOR: colorref("#12161B"),  # bg-0
    DWMWA_TEXT_COLOR: colorref("#97A2B0"),  # text-secondary
    DWMWA_BORDER_COLOR: colorref("#323A45"),  # border
}
DEFAULT = {
    DWMWA_USE_IMMERSIVE_DARK_MODE: 0,
    DWMWA_CAPTION_COLOR: DWMWA_COLOR_DEFAULT,
    DWMWA_TEXT_COLOR: DWMWA_COLOR_DEFAULT,
    DWMWA_BORDER_COLOR: DWMWA_COLOR_DEFAULT,
}


def paint(hwnd, attributes):
    for attribute, value in attributes.items():
        data = wintypes.DWORD(value)
        ctypes.windll.dwmapi.DwmSetWindowAttribute(
            wintypes.HWND(hwnd), attribute, ctypes.byref(data), ctypes.sizeof(data)
        )


class ArdosiaTitleBar(mobase.IPlugin):
    def __init__(self):
        super().__init__()
        self._painted = set()

    def init(self, organizer):
        # focusWindowChanged cobre as janelas novas e, ao voltar de Settings, a troca de tema
        QApplication.instance().focusWindowChanged.connect(self._onFocusWindowChanged)
        organizer.onUserInterfaceInitialized(lambda window: self._update(int(window.winId())))
        return True

    def name(self):
        return "Ardosia Title Bar"

    def author(self):
        return "Ardosia"

    def description(self):
        return "Pinta a barra de título nas cores do tema Ardósia."

    def version(self):
        return mobase.VersionInfo(1, 0, 0, mobase.ReleaseType.FINAL)

    def settings(self):
        return []

    def _onFocusWindowChanged(self, window):
        if window is not None:
            self._update(int(window.winId()))

    def _update(self, hwnd):
        if "Ardosia" in QApplication.instance().styleSheet():
            paint(hwnd, ARDOSIA)
            self._painted.add(hwnd)
        elif hwnd in self._painted:
            paint(hwnd, DEFAULT)
            self._painted.discard(hwnd)


def createPlugin():
    return ArdosiaTitleBar()
