define config.log = "log.txt"

label after_load:
    $ flags = updateFlags(flags, flag_keys)
    return
