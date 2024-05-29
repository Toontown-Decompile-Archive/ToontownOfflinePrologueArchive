# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: build.make
# Compiled at: 2014-04-30 09:53:54
import argparse, sys, os
if not os.path.exists('built'):
    os.mkdir('built')
sys.path.append('../../src')
from panda3d.core import Datagram
from niraitools import *
parser = argparse.ArgumentParser()
parser.add_argument('--compile-cxx', '-c', action='store_true', help='Compile the CXX codes and generate TTOffEngine.exe into built.')
parser.add_argument('--make-bin', '-n', action='store_true', help='Generate TTOffGame.bin.')
parser.add_argument('--make-mfs', '-m', action='store_true', help='Pack resources into .mf files.')
args = parser.parse_args()

def niraicall_obfuscate(code):
    if len(code) % 4:
        return (False, None)
    else:
        code = code[::-1]
        key = [
         'F', 'Q', 'H', 'C', 'Z', 'A', 'Y', 'T', 'L', 'B', 
         'E', 'R']
        output = []
        for i in xrange(len(code)):
            xor_num = ord(code[i]) ^ ord(key[i % len(key)])
            output.append(chr(xor_num))

        code = ('').join(output)
        return (
         True, code)


niraimarshal.niraicall_obfuscate = niraicall_obfuscate

class ToontownPackager(NiraiPackager):
    HEADER = 'TTOFFPROLOGUE'
    BASEDIR = '..' + os.sep

    def __init__(self, outfile):
        NiraiPackager.__init__(self, outfile)
        self.__manglebase = self.get_mangle_base(self.BASEDIR)
        self.add_panda3d_dirs()
        self.add_default_lib()
        self.add_directory(self.BASEDIR, mangler=self.__mangler)
        self.add_toontown_dirs()

    def __mangler(self, name):
        name = name[self.__manglebase:].strip('.')
        return name

    def add_toontown_dirs(self):
        self.add_directory(os.path.join(self.BASEDIR, 'otp'), mangler=self.__mangler)
        self.add_directory(os.path.join(self.BASEDIR, 'toontown'), mangler=self.__mangler)

    def generate_niraidata(self):
        print 'Generating niraidata'
        config = self.get_file_contents('../config/public_client.prc')
        config_iv = self.generate_key(16)
        config_key = self.generate_key(16)
        config = config_iv + config_key + aes.encrypt(config, config_key, config_iv)
        niraidata = 'CONFIG = %r' % config
        niraidata += '\nDC = %r' % self.get_file_contents('../astron/ttoff.dc', True)
        self.add_module('niraidata', niraidata, compile=True)

    def process_modules(self):
        dg = Datagram()
        dg.addUint32(len(self.modules))
        for moduleName in self.modules:
            data, size = self.modules[moduleName]
            dg.addString(moduleName)
            dg.addInt32(size)
            dg.appendData(data)

        data = dg.getMessage()
        iv = self.generate_key(16)
        key = self.generate_key(16)
        fixed_key = ('').join(chr((i ^ 7 * i + 16) % ((i + 5) * 3)) for i in xrange(16))
        fixed_iv = ('').join(chr((i ^ 2 * i + 53) % ((i + 9) * 6)) for i in xrange(16))
        securekeyandiv = aes.encrypt(iv + key, fixed_key, fixed_iv)
        return securekeyandiv + aes.encrypt(data, key, iv)


if args.compile_cxx:
    compiler = NiraiCompiler('TTOffEngine.exe', libs=set(glob.glob('../../libpandadna/built/libpandadna.dir/Release/*.obj')))
    compiler.add_nirai_files()
    compiler.add_source('src/TTOffEngine.cxx')
    compiler.run()
if args.make_bin:
    pkg = ToontownPackager('built/TTOffGame.bin')
    pkg.add_file('NiraiStart.py')
    pkg.generate_niraidata()
    pkg.write_out()
if args.make_mfs:
    os.chdir('..')
    phases = [
     'phase_3', 
     'phase_3.5', 
     'phase_4', 
     'phase_5', 
     'phase_5.5', 
     'phase_6', 
     'phase_7', 
     'phase_8', 
     'phase_9', 
     'phase_10', 
     'phase_11', 
     'phase_12', 
     'phase_13', 
     'phase_14']
    for phase in phases:
        if phase == 'phase_14':
            password = raw_input('phase_14 password: ')
            if not password:
                print 'No password specified; not encrypting phase_14.'
                cmd = 'multify -cf build/built/%s.mf %s' % (phase, phase)
            else:
                print 'Encrypting phase_14 with provided password...'
                cmd = 'multify -cf build/built/%s.mf -ep %s %s' % (phase, password, phase)
        else:
            cmd = 'multify -cf build/built/%s.mf %s' % (phase, phase)
        p = subprocess.Popen(cmd, stdout=sys.stdout, stderr=sys.stderr, shell=True)
        v = p.wait()
        if v != 0:
            print 'The following command returned non-zero value (%d): %s' % (v, cmd[:100] + '...')
            sys.exit(1)