# -*- coding: utf-8 -*-

"""
.. module:: libopenzwave

This file is part of **python-openzwave** project https://github.com/OpenZWave/python-openzwave.

:platform: Unix, Windows, MacOS X
:sinopsis: openzwave C++

.. moduleauthor: bibi21000 aka Sebastien GALLET <bibi21000@gmail.com>
.. moduleauthor: Maarten Damen <m.damen@gmail.com>

License : GPL(v3)

**python-openzwave** is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

**python-openzwave** is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with python-openzwave. If not, see http://www.gnu.org/licenses.

"""

class PyOptions(object):
    """
    Manage options manager
    """

    def __init__(self, config_path=None, user_path=".", cmd_line=""):
        """
        Create an option object and check that parameters are valid.

        :param device: The device to use
        :type device: str
        :param config_path: The openzwave config directory. If None, try to configure automatically.
        :type config_path: str
        :param user_path: The user directory
        :type user_path: str
        :param cmd_line: The "command line" options of the openzwave library
        :type cmd_line: str

        """
        if config_path is None:
            config_path = self.getConfigPath()
        if config_path is None:
            raise LibZWaveException("Can't autoconfigure path to config")
        self._config_path = config_path
        if user_path is None:
            user_path = "."
        self._user_path = user_path
        if cmd_line is None:
            cmd_line=""
        self._cmd_line = cmd_line
        self.create(self._config_path, self._user_path, self._cmd_line)


    def create(self, a, b, c):
        """
        .. _createoptions:

        Create an option object used to start the manager

        :param a: The path of the config directory
        :type a: str
        :param b: The path of the user directory
        :type b: str
        :param c: The "command line" options of the openzwave library
        :type c: str

        :see: destroyoptions_

        """
        self.options = CreateOptions(
            str_to_cppstr(a), str_to_cppstr(b), str_to_cppstr(c))
        return True

    def destroy(self):
        """
        .. _destroyoptions:

         Deletes the Options and cleans up any associated objects.
         The application is responsible for destroying the Options object,
         but this must not be done until after the Manager object has been
         destroyed.

        :return: The result of the operation.
        :rtype: bool

        :see: createoptions_

        """
        return self.options.Destroy()

    def lock(self):
        """
        .. _lock:

        Lock the options. Needed to start the manager

        :return: The result of the operation.
        :rtype: bool

        :see: areLocked_

        """
        return self.options.Lock()

    def areLocked(self):
        '''
        .. _areLocked:

         Test whether the options have been locked.

        :return: true if the options have been locked.
        :rtype: boolean

        :see: lock_

        '''
        return self.options.AreLocked()

    def addOptionBool(self, name, value):
        """
        .. _addOptionBool:

        Add a boolean option.

        :param name: The name of the option.
        :type name: str
        :param value: The value of the option.
        :type value: boolean
        :return: The result of the operation.
        :rtype: bool

        :see: addOption_, addOptionInt_, addOptionString_

        """
        return self.options.AddOptionBool(str_to_cppstr(name), value)

    def addOptionInt(self, name, value):
        """
        .. _addOptionInt:

        Add an integer option.

        :param name: The name of the option.
        :type name: str
        :param value: The value of the option.
        :type value: boolean
        :return: The result of the operation.
        :rtype: bool

        :see: addOption_, addOptionBool_, addOptionString_

        """
        return self.options.AddOptionInt(str_to_cppstr(name), value)

    def addOptionString(self, name, value, append=False):
        """
        .. _addOptionString:

        Add a string option.

        :param name: The name of the option.  Option names are case insensitive and must be unique.
        :type name: str
        :param value: The value of the option.
        :type value: str
        :param append: Setting append to true will cause values read from the command line
         or XML file to be concatenated into a comma delimited set.  If _append is false,
         newer values will overwrite older ones.
        :type append: boolean
        :return: The result of the operation.
        :rtype: bool

        :see: addOption_, addOptionBool_, addOptionInt_

        """
        return self.options.AddOptionString(
            str_to_cppstr(name), str_to_cppstr(value), append)

    def addOption(self, name, value):
        """
        .. _addOption:

        Add an option.

        :param name: The name of the option.
        :type name: string
        :param value: The value of the option.
        :type value: boolean, integer, string
        :return: The result of the operation.
        :rtype: bool

        :see: addOptionBool_, addOptionInt_, addOptionString_

        """
        if name not in PyOptionList:
            return False
        if PyOptionList[name]['type'] == "String":
            return self.addOptionString(name, value)
        elif PyOptionList[name]['type'] == "Bool":
            return self.addOptionBool(name, value)
        elif PyOptionList[name]['type'] == "Int":
            return self.addOptionInt(name, value)
        return False

    def getOption(self, name):
        """
        .. _getOption:

        Retrieve option of a value.

        :param name: The name of the option.
        :type name: string
        :return: The value
        :rtype: boolean, integer, string or None

        :see: getOptionAsBool_, getOptionAsInt_, getOptionAsString_

        """
        if name not in PyOptionList:
            return None
        if PyOptionList[name]['type'] == "String":
            return self.getOptionAsString(name)
        elif PyOptionList[name]['type'] == "Bool":
            return self.getOptionAsBool(name)
        elif PyOptionList[name]['type'] == "Int":
            return self.getOptionAsInt(name)
        return False

    # def getOptionAsBool(self, name):
    #     """
    #     .. _getOptionAsBool:
    #
    #     Retrieve boolean value of an option.
    #
    #     :param name: The name of the option.
    #     :type name: string
    #     :return: The value or None
    #     :rtype: boolean or None
    #
    #     :see: getOption_, getOptionAsInt_, getOptionAsString_
    #
    #     """
    #     cdef bool type_bool
    #     cret = self.options.GetOptionAsBool(str_to_cppstr(name), &type_bool)
    #     ret = type_bool if cret==True else None
    #     return ret
    #
    # def getOptionAsInt(self, name):
    #     """
    #     .. _getOptionAsInt:
    #
    #     Retrieve integer value of an option.
    #
    #     :param name: The name of the option.
    #     :type name: string
    #     :return: The value or None
    #     :rtype: Integer or None
    #
    #     :see: getOption_, getOptionAsBool_, getOptionAsString_
    #
    #     """
    #     cdef int32_t type_int
    #     cret = self.options.GetOptionAsInt(str_to_cppstr(name), &type_int)
    #     ret = type_int if cret==True else None
    #     return ret
    #
    # def getOptionAsString(self, name):
    #     """
    #     .. _getOptionAsString:
    #
    #     Retrieve string value of an option.
    #
    #     :param name: The name of the option.
    #     :type name: string
    #     :return: The value or None
    #     :rtype: String or None
    #
    #     :see: getOption_, getOptionAsBool_, getOptionAsInt_
    #
    #     """
    #     cdef string type_string
    #     cret = self.options.GetOptionAsString(str_to_cppstr(name), &type_string)
    #     ret = cstr_to_str(type_string.c_str()) if cret==True else None
    #     return ret

    def getConfigPath(self):
        '''
        .. _getConfigPath:

        Retrieve the config path. This directory hold the xml files.

        :return: A string containing the library config path or None.
        :rtype: str

        '''
        return configPath()


