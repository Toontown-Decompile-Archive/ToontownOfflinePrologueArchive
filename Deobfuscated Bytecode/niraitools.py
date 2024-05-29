# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: niraitools
# Compiled at: 2014-04-30 09:53:54
from collections import OrderedDict
import subprocess, glob, sys, os, niraimarshal, aes
SOURCE_ROOT = os.path.dirname(os.path.abspath(__file__))
NIRAI_ROOT = os.path.abspath(os.path.join(SOURCE_ROOT, '..'))
PYTHON_ROOT = os.path.join(NIRAI_ROOT, 'python')
PANDA3D_ROOT = os.path.join(NIRAI_ROOT, 'panda3d')
THIRDPARTY_ROOT = os.path.join(PANDA3D_ROOT, 'thirdparty')

class NiraiCompilerBase:

    def __init__(self, output, outputdir='built', includedirs=set(), libs=set(), libpath=set()):
        self.output = output
        self.outputdir = outputdir
        self.includedirs = includedirs.copy()
        self.includedirs.add(os.path.join(PANDA3D_ROOT, 'built', 'include'))
        self.includedirs.add(os.path.join(PYTHON_ROOT, 'Include'))
        self.includedirs.add(SOURCE_ROOT)
        self.libs = libs.copy()
        self.libpath = libpath.copy()
        self.builtLibs = os.path.join(PANDA3D_ROOT, 'built', 'lib')
        self.libpath.add(self.builtLibs)
        self.libpath.add(PYTHON_ROOT)
        self.sources = set()
        self._built = set()

    def add_source(self, filename):
        self.sources.add(filename)

    def add_library(self, lib, thirdparty=False):
        if thirdparty:
            root = os.path.normpath(lib).split(os.sep)[0]
            self.includedirs.add(os.path.join(self.thirdpartydir, root, 'include'))
            lib = os.path.join(self.thirdpartydir, lib)
        self.libs.add(lib)

    def add_nirai_files(self):
        for filename in ('aes.cxx', 'main.cxx'):
            self.add_source(os.path.join(SOURCE_ROOT, filename))

        self.add_library('pythonembed')

    def _run_command(self, cmd):
        p = subprocess.Popen(cmd, stdout=sys.stdout, stderr=sys.stderr, shell=True)
        v = p.wait()
        if v != 0:
            print 'The following command returned non-zero value (%d): %s' % (v, cmd[:100] + '...')
            sys.exit(1)

    def run(self):
        print 'Compiling CXX codes...'
        for filename in self.sources:
            self.compile(filename)

        print 'Linking...'
        self.link()


class NiraiCompilerWindows(NiraiCompilerBase):

    def add_nirai_files(self):
        NiraiCompilerBase.add_nirai_files(self)
        self.thirdpartydir = os.path.join(THIRDPARTY_ROOT, 'win-libs-vc10')
        self.libs |= set(glob.glob(os.path.join(self.builtLibs, '*.lib')))
        self.add_library('ws2_32')
        self.add_library('shell32')
        self.add_library('advapi32')
        self.add_library('gdi32')
        self.add_library('user32')
        self.add_library('oleaut32')
        self.add_library('ole32')
        self.add_library('iphlpapi')
        self.add_library('shell32')
        self.add_library('wsock32')
        self.add_library('opengl32')
        self.add_library('imm32')
        self.add_library('crypt32')
        self.add_library('fftw\\lib\\fftw', thirdparty=True)
        self.add_library('fftw\\lib\\rfftw', thirdparty=True)
        self.add_library('freetype\\lib\\freetype', thirdparty=True)
        self.add_library('jpeg\\lib\\jpeg-static', thirdparty=True)
        self.add_library('nvidiacg\\lib\\cgGL', thirdparty=True)
        self.add_library('nvidiacg\\lib\\cgD3D9', thirdparty=True)
        self.add_library('nvidiacg\\lib\\cg', thirdparty=True)
        self.add_library('ode\\lib\\ode_single', thirdparty=True)
        self.add_library('openal\\lib\\OpenAL32', thirdparty=True)
        self.add_library('openssl\\lib\\libpandaeay', thirdparty=True)
        self.add_library('openssl\\lib\\libpandassl', thirdparty=True)
        self.add_library('png\\lib\\libpng_static', thirdparty=True)
        self.add_library('squish\\lib\\squish', thirdparty=True)
        self.add_library('tiff\\lib\\libtiff', thirdparty=True)
        self.add_library('zlib\\lib\\zlibstatic', thirdparty=True)
        self.add_library('vorbis\\lib\\libogg_static', thirdparty=True)
        self.add_library('vorbis\\lib\\libvorbis_static', thirdparty=True)
        self.add_library('vorbis\\lib\\libvorbisfile_static', thirdparty=True)

    def compile(self, filename):
        out = '%s/%s.obj' % (self.outputdir, os.path.basename(filename).rsplit('.', 1)[0])
        cmd = 'cl /c /GF /MP4 /DPy_BUILD_CORE /DNTDDI_VERSION=0x0501 /wd4996 /wd4275 /wd4267 /wd4101 /wd4273 /nologo /EHsc /MD /Zi /O2'
        for ic in self.includedirs:
            cmd += ' /I"%s"' % ic

        cmd += ' /Fo%s "%s"' % (out, filename)
        self._run_command(cmd)
        self._built.add(out)

    def link(self):
        cmd = 'link /LTCG /LTCG:STATUS /nologo /out:%s/%s' % (self.outputdir, self.output)
        for obj in self._built:
            cmd += ' "%s"' % obj

        for lib in self.libs:
            if not lib.endswith('.obj') and not lib.endswith('.lib'):
                lib += '.lib'
            cmd += ' "%s"' % lib

        for path in self.libpath:
            cmd += ' /LIBPATH:"%s"' % path

        cmd += ' /RELEASE /nodefaultlib:python27.lib /nodefaultlib:libcmt /ignore:4049 /ignore:4006 /ignore:4221'
        self._run_command(cmd)


