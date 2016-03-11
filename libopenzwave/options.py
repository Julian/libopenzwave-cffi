from _libopenzwave import lib


class PyOptions(object):
    def __init__(self, config_path, user_path=".", cmd_line=""):
        self._config_path = config_path
        self._user_path = user_path
        self._cmd_line = cmd_line
        self.create()

    def create(self):
        self.options = lib.newCOptions(
            self._config_path, self._user_path, self._cmd_line,
        )
        return True

    def addOptionBool(self, name, value):
        return lib.COptionsAddBool(self.options, name, value)

    def addOptionInt(self, name, value):
        return lib.COptionsAddInt(self.options, name, value)

    def addOptionString(self, name, value, append=False):
        return lib.COptionsAddString(self.options, name, value, append)

    def lock(self):
        return lib.COptionsLock(self.options)

    def areLocked(self):
        return lib.COptionsAreLocked(self.options)
