import os

enable_hpc_rl = os.environ.get('ENABLE_DI_HPC', 'false').lower() == 'true'
enable_linklink = os.environ.get('ENABLE_LINKLINK', 'false').lower() == 'true'
enable_numba = True
