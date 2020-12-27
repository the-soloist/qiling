from qiling.os.const import *
from ..fncc import *
from ..ProcessorBind import *

# Based on AMI codebase found on https://github.com/marktsai0316/RAIDOOBMODULE
# @see: AmiModulePkg/Include/Protocol/AmiDebugService.h
class AMI_DEBUG_SERVICE_PROTOCOL(STRUCT):
	_fields_ = [
		('Debug',       FUNCPTR(VOID, UINTN, PTR(CHAR8), PTR(VOID))),
		('DebugAssert', FUNCPTR(VOID, PTR(CHAR8), UINTN, PTR(CHAR8)))
	]

@dxeapi(params = {
	"ErrorLevel"    : INT,
	"Format"        : STRING,
	"VaListMarker"  : POINTER
})
def hook_Debug(ql, address, params):
	pass

@dxeapi(params = {
	"FileName"      : STRING,
	"LineNumber"    : INT,
	"Description"   : STRING
})
def hook_DebugAssert(ql, address, params):
	pass

descriptor = {
	"guid" : "441ffa18-8714-421e-8c95-587080796fee",
	"struct" : AMI_DEBUG_SERVICE_PROTOCOL,
	"fields" : (
		("Debug",       hook_Debug),
		("DebugAssert", hook_DebugAssert)
	)
}