PyStatDriver = {
    'SOFCnt' : "Number of SOF bytes received",
    'ACKWaiting' : "Number of unsolicited messages while waiting for an ACK",
    'readAborts' : "Number of times read were aborted due to timeouts",
    'badChecksum' : "Number of bad checksums",
    'readCnt' : "Number of messages successfully read",
    'writeCnt' : "Number of messages successfully sent",
    'CANCnt' : "Number of CAN bytes received",
    'NAKCnt' : "Number of NAK bytes received",
    'ACKCnt' : "Number of ACK bytes received",
    'OOFCnt' : "Number of bytes out of framing",
    'dropped' : "Number of messages dropped & not delivered",
    'retries' : "Number of messages retransmitted",
    'callbacks' : "Number of unexpected callbacks",
    'badroutes' : "Number of failed messages due to bad route response",
    'noack' : "Number of no ACK returned errors",
    'netbusy' : "Number of network busy/failure messages",
    'nondelivery' : "Number of messages not delivered to network",
    'routedbusy' : "Number of messages received with routed busy status",
    'broadcastReadCnt' : "Number of broadcasts read",
    'broadcastWriteCnt' : "Number of broadcasts sent",
    }


PyLogLevels = {
    'Invalid' : {'doc':'Invalid Log Status', 'value':0},
    'None' : {'doc':'Disable all logging', 'value':1},
    'Always' : {'doc':'These messages should always be shown', 'value':2},
    'Fatal' : {'doc':'A likely fatal issue in the library', 'value':3},
    'Error' : {'doc':'A serious issue with the library or the network', 'value':4},
    'Warning' : {'doc':'A minor issue from which the library should be able to recover', 'value':5},
    'Alert' : {'doc':'Something unexpected by the library about which the controlling application should be aware', 'value':6},
    'Info' : {'doc':"Everything's working fine...these messages provide streamlined feedback on each message", 'value':7},
    'Detail' : {'doc':'Detailed information on the progress of each message', 'value':8},
    'Debug' : {'doc':'Very detailed information on progress that will create a huge log file quickly but this level (as others) can be queued and sent to the log only on an error or warning', 'value':9},
    'StreamDetail' : {'doc':'Will include low-level byte transfers from controller to buffer to application and back', 'value':10},
    'Internal' : {'doc':'Used only within the log class (uses existing timestamp, etc', 'value':11},
    }


class EnumWithDoc(str):
    """Enum helper"""
    def setDoc(self, doc):
        self.doc = doc
        return self

