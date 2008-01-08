# This file was created automatically by SWIG 1.3.29.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import libnxpython
import new
new_instancemethod = new.instancemethod
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


NXACC_READ = libnxpython.NXACC_READ
NXACC_RDWR = libnxpython.NXACC_RDWR
NXACC_CREATE = libnxpython.NXACC_CREATE
NXACC_CREATE4 = libnxpython.NXACC_CREATE4
NXACC_CREATE5 = libnxpython.NXACC_CREATE5
NXACC_CREATEXML = libnxpython.NXACC_CREATEXML
NX_FLOAT32 = libnxpython.NX_FLOAT32
NX_FLOAT64 = libnxpython.NX_FLOAT64
NX_INT8 = libnxpython.NX_INT8
NX_UINT8 = libnxpython.NX_UINT8
NX_BOOLEAN = libnxpython.NX_BOOLEAN
NX_INT16 = libnxpython.NX_INT16
NX_UINT16 = libnxpython.NX_UINT16
NX_INT32 = libnxpython.NX_INT32
NX_UINT32 = libnxpython.NX_UINT32
NX_INT64 = libnxpython.NX_INT64
NX_UINT64 = libnxpython.NX_UINT64
NX_CHAR = libnxpython.NX_CHAR
create_nxds = libnxpython.create_nxds
create_text_nxds = libnxpython.create_text_nxds
drop_nxds = libnxpython.drop_nxds
get_nxds_rank = libnxpython.get_nxds_rank
get_nxds_type = libnxpython.get_nxds_type
get_nxds_dim = libnxpython.get_nxds_dim
get_nxds_value = libnxpython.get_nxds_value
get_nxds_text = libnxpython.get_nxds_text
put_nxds_value = libnxpython.put_nxds_value
nx_getlasterror = libnxpython.nx_getlasterror
nx_open = libnxpython.nx_open
nx_flush = libnxpython.nx_flush
nx_close = libnxpython.nx_close
nx_makegroup = libnxpython.nx_makegroup
nx_opengroup = libnxpython.nx_opengroup
nx_openpath = libnxpython.nx_openpath
nx_opengrouppath = libnxpython.nx_opengrouppath
nx_closegroup = libnxpython.nx_closegroup
nx_getnextentry = libnxpython.nx_getnextentry
nx_getgroupID = libnxpython.nx_getgroupID
nx_initgroupdir = libnxpython.nx_initgroupdir
nx_makedata = libnxpython.nx_makedata
nx_compmakedata = libnxpython.nx_compmakedata
nx_opendata = libnxpython.nx_opendata
nx_closedata = libnxpython.nx_closedata
nx_putslab = libnxpython.nx_putslab
nx_getslab = libnxpython.nx_getslab
nx_getds = libnxpython.nx_getds
nx_putds = libnxpython.nx_putds
nx_getdata = libnxpython.nx_getdata
nx_putdata = libnxpython.nx_putdata
nx_getinfo = libnxpython.nx_getinfo
nx_getdataID = libnxpython.nx_getdataID
nx_getnextattr = libnxpython.nx_getnextattr
nx_putattr = libnxpython.nx_putattr
nx_getattr = libnxpython.nx_getattr
nx_makelink = libnxpython.nx_makelink
nx_makenamedlink = libnxpython.nx_makenamedlink
nx_opensourcegroup = libnxpython.nx_opensourcegroup
nx_inquirefile = libnxpython.nx_inquirefile
nx_isexternalgroup = libnxpython.nx_isexternalgroup
nx_linkexternal = libnxpython.nx_linkexternal


