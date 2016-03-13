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

    void destroyCManager(CManager cManager) {
        static_cast<OpenZWave::Manager*>(cManager)->Destroy();
    }

    bool CManagerAddWatcher(CManager cManager, pfnOnNotification_t notification, void* context) {
        return static_cast<OpenZWave::Manager*>(cManager)->AddWatcher(
                reinterpret_cast<OpenZWave::Manager::pfnOnNotification_t>(notification), context);
    }

    bool CManagerAddDriver(CManager cManager, const char* cControllerPath) {
        std::string controllerPath = cControllerPath;
        return static_cast<OpenZWave::Manager*>(cManager)->AddDriver(controllerPath);
    }

    bool CManagerCancelControllerCommand(CManager cManager, uint32_t const homeId) {
        return static_cast<OpenZWave::Manager*>(cManager)->CancelControllerCommand(homeId);
    }

    const char* CManagerGetLibraryTypeName(CManager cManager, uint32_t const homeId) {
        return static_cast<OpenZWave::Manager*>(cManager)->GetLibraryTypeName(homeId).c_str();
    }

    const char* CManagerGetLibraryVersion(CManager cManager, uint32_t const homeId) {
        return static_cast<OpenZWave::Manager*>(cManager)->GetLibraryVersion(homeId).c_str();
    }

    void CManagerSetNodeName(CManager cManager, uint32_t const homeId, uint8_t const nodeId, const char* cNodeName) {
        std::string nodeName = cNodeName;
        static_cast<OpenZWave::Manager*>(cManager)->SetNodeName(homeId, nodeId, nodeName);
    }

    void CManagerSetNodeLocation(CManager cManager, uint32_t homeId, uint8_t const nodeId, const char* cNodeLocation) {
        std::string nodeLocation = cNodeLocation;
        static_cast<OpenZWave::Manager*>(cManager)->SetNodeLocation(homeId, nodeId, nodeLocation);
    }

    NotificationType CNotificationGetType(CNotification cNotification) {
        return static_cast<OpenZWave::Notification*>(cNotification)->GetType();
    }

    uint32 CNotificationGetHomeId(CNotification cNotification) {
        return static_cast<OpenZWave::Notification*>(cNotification)->GetHomeId();
    }

    uint8 CNotificationGetNodeId(CNotification cNotification) {
        return static_cast<OpenZWave::Notification*>(cNotification)->GetNodeId();
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

    void destroyCOptions(COptions cOptions) {
        static_cast<OpenZWave::Options*>(cOptions)->Destroy();
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
