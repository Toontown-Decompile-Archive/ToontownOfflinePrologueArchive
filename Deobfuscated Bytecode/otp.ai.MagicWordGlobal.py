# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.ai.MagicWordGlobal
# Compiled at: 2014-04-30 09:53:54
MINIMUM_MAGICWORD_ACCESS = 300
MINIMUM_AI_OBJ_MW_ACCESS = config.GetInt('mw-minimum-ai-manipulation-access', 500)

class MagicError(Exception):
    pass


def ensureAccess(access, msg='Insufficient access'):
    if spellbook.getInvokerAccess() < access:
        raise MagicError(msg)


class Spellbook:

    def __init__(self):
        self.words = {}
        self.alias2word = {}
        self.categories = []
        self.currentInvoker = None
        self.currentTarget = None
        return

    def addWord(self, word):
        self.words[word.name.lower()] = word
        for alias in word.aliases:
            self.alias2word[alias.lower()] = word

    def addCategory(self, category):
        self.categories.append(category)

    def process(self, invoker, target, incantation):
        self.currentInvoker = invoker
        self.currentTarget = target
        word, args = (incantation.split(' ', 1) + [''])[:2]
        try:
            try:
                return self.doWord(word, args)
            except MagicError as e:
                return (
                 e.message, True)
            except Exception:
                return (
                 describeException(backTrace=1), True)

        finally:
            self.currentInvoker = None
            self.currentTarget = None

        return

    def doWord(self, wordName, args):
        word = self.words.get(wordName.lower()) or self.alias2word.get(wordName.lower())
        if not word:
            return ('Unknown magic word!', False)
        else:
            ensureAccess(word.access)
            if self.getTarget() and self.getTarget() != self.getInvoker():
                if word.targetClasses:
                    if not isinstance(self.getTarget(), tuple(word.targetClasses)):
                        raise MagicError('Target is an invalid class! Expected: %s, Got: %s' % (str([ x.__name__ for x in word.targetClasses ]), self.getTarget().__class__.__name__))
                if hasattr(self.getTarget(), 'getAdminAccess'):
                    targetAccess = self.getTarget().getAdminAccess()
                else:
                    targetAccess = MINIMUM_AI_OBJ_MW_ACCESS - 1
                if self.getInvokerAccess() <= targetAccess:
                    raise MagicError('Target must have lower access')
            result = word.run(args)
            if result is not None:
                return (str(result), True)
            return (
             'Magic word executed successfully!', True)

    def getInvoker(self):
        return self.currentInvoker

    def getTarget(self):
        return self.currentTarget

    def getInvokerAccess(self):
        if not self.currentInvoker:
            return 0
        return self.currentInvoker.getAdminAccess()


spellbook = Spellbook()

class MagicWordCategory:

    def __init__(self, name, defaultAccess=500, doc=''):
        self.name = name
        self.defaultAccess = self.getDefinedAccess() or defaultAccess
        self.doc = doc
        self.words = []
        spellbook.addCategory(self)

    def addWord(self, word):
        self.words.append(word)

    def getDefinedAccess(self):
        return config.GetInt('mw-category-' + self.name.replace(' ', '-').lower(), 0)


CATEGORY_UNKNOWN = MagicWordCategory('Unknown')
CATEGORY_GRAPHICAL = MagicWordCategory('Graphical debugging', defaultAccess=300, doc='Magic Words in this category are used to assist developers in locating the cause of graphical glitches.')
CATEGORY_GUI = MagicWordCategory('GUI debugging', defaultAccess=300, doc='These Magic Words are intended to manipulate the on-screen GUI to assist developers in testing/debugging the GUI system.')
CATEGORY_MOBILITY = MagicWordCategory('Mobility cheats', defaultAccess=300, doc='These Magic Words allow you to move around the area/world more easily, allow you to get to areas more quickly.')
CATEGORY_OVERRIDE = MagicWordCategory('Override cheats', defaultAccess=400, doc='These Magic Words let you override normal game logic.')
CATEGORY_CHARACTERSTATS = MagicWordCategory('Character-stats cheats', defaultAccess=400, doc='These Magic Words let you alter the stats (e.g. gags, laff) of Toons.')
CATEGORY_DEBUG = MagicWordCategory('Debug cheats', defaultAccess=300, doc='These are Magic Words that may be useful in debugging, but have an impact on the fairness of the game if you use them, therefore they are considered cheats.')
CATEGORY_MODERATION = MagicWordCategory('Moderation commands', defaultAccess=300, doc='These are Magic Words focused on allowing moderators to deal with unruly players.')
CATEGORY_CAMERA = MagicWordCategory('Camera controls', defaultAccess=300, doc='These Magic Words manually control the camera system, originally implemented with Doomsday.')
CATEGORY_SYSADMIN = MagicWordCategory('Sysadmin commands', defaultAccess=500, doc="These Magic Words are useful for executing/viewing system information. Note that these Magic Words may have an impact on the server's stability and speed, and should be used with caution.")

class MagicWord:

    def __init__(self, name, func, types, access, doc, category, targetClasses, aliases):
        self.name = name
        self.func = func
        self.types = types
        self.access = access
        self.doc = doc
        self.category = category
        self.targetClasses = targetClasses
        self.aliases = aliases
        category.addWord(self)

    def getUsage(self):
        maxArgs = self.func.func_code.co_argcount
        minArgs = maxArgs - (len(self.func.func_defaults) if self.func.func_defaults else 0)
        argnames = self.func.func_code.co_varnames[:maxArgs]
        usageArgs = []
        for x in xrange(minArgs):
            usageArgs.append(argnames[x])

        for x in xrange(minArgs, maxArgs):
            usageArgs.append('[%s]' % argnames[x])

        return (' ').join(usageArgs)

    def parseArgs(self, string):
        maxArgs = self.func.func_code.co_argcount
        minArgs = maxArgs - (len(self.func.func_defaults) if self.func.func_defaults else 0)
        args = string.split(None, maxArgs - 1)[:maxArgs]
        if len(args) < minArgs:
            raise MagicError('Magic word %s requires at least %d arguments' % (self.name, minArgs))
        output = []
        for i, (type, arg) in enumerate(zip(self.types, args)):
            try:
                targ = type(arg)
            except (TypeError, ValueError):
                raise MagicError('Argument %d of magic word %s must be %s' % (i, self.name, type.__name__))

            output.append(targ)

        return output

    def run(self, rawArgs):
        args = self.parseArgs(rawArgs)
        return self.func(*args)


class MagicWordDecorator:

    def __init__(self, name=None, types=[str], access=None, category=CATEGORY_UNKNOWN, targetClasses=[], aliases=[]):
        self.name = name
        self.types = types
        self.category = category
        if access is not None:
            self.access = access
        else:
            self.access = self.category.defaultAccess
        self.targetClasses = targetClasses
        self.aliases = aliases
        return

    def __call__(self, mw):
        name = self.name
        if name is None:
            name = mw.func_name
        config_access = config.GetInt('mw-word-' + name.lower(), 0)
        if config_access:
            self.access = config_access
        word = MagicWord(name, mw, self.types, self.access, mw.__doc__, self.category, self.targetClasses, self.aliases)
        spellbook.addWord(word)
        return mw


magicWord = MagicWordDecorator