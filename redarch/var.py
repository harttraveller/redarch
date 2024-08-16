# For some reason, 2**31 works best. 2**32 breaks stuff.
ZST_MAX_WINDOW_SIZE_CONSTANT: int = 1 << 31