PyNotifications = [
    EnumWithDoc('ValueAdded').setDoc("A new node value has been added to OpenZWave's set. These notifications occur after a node has been discovered, and details of its command classes have been received.  Each command class may generate one or more values depending on the complexity of the item being represented."),
    EnumWithDoc('ValueRemoved').setDoc("A node value has been removed from OpenZWave's set.  This only occurs when a node is removed."),
    EnumWithDoc('ValueChanged').setDoc("A node value has been updated from the Z-Wave network and it is different from the previous value."),
    EnumWithDoc('ValueRefreshed').setDoc("A node value has been updated from the Z-Wave network."),
    EnumWithDoc('Group').setDoc("The associations for the node have changed. The application should rebuild any group information it holds about the node."),
    EnumWithDoc('NodeNew').setDoc("A new node has been found (not already stored in zwcfg*.xml file)."),
    EnumWithDoc('NodeAdded').setDoc("A new node has been added to OpenZWave's set.  This may be due to a device being added to the Z-Wave network, or because the application is initializing itself."),
    EnumWithDoc('NodeRemoved').setDoc("A node has been removed from OpenZWave's set.  This may be due to a device being removed from the Z-Wave network, or because the application is closing."),
    EnumWithDoc('NodeProtocolInfo').setDoc("Basic node information has been receievd, such as whether the node is a setening device, a routing device and its baud rate and basic, generic and specific types. It is after this notification that you can call Manager::GetNodeType to obtain a label containing the device description."),
    EnumWithDoc('NodeNaming').setDoc("One of the node names has changed (name, manufacturer, product)."),
    EnumWithDoc('NodeEvent').setDoc("A node has triggered an event.  This is commonly caused when a node sends a Basic_Set command to the controller.  The event value is stored in the notification."),
    EnumWithDoc('PollingDisabled').setDoc("Polling of a node has been successfully turned off by a call to Manager::DisablePoll."),
    EnumWithDoc('PollingEnabled').setDoc("Polling of a node has been successfully turned on by a call to Manager::EnablePoll."),
    EnumWithDoc('SceneEvent').setDoc("Scene Activation Set received."),
    EnumWithDoc('CreateButton').setDoc("Handheld controller button event created."),
    EnumWithDoc('DeleteButton').setDoc("Handheld controller button event deleted."),
    EnumWithDoc('ButtonOn').setDoc("Handheld controller button on pressed event."),
    EnumWithDoc('ButtonOff').setDoc("Handheld controller button off pressed event."),
    EnumWithDoc('DriverReady').setDoc("A driver for a PC Z-Wave controller has been added and is ready to use.  The notification will contain the controller's Home ID, which is needed to call most of the Manager methods."),
    EnumWithDoc('DriverFailed').setDoc("Driver failed to load."),
    EnumWithDoc('DriverReset').setDoc("All nodes and values for this driver have been removed.  This is sent instead of potentially hundreds of individual node and value notifications."),
    EnumWithDoc('EssentialNodeQueriesComplete').setDoc("The queries on a node that are essential to its operation have been completed. The node can now handle incoming messages."),
    EnumWithDoc('NodeQueriesComplete').setDoc("All the initialisation queries on a node have been completed."),
    EnumWithDoc('AwakeNodesQueried').setDoc("All awake nodes have been queried, so client application can expected complete data for these nodes."),
    EnumWithDoc('AllNodesQueriedSomeDead').setDoc("All nodes have been queried but some dead nodes found."),
    EnumWithDoc('AllNodesQueried').setDoc("All nodes have been queried, so client application can expected complete data."),
    EnumWithDoc('Notification').setDoc("A manager notification report."),
    EnumWithDoc('DriverRemoved').setDoc("The Driver is being removed."),
    EnumWithDoc('ControllerCommand').setDoc("When Controller Commands are executed, Notifications of Success/Failure etc are communicated via this Notification."),
    ]


PyStatDriver = {
    'SOFCnt' : "Number of SOF bytes received",
    'ACKWaiting' : "Number of unsolicited messages while waiting for an ACK",
    'readAborts' : "Number of times read were aborted due to timeouts",
    'badChecksum' : "Number of bad checksums",
    'readCnt' : "Number of messages successfully read",
    'writeCnt' : "Number of messages successfully sent",
    'CANCnt' : "Number of CAN bytes received",
    'NAKCnt' : "Number of NAK bytes received",
    'ACKCnt' : "Number of ACK bytes received",
    'OOFCnt' : "Number of bytes out of framing",
    'dropped' : "Number of messages dropped & not delivered",
    'retries' : "Number of messages retransmitted",
    'callbacks' : "Number of unexpected callbacks",
    'badroutes' : "Number of failed messages due to bad route response",
    'noack' : "Number of no ACK returned errors",
    'netbusy' : "Number of network busy/failure messages",
    'nondelivery' : "Number of messages not delivered to network",
    'routedbusy' : "Number of messages received with routed busy status",
    'broadcastReadCnt' : "Number of broadcasts read",
    'broadcastWriteCnt' : "Number of broadcasts sent",
    }
