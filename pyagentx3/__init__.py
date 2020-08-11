# -*- coding: utf-8 -*-

import logging

from pyagentx3.updater import Updater
from pyagentx3.agent import Agent
from pyagentx3.sethandler import SetHandler, SetHandlerError

def setup_logging(debug=False):
    if debug:
        level = logging.DEBUG
    else:
        level = logging.INFO
    logger = logging.getLogger('pyagentx3')
    logger.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

SOCKET_PATH = "/var/agentx/master"

AGENTX_EMPTY_PDU = 1
AGENTX_OPEN_PDU = 1
AGENTX_CLOSE_PDU = 2
AGENTX_REGISTER_PDU = 3
AGENTX_UNREGISTER_PDU = 4
AGENTX_GET_PDU = 5
AGENTX_GETNEXT_PDU = 6
AGENTX_GETBULK_PDU = 7
AGENTX_TESTSET_PDU = 8
AGENTX_COMMITSET_PDU = 9
AGENTX_UNDOSET_PDU = 10
AGENTX_CLEANUPSET_PDU = 11
AGENTX_NOTIFY_PDU = 12
AGENTX_PING_PDU = 13
AGENTX_INDEXALLOCATE_PDU = 14
AGENTX_INDEXDEALLOCATE_PDU = 15
AGENTX_ADDAGENTCAPS_PDU = 16
AGENTX_REMOVEAGENTCAPS_PDU = 17
AGENTX_RESPONSE_PDU = 18

PDU_TYPE_NAME = {}
PDU_TYPE_NAME[0] = "EMPTY_PDU"
PDU_TYPE_NAME[1] = "OPEN_PDU"
PDU_TYPE_NAME[2] = "CLOSE_PDU"
PDU_TYPE_NAME[3] = "REGISTER_PDU"
PDU_TYPE_NAME[4] = "UNREGISTER_PDU"
PDU_TYPE_NAME[5] = "GET_PDU"
PDU_TYPE_NAME[6] = "GETNEXT_PDU"
PDU_TYPE_NAME[7] = "GETBULK_PDU"
PDU_TYPE_NAME[8] = "TESTSET_PDU"
PDU_TYPE_NAME[9] = "COMMITSET_PDU"
PDU_TYPE_NAME[10] = "UNDOSET_PDU"
PDU_TYPE_NAME[11] = "CLEANUPSET_PDU"
PDU_TYPE_NAME[12] = "NOTIFY_PDU"
PDU_TYPE_NAME[13] = "PING_PDU"
PDU_TYPE_NAME[14] = "INDEXALLOCATE_PDU"
PDU_TYPE_NAME[15] = "INDEXDEALLOCATE_PDU"
PDU_TYPE_NAME[16] = "ADDAGENTCAPS_PDU"
PDU_TYPE_NAME[17] = "REMOVEAGENTCAPS_PDU"
PDU_TYPE_NAME[18] = "RESPONSE_PDU"

TYPE_INTEGER = 2
TYPE_OCTETSTRING = 4
TYPE_NULL = 5
TYPE_OBJECTIDENTIFIER = 6
TYPE_IPADDRESS = 64
TYPE_COUNTER32 = 65
TYPE_GAUGE32 = 66
TYPE_TIMETICKS = 67
TYPE_OPAQUE = 68
TYPE_COUNTER64 = 70
TYPE_NOSUCHOBJECT = 128
TYPE_NOSUCHINSTANCE = 129
TYPE_ENDOFMIBVIEW = 130

TYPE_NAME = {}
TYPE_NAME[2] = "INTEGER"
TYPE_NAME[4] = "OCTETSTRING"
TYPE_NAME[5] = "NULL"
TYPE_NAME[6] = "OBJECTIDENTIFIER"
TYPE_NAME[64] = "IPADDRESS"
TYPE_NAME[65] = "COUNTER32"
TYPE_NAME[66] = "GAUGE32"
TYPE_NAME[67] = "TIMETICKS"
TYPE_NAME[68] = "OPAQUE"
TYPE_NAME[70] = "COUNTER64"
TYPE_NAME[128] = "NOSUCHOBJECT"
TYPE_NAME[129] = "NOSUCHINSTANCE"
TYPE_NAME[130] = "ENDOFMIBVIEW"

ERROR_NOAGENTXERROR = 0
ERROR_GENERR = 5
ERROR_NOACCESS = 6
ERROR_WRONGTYPE = 7
ERROR_WRONGLENGTH = 8
ERROR_WRONGENCODING = 9
ERROR_WRONGVALUE = 10
ERROR_NOCREATION = 11
ERROR_INCONSISTENTVALUE = 12
ERROR_RESOURCEUNAVAILABLE = 13
ERROR_COMMITFAILED = 14
ERROR_UNDOFAILED = 15
ERROR_NOTWRITABLE = 17
ERROR_INCONSISTENTNAME = 18
ERROR_OPENFAILED = 256
ERROR_NOTOPEN = 257
ERROR_INDEXWRONGTYPE = 258
ERROR_INDEXALREADYALLOCATED = 259
ERROR_INDEXNONEAVAILABLE = 260
ERROR_INDEXNOTALLOCATED = 261
ERROR_UNSUPPORTEDCONTEXT = 262
ERROR_DUPLICATEREGISTRATION = 263
ERROR_UNKNOWNREGISTRATION = 264
ERROR_UNKNOWNAGENTCAPS = 265
ERROR_PARSEERROR = 266
ERROR_REQUESTDENIED = 267
ERROR_PROCESSINGERROR = 268

ERROR_NAMES = {}
ERROR_NAMES[0] = "NOAGENTXERROR"
ERROR_NAMES[5] = "GENERR"
ERROR_NAMES[6] = "NOACCESS"
ERROR_NAMES[7] = "WRONGTYPE"
ERROR_NAMES[8] = "WRONGLENGTH"
ERROR_NAMES[9] = "WRONGENCODING"
ERROR_NAMES[10] = "WRONGVALUE"
ERROR_NAMES[11] = "NOCREATION"
ERROR_NAMES[12] = "INCONSISTENTVALUE"
ERROR_NAMES[13] = "RESOURCEUNAVAILABLE"
ERROR_NAMES[14] = "ERROR_COMMITFAILED"
ERROR_NAMES[15] = "ERROR_UNDOFAILED"
ERROR_NAMES[17] = "NOTWRITABLE"
ERROR_NAMES[18] = "INCONSISTENTNAME"
ERROR_NAMES[256] = "OPENFAILED"
ERROR_NAMES[257] = "NOTOPEN"
ERROR_NAMES[258] = "INDEXWRONGTYPE"
ERROR_NAMES[259] = "INDEXALREADYALLOCATED"
ERROR_NAMES[260] = "INDEXNONEAVAILABLE"
ERROR_NAMES[261] = "INDEXNOTALLOCATED"
ERROR_NAMES[262] = "UNSUPPORTEDCONTEXT"
ERROR_NAMES[263] = "DUPLICATEREGISTRATION"
ERROR_NAMES[264] = "UNKNOWNREGISTRATION"
ERROR_NAMES[265] = "UNKNOWNAGENTCAPS"
ERROR_NAMES[266] = "PARSEERROR"
ERROR_NAMES[267] = "REQUESTDENIED"
ERROR_NAMES[268] = "PROCESSINGERROR"

