# Copyright(C) 2023 InfiniFlow, Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from enum import IntEnum


class ErrorCode(IntEnum):
    OK = 0,

    INVALID_TIME_INFO = 1001,
    EMPTY_CONFIG_PARAMETER = 1002,
    MISMATCH_VERSION = 1003,
    INVALID_TIMEZONE = 1004,
    INVALID_BYTE_SIZE = 1005,
    INVALID_IP_ADDR = 1006,
    INVALID_LOG_LEVEL = 1007,

    WRONG_PASSWD = 2001,
    INSUFFICIENT_PRIVILEGE = 2002,

    INVALID_USERNAME = 3001,
    INVALID_PASSWD = 3002,
    INVALID_DB_NAME = 3003,
    INVALID_TABLE_NAME = 3004,
    INVALID_COLUMN_NAME = 3005,
    INVALID_INDEX_NAME = 3006,
    INVALID_COLUMN_DEFINITION = 3007,
    INVALID_TABLE_DEFINITION = 3008,
    INVALID_INDEX_DEFINITION = 3009,
    DATA_TYPE_MISMATCH = 3010,
    NAME_TOO_LONG = 3011,
    RESERVED_NAME = 3012,
    SYNTAX_ERROR = 3013,
    INVALID_PARAMETER_VALUE = 3014,
    DUPLICATE_USER = 3015,
    DUPLICATE_DATABASE_NAME = 3016,
    DUPLICATE_TABLE_NAME = 3017,
    DUPLICATE_INDEX_NAME = 3018,
    DUPLICATE_INDEX_ON_COLUMN = 3019,
    NO_SUCH_USER = 3020,
    DB_NOT_EXIST = 3021,
    TABLE_NOT_EXIST = 3022,
    INDEX_NOT_EXIST = 3023,
    COLUMN_NOT_EXIST = 3024,
    AGG_NOT_ALLOW_IN_WHERE_CLAUSE = 3025,
    COLUMN_IN_SELECT_NOT_IN_GROUP_BY = 3026,
    NO_SUCH_SYSTEM_VAR = 3027,
    INVALID_SYSTEM_VAR_VALUE = 3028,
    SYSTEM_VAR_READ_ONLY = 3029,
    FUNCTION_NOT_FOUND = 3030,
    SPECIAL_FUNCTION_NOT_FOUND = 3031,
    NOT_SUPPORTED = 3032,
    DROPPING_USING_DB = 3033,
    SESSION_NOT_FOUND = 3034,
    RECURSIVE_AGG = 3035,
    FUNCTION_ARGS_ERROR = 3036,
    IMPORT_FILE_FORMAT_ERROR = 3037,
    DATA_NOT_EXIST = 3038,
    COLUMN_COUNT_MISMATCH = 3039,
    EMPTY_DB_NAME = 3040,
    EMPTY_TABLE_NAME = 3041,
    EMPTY_COLUMN_NAME = 3042,
    EMPTY_INDEX_NAME = 3043,
    EXCEED_DB_NAME_LENGTH = 3044,
    EXCEED_TABLE_NAME_LENGTH = 3045,
    EXCEED_COLUMN_NAME_LENGTH = 3046,
    EXCEED_INDEX_NAME_LENGTH = 3047,
    NO_COLUMN_DEFINED = 3048,
    NOT_SUPPORTED_TYPE_CONVERSION = 3049,
    EMPTY_SELECT_FIELDS = 3050,
    INVALID_DATA_TYPE = 3051,

    TXN_ROLLBACK = 4001,
    TXN_CONFLICT = 4002,

    DISK_FULL = 5001,
    OUT_OF_MEMORY = 5002,
    TOO_MANY_CONNECTIONS = 5003,
    CONFIGURATION_LIMIT_EXCEED = 5004,
    QUERY_IS_TOO_COMPLEX = 5005,

    QUERY_CANCELLED = 6001,
    QUERY_NOT_SUPPORTED = 6002,
    CLIENT_CLOSE = 6003,

    DISK_IO_ERROR = 7001,
    DUPLICATED_FILE = 7002,


    CONFIG_FILE_ERROR = 7003,
    LOCK_FILE_EXISTS = 7004,
    CATALOG_CORRUPTED = 7005,
    DATA_CORRUPTED = 7006,
    INDEX_CORRUPTED = 7007,
    FILE_NOT_FOUND = 7008,
    DIR_NOT_FOUND = 7009,
    DATA_IO_ERROR = 7010,
    UNEXPECTED_ERROR = 7011,

    INVALID_ENTRY = 8001,
    NOT_FOUND_ENTRY = 8002,
    EMPTY_ENTRY_LIST = 8003,
