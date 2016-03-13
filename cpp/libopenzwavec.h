#include <stdint.h>
#include <stdbool.h>

#include "openzwave/Manager.h"
#include "openzwave/Notification.h"

extern "C" {
    typedef void* CManager;
    typedef void* CNotification;
    typedef void* COptions;

    typedef void* pfnOnNotification_t;
    typedef OpenZWave::Notification::NotificationType NotificationType;

    CManager newCManager(void);
    void destroyCManager(CManager);

    bool CManagerIsBridgeController(CManager, uint32_t);
    bool CManagerIsPrimaryController(CManager, uint32_t);
    bool CManagerIsStaticUpdateController(CManager, uint32_t);
    bool CManagerCancelControllerCommand(CManager, uint32_t const);

    bool CManagerAddWatcher(CManager, pfnOnNotification_t, void* context);
    bool CManagerRemoveWatcher(CManager, pfnOnNotification_t, void* context);

    bool CManagerAddDriver(CManager, const char*);
    bool CManagerRemoveDriver(CManager, const char*);

    const char* CManagerGetLibraryTypeName(CManager, uint32_t const);
    const char* CManagerGetLibraryVersion(CManager, uint32_t const);
    int32_t CManagerGetSendQueueCount(CManager, uint32_t const);

    const char* CManagerGetNodeName(CManager, uint32_t const, uint8_t const);
    void CManagerSetNodeName(CManager, uint32_t const, uint8_t const, const char*);

    const char* CManagerGetNodeLocation(CManager, uint32_t const, uint8_t const);
    void CManagerSetNodeLocation(CManager, uint32_t const, uint8_t const, const char*);

    const char* CManagerGetNodeProductName(CManager, uint32_t const, uint8_t const);
    void CManagerSetNodeProductName(CManager, uint32_t const, uint8_t const, const char*);

    void CManagerWriteConfig(CManager, uint32_t const);

    NotificationType CNotificationGetType(CNotification);
    uint32_t CNotificationGetHomeId(CNotification);
    uint8_t CNotificationGetNodeId(CNotification);

    COptions newCOptions(const char*, const char*, const char*);
    void destroyCOptions(COptions);
    bool COptionsAddString(COptions, const char*, const char*, bool);
    bool COptionsAddBool(COptions, const char*, bool);
    bool COptionsAddInt(COptions, const char*, int32_t);
    bool COptionsLock(COptions);
    bool COptionsAreLocked(COptions);
}
