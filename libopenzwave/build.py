from cffi import FFI


ffi = FFI()
ffi.set_source(
    "_libopenzwave",
    '#include "libopenzwavec.h"',
    libraries=["openzwavec"],
    source_extension=".cpp",
)
ffi.cdef(
    """
    typedef void* CManager;
    typedef void* CNotification;
    typedef void* COptions;

    typedef void* pfnOnNotification_t;
    typedef int... NotificationType;
    typedef struct {
        uint32_t m_SOFCnt;               // Number of SOF bytes received
        uint32_t m_ACKWaiting;           // Number of unsolicited messages while waiting for an ACK
        uint32_t m_readAborts;           // Number of times read were aborted due to timeouts
        uint32_t m_badChecksum;          // Number of bad checksums
        uint32_t m_readCnt;              // Number of messages successfully read
        uint32_t m_writeCnt;             // Number of messages successfully sent
        uint32_t m_CANCnt;               // Number of CAN bytes received
        uint32_t m_NAKCnt;               // Number of NAK bytes received
        uint32_t m_ACKCnt;               // Number of ACK bytes received
        uint32_t m_OOFCnt;               // Number of bytes out of framing
        uint32_t m_dropped;              // Number of messages dropped & not delivered
        uint32_t m_retries;              // Number of messages retransmitted
        uint32_t m_callbacks;            // Number of unexpected callbacks
        uint32_t m_badroutes;            // Number of failed messages due to bad route response
        uint32_t m_noack;                // Number of no ACK returned errors
        uint32_t m_netbusy;              // Number of network busy/failure messages
        uint32_t m_nondelivery;          // Number of messages not delivered to network
        uint32_t m_routedbusy;           // Number of messages received with routed busy status
        uint32_t m_broadcastReadCnt;     // Number of broadcasts read
        uint32_t m_broadcastWriteCnt;    // Number of broadcasts sent
    } DriverData;

    CManager newCManager(void);
    void destroyCManager(CManager);

    const char* CManagerGetVersionAsString(void);
    const char* CManagerGetLibraryTypeName(CManager, uint32_t const);
    const char* CManagerGetLibraryVersion(CManager, uint32_t const);
    uint8_t CManagerGetNodeVersion(CManager, uint32_t const, uint8_t);

    bool CManagerIsBridgeController(CManager, uint32_t);
    bool CManagerIsNodeBeamingDevice(CManager, uint32_t const, uint8_t);
    bool CManagerIsNodeFrequentListeningDevice(CManager, uint32_t const, uint8_t);
    bool CManagerIsNodeListeningDevice(CManager, uint32_t const, uint8_t);
    bool CManagerIsNodeRoutingDevice(CManager, uint32_t const, uint8_t);
    bool CManagerIsNodeSecurityDevice(CManager, uint32_t const, uint8_t);
    bool CManagerIsPrimaryController(CManager, uint32_t);
    bool CManagerIsStaticUpdateController(CManager, uint32_t);
    bool CManagerCancelControllerCommand(CManager, uint32_t const);

    bool CManagerAddWatcher(CManager, pfnOnNotification_t, void* context);
    bool CManagerRemoveWatcher(CManager, pfnOnNotification_t, void* context);

    bool CManagerAddDriver(CManager, const char*);
    bool CManagerRemoveDriver(CManager, const char*);

    const char* CManagerGetNodeName(CManager, uint32_t const, uint8_t const);
    void CManagerSetNodeName(CManager, uint32_t const, uint8_t const, const char*);

    const char* CManagerGetNodeLocation(CManager, uint32_t const, uint8_t const);
    void CManagerSetNodeLocation(CManager, uint32_t const, uint8_t const, const char*);

    const char* CManagerGetNodeManufacturerId(CManager, uint32_t const, uint8_t const);

    const char* CManagerGetNodeManufacturerName(CManager, uint32_t const, uint8_t const);
    void CManagerSetNodeManufacturerName(CManager, uint32_t const, uint8_t const, const char*);

    uint32_t CManagerGetNodeNeighbors(CManager, uint32_t const, uint8_t const, uint8_t**);
    const char* CManagerGetNodeProductId(CManager, uint32_t const, uint8_t const);
    const char* CManagerGetNodeProductType(CManager, uint32_t const, uint8_t const);
    bool CManagerGetNodeClassInformation(CManager, uint32_t const, uint8_t const, uint8_t const, const char **, uint8_t *);

    const char* CManagerGetNodeProductName(CManager, uint32_t const, uint8_t const);
    void CManagerSetNodeProductName(CManager, uint32_t const, uint8_t const, const char*);

    void CManagerGetDriverStatistics(CManager, uint32_t const, DriverData*);
    uint8_t CManagerGetNumGroups(CManager, uint32_t const, uint8_t const);
    int32_t CManagerGetSendQueueCount(CManager, uint32_t const);

    void CManagerWriteConfig(CManager, uint32_t const);

    extern "Python" void do_manager_watcher_callback(CManager, void* pythonFn);

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
    """
)

ffi.compile()