class NiraiCompilerDarwin(NiraiCompilerBase):

    def __init__(self, *args, **kwargs):
        self.frameworks = kwargs.pop('frameworks', set()).copy()
        self.frameworkDirs = kwargs.pop('frameworkDirs', set()).copy()
        NiraiCompilerBase.__init__(self, *args, **kwargs)

    def add_library(self, lib, thirdparty=False):
        if thirdparty:
            root = os.path.normpath(lib).split(os.sep)[0]
            self.includedirs.add(os.path.join(self.thirdpartydir, root, 'include'))
            lib = os.path.join(self.thirdpartydir, lib)
            self.libpath.add(os.path.join(self.thirdpartydir, root, 'lib'))
        self.libs.add(lib)

    def add_nirai_files(self):
        NiraiCompilerBase.add_nirai_files(self)
        self.thirdpartydir = os.path.join(THIRDPARTY_ROOT, 'darwin-libs-a')
        self.libpath.add(self.builtLibs)
        self.libs |= set(glob.glob(os.path.join(self.builtLibs, '*.a')))
        self.add_library('crypto')
        self.add_library('z')
        self.add_library('ssl')
        self.add_library('freetype/lib/freetype', thirdparty=True)
        self.add_library('jpeg/lib/jpeg', thirdparty=True)
        self.add_library('png/lib/png', thirdparty=True)
        self.add_library('ode/lib/ode', thirdparty=True)
        self.add_library('squish/lib/squish', thirdparty=True)
        self.add_library('tiff/lib/pandatiff', thirdparty=True)
        self.add_library('tiff/lib/pandatiffxx', thirdparty=True)
        self.add_library('vorbis/lib/ogg', thirdparty=True)
        self.add_library('vorbis/lib/vorbis', thirdparty=True)
        self.add_library('vorbis/lib/vorbisenc', thirdparty=True)
        self.add_library('vorbis/lib/vorbisfile', thirdparty=True)
        self.frameworkDirs.add(os.path.join(PANDA3D_ROOT, 'built', 'Frameworks'))
        self.frameworks.add('AppKit')
        self.frameworks.add('OpenAL')
        self.frameworks.add('OpenGL')
        self.frameworks.add('Cg')
        self.frameworks.add('AGL')
        self.frameworks.add('Carbon')
        self.frameworks.add('Cocoa')

    def compile(self, filename):
        print filename
        out = '%s/%s.o' % (self.outputdir, os.path.basename(filename).rsplit('.', 1)[0])
        cmd = 'g++ -c -DPy_BUILD_CORE -ftemplate-depth-70 -fPIC -O2 -Wno-deprecated-declarations -pthread'
        for ic in self.includedirs:
            cmd += ' -I"%s"' % ic

        cmd += ' -o "%s" "%s"' % (out, filename)
        self._run_command(cmd)
        self._built.add(out)

    def link(self):
        cmd = 'g++ -o %s/%s' % (self.outputdir, self.output)
        for path in self.libpath:
            cmd += ' -L"%s"' % path

        for path in self.frameworkDirs:
            cmd += ' -F"%s"' % path

        for framework in self.frameworks:
            cmd += ' -framework %s' % framework

        for lib in self.libs:
            lib = os.path.basename(lib)
            if lib.startswith('lib'):
                lib = lib[3:]
            if lib.endswith('.a'):
                lib = lib[:-2]
            cmd += ' -l%s' % lib

        for obj in self._built:
            cmd += ' "%s"' % obj

        cmd += ' -dylib_file /System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGL.dylib'
        cmd += ':/System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGL.dylib'
        self._run_command(cmd)


