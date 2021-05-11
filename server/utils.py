import os
import pwd
import stat


def file_info(file, user):
    user_info = get_user(user)
    return {
        "filename": file,
        "is_can_read": user_can_read_file(file, user_info),
        "is_can_write": user_can_write_file(file, user_info),
        "is_dir": os.path.isdir(file)
    }


def user_can_write_file(file, user_info):
    return user_can_wrx_file(file, user_info, 'write')


def user_can_read_file(file, user_info):
    return user_can_wrx_file(file, user_info, 'read')


def user_can_wrx_file(file, user_info, behave):
    s = os.stat(file)
    mode = s[stat.ST_MODE]
    if 'write' == behave:
        target_mode = stat.S_IWOTH
    elif "read" == behave:
        target_mode = stat.S_IROTH
    elif "exec" == behave:
        target_mode = stat.S_IEXEC
    return (
        ((s[stat.ST_UID] == user_info['uid']) and (mode & stat.S_IRUSR > 0)) or
        ((s[stat.ST_GID] == user_info['gid']) and (mode & stat.S_IRGRP > 0)) or
        (mode & target_mode > 0)
    )


def get_user(user):
    user_info = pwd.getpwnam(user)
    return {
        "name": user_info.pw_name,
        "uid": user_info.pw_passwd,
        "gid": user_info.pw_gid
    }