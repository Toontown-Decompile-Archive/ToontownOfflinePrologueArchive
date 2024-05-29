# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: niraimarshal
# Compiled at: 2014-04-30 09:53:54
from cStringIO import StringIO
import marshal, struct, types

def niraicall_obfuscate(code):
    print 'Error:\n    niraicall_obfuscate not implemented\n    \n    Add it to your make file:\n    \n    def niraicall_obfuscate(code):\n        ...\n        \n    niraimarshal.niraicall_obfuscate = niraicall_obfuscate\n    \n    Input: string\n    Output: (bool, string)\n    \n    bool indicates whether the string has been obfuscated or not\n    if True, OBFS is prepend to string\n    if False, string is ignored \n    \n    See sample project for help\n    '
    raise NotImplementedError('niraicall_obfuscate not implemented')


def obfuscate(x):
    obfuscated, code = niraicall_obfuscate(x)
    if obfuscated:
        return 'E' + code
    else:
        return x


def dump(value, file):
    if isinstance(value, types.CodeType):
        dump_code(value, file)
    elif type(value) in (list, tuple):
        file.write('[' if type(value) == list else '(')
        file.write(struct.pack('<I', len(value)))
        for x in value:
            dump(x, file)

    elif type(value) == dict:
        print 'dict'
        file.write('{')
        for k, v in value.items():
            dump(k, file)
            dump(v, file)

        file.write('0')
    else:
        file.write(marshal.dumps(value))


def dump_code(value, file):
    file.write(struct.pack('<cIIII', 'c', value.co_argcount, value.co_nlocals, value.co_stacksize, value.co_flags))
    code = value.co_code
    dump(obfuscate(code), file)
    dump(value.co_consts, file)
    dump(value.co_names, file)
    dump(value.co_varnames, file)
    dump(value.co_freevars, file)
    dump(value.co_cellvars, file)
    dump(value.co_filename, file)
    dump(value.co_name, file)
    file.write(struct.pack('<I', value.co_firstlineno))
    dump(value.co_lnotab, file)


def dumps(value):
    sio = StringIO()
    dump(value, sio)
    return sio.getvalue()