class NiraiPackager:
    HEADER = 'NRI\n'

    def __init__(self, outfile):
        self.modules = OrderedDict()
        self.outfile = outfile

    def __read_file(self, filename, mangler=None):
        with open(filename, 'rb') as (f):
            data = f.read()
        base = filename.rsplit('.', 1)[0].replace('\\', '/').replace('/', '.')
        pkg = base.endswith('.__init__')
        moduleName = base.rsplit('.', 1)[0] if pkg else base
        name = moduleName
        if mangler is not None:
            name = mangler(name)
        if not name:
            return ('', ('', 0))
        else:
            try:
                data = self.compile_module(name, data)
            except:
                print 'WARNING: Failed to compile', filename
                return ('', ('', 0))

            size = len(data) * (-1 if pkg else 1)
            return (name, (data, size))

    def compile_module(self, name, data):
        return niraimarshal.dumps(compile(data, name, 'exec'))

    def add_module(self, moduleName, data, size=None, compile=False, negSize=False):
        if compile:
            data = self.compile_module(moduleName, data)
        if size is None:
            size = len(data)
            if negSize:
                size = -size
        self.modules[moduleName] = (
         data, size)
        return

    def add_file(self, filename, mangler=None):
        print 'Adding file', filename
        moduleName, (data, size) = self.__read_file(filename, mangler)
        if moduleName:
            moduleName = os.path.basename(filename).rsplit('.', 1)[0]
            self.add_module(moduleName, data, size)

    def add_directory(self, dir, mangler=None):
        print 'Adding directory', dir

        def _recurse_dir(dir):
            for f in os.listdir(dir):
                f = os.path.join(dir, f)
                if os.path.isdir(f):
                    _recurse_dir(f)
                elif f.endswith('py'):
                    moduleName, (data, size) = self.__read_file(f, mangler)
                    if moduleName:
                        self.add_module(moduleName, data, size)

        _recurse_dir(dir)

    def get_mangle_base(self, path, relative=True):
        abs = os.path.abspath(path)
        norm = os.path.normpath(abs)
        if relative:
            rel = os.path.relpath(norm)
        else:
            rel = norm
        return len(rel) + len(os.sep)

    def add_panda3d_dirs(self):
        manglebase = self.get_mangle_base(os.path.join(NIRAI_ROOT, 'panda3d', 'built'), relative=False)

        def _mangler(name):
            name = name[manglebase:].strip('.')
            if name == 'direct.extensions_native.extension_native_helpers':
                name = 'extension_native_helpers'
            return name

        self.add_directory(os.path.join(NIRAI_ROOT, 'panda3d', 'built', 'direct'), mangler=_mangler)
        self.add_directory(os.path.join(NIRAI_ROOT, 'panda3d', 'built', 'pandac'), mangler=_mangler)
        self.add_directory(os.path.join(NIRAI_ROOT, 'panda3d', 'built', 'panda3d'), mangler=_mangler)

    def add_default_lib(self):
        manglebase = self.get_mangle_base(os.path.join(NIRAI_ROOT, 'python', 'Lib'), relative=False)

        def _mangler(name):
            name = name[manglebase:]
            return name.strip('.')

        self.add_directory(os.path.join(NIRAI_ROOT, 'python', 'Lib'), mangler=_mangler)

    def write_out(self):
        f = open(self.outfile, 'wb')
        f.write(self.HEADER)
        f.write(self.process_modules())
        f.close()

    def generate_key(self, size=256):
        return os.urandom(size)

    def dump_key(self, key):
        for k in key:
            print ord(k),

        print

    def process_modules(self):
        raise NotImplementedError('process_modules')

    def get_file_contents(self, filename, encrypt=False):
        with open(filename, 'rb') as (f):
            data = f.read()
        if encrypt:
            iv = self.generate_key(16)
            key = self.generate_key(16)
            data = iv + key + aes.encrypt(data, key, iv)
        return data


if sys.platform.startswith('win'):
    NiraiCompiler = NiraiCompilerWindows
elif sys.platform == 'darwin':
    NiraiCompiler = NiraiCompilerDarwin
else:

    class NiraiCompiler:

        def __init__(self, *args, **kw):
            raise RuntimeError('Attempted to use NiraiCompiler on unsupported platform: %s' % sys.platform)