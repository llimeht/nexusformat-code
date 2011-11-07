#ifndef NAPI5_H
#define NAPI5_H

#define NX5SIGNATURE 959695

#include <hdf5.h>

/* HDF5 interface */

extern  NXstatus  NX5open(CONSTCHAR *filename, NXaccess access_method, NXhandle* pHandle);
extern  NXstatus  NX5reopen(NXhandle pOrigHandle, NXhandle* pNewHandle);

extern  NXstatus  NX5close(NXhandle* pHandle);
extern  NXstatus  NX5flush(NXhandle* pHandle);
  
extern  NXstatus  NX5makegroup (NXhandle handle, CONSTCHAR *name, CONSTCHAR* NXclass);
extern  NXstatus  NX5opengroup (NXhandle handle, CONSTCHAR *name, CONSTCHAR* NXclass);
extern  NXstatus  NX5closegroup(NXhandle handle);
  
extern  NXstatus  NX5makedata64 (NXhandle handle, CONSTCHAR* label, int datatype, int rank, int64_t dim[]);
extern  NXstatus  NX5compmakedata64 (NXhandle handle, CONSTCHAR* label, int datatype, int rank, int64_t dim[], int comp_typ, int64_t bufsize[]);
extern  NXstatus  NX5compress (NXhandle handle, int compr_type);
extern  NXstatus  NX5opendata (NXhandle handle, CONSTCHAR* label);
extern  NXstatus  NX5closedata(NXhandle handle);
extern  NXstatus  NX5putdata(NXhandle handle, void* data);

extern  NXstatus  NX5putattr(NXhandle handle, CONSTCHAR* name, void* data, int iDataLen, int iType);
extern  NXstatus  NX5putslab64(NXhandle handle, void* data, int64_t start[], int64_t size[]);    

extern  NXstatus  NX5getdataID(NXhandle handle, NXlink* pLink);
extern  NXstatus  NX5makelink(NXhandle handle, NXlink* pLink);
extern  NXstatus  NX5printlink(NXhandle handle, NXlink* pLink);

extern  NXstatus  NX5getdata(NXhandle handle, void* data);
extern  NXstatus  NX5getinfo64(NXhandle handle, int* rank, int64_t dimension[], int* datatype);
extern  NXstatus  NX5getnextentry(NXhandle handle, NXname name, NXname nxclass, int* datatype);

extern  NXstatus  NX5getslab64(NXhandle handle, void* data, const int64_t start[], const int64_t size[]);
extern  NXstatus  NX5getnextattr(NXhandle handle, NXname pName, int *iLength, int *iType);
extern  NXstatus  NX5getattr(NXhandle handle, char* name, void* data, int* iDataLen, int* iType);
extern  NXstatus  NX5getattrinfo(NXhandle handle, int* no_items);
extern  NXstatus  NX5getgroupID(NXhandle handle, NXlink* pLink);
extern  NXstatus  NX5getgroupinfo(NXhandle handle, int* no_items, NXname name, NXname nxclass);

extern  NXstatus  NX5initgroupdir(NXhandle handle);
extern  NXstatus  NX5initattrdir(NXhandle handle);

void NX5assignFunctions(pNexusFunction fHandle);

herr_t attr_info(hid_t loc_id, const char *name, const H5A_info_t *unused, void *opdata);
herr_t group_info(hid_t loc_id, const char *name, const H5L_info_t *unused, void *opdata);
herr_t nxgroup_info(hid_t loc_id, const char *name, const H5L_info_t *unused, void *op_data);

#endif /* NAPI5_H */
