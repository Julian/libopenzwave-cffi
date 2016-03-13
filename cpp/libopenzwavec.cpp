#include <stdbool.h>
#include <stdint.h>

#include "libopenzwavec.h"

#include "openzwave/Manager.h"
#include "openzwave/Notification.h"
#include "openzwave/Options.h"


int main() {}


extern "C"
{
    CManager newCManager(void) {
        return reinterpret_cast<void*>(OpenZWave::Manager::Create());
    }

    bool CManagerAddWatcher(CManager cManager, void* notification, void* context) {
        return static_cast<OpenZWave::Manager*>(cManager)->AddWatcher(
                reinterpret_cast<OpenZWave::Manager::pfnOnNotification_t>(notification), context);
    }

    bool CManagerAddDriver(CManager cManager, const char* cControllerPath) {
        std::string controllerPath = cControllerPath;
        return static_cast<OpenZWave::Manager*>(cManager)->AddDriver(controllerPath);
    }

    COptions newCOptions(
            const char *cConfigPath,
            const char *cUserPath,
            const char *cCommandLine)
    {
        std::string configPath = cConfigPath;
        std::string userPath = cUserPath;
        std::string commandLine = cCommandLine;
        return reinterpret_cast<void*>(
                OpenZWave::Options::Create(configPath, userPath, commandLine));
    }

    bool COptionsAddBool(COptions cOptions, const char *cName, bool value)
    {
        std::string name = cName;
        return static_cast<OpenZWave::Options*>(cOptions)->AddOptionBool(name, value);
    }

    bool COptionsAddInt(COptions cOptions, const char *cName, int32_t value)
    {
        std::string name = cName;
        return static_cast<OpenZWave::Options*>(cOptions)->AddOptionInt(name, value);
    }

    bool COptionsAddString(
            COptions cOptions,
            const char *cName,
            const char *cValue,
            bool append
            )
    {
        std::string name = cName;
        std::string value = cValue;
        return static_cast<OpenZWave::Options*>(cOptions)->AddOptionString(name, value, append);
    }

    bool COptionsLock(COptions cOptions) {
        return static_cast<OpenZWave::Options*>(cOptions)->Lock();
    }

    bool COptionsAreLocked(COptions cOptions) {
        return static_cast<OpenZWave::Options*>(cOptions)->AreLocked();
    }
}
