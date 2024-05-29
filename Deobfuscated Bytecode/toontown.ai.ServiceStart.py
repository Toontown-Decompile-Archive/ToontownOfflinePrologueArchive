# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: toontown.ai.ServiceStart
# Compiled at: 2014-04-30 09:53:54
import gc
gc.disable()
from pandac.PandaModules import *
from toontown.distributed import PythonUtil
import __builtin__, argparse, os
parser = argparse.ArgumentParser()
parser.add_argument('--base-channel', help='The base channel that the server may use.')
parser.add_argument('--max-channels', help='The number of channels the server may use.')
parser.add_argument('--stateserver', help="The control channel of this AI's designated State Server.")
parser.add_argument('--district-name', help="What this AI Server's district will be named.")
parser.add_argument('--astron-ip', help='The IP address of the Astron Message Director to connect to.')
parser.add_argument('--eventlogger-ip', help='The IP address of the Astron Event Logger to log to.')
args = parser.parse_args()
print ':ToontownAIRepository: Loading settings.'
from toontown.toonbase.GameSettings import GameSettings
settings = GameSettings()
settings.loadFromSettings()
localconfig = ''
if args.base_channel:
    localconfig += 'air-base-channel %s\n' % args.base_channel
if args.max_channels:
    localconfig += 'air-channel-allocation %s\n' % args.max_channels
if args.stateserver:
    localconfig += 'air-stateserver %s\n' % args.stateserver
if args.district_name:
    localconfig += 'district-name %s\n' % args.district_name
if args.astron_ip:
    localconfig += 'air-connect %s\n' % args.astron_ip
if args.eventlogger_ip:
    localconfig += 'eventlog-host %s\n' % args.eventlogger_ip
loadPrcFileData('Command-line', localconfig)

class game:
    name = 'toontown'
    process = 'server'


__builtin__.game = game
from otp.ai.AIBaseGlobal import *
from toontown.ai.ToontownAIRepository import ToontownAIRepository
simbase.air = ToontownAIRepository(config.GetInt('air-base-channel', 401000000), config.GetInt('air-stateserver', 10000), config.GetString('district-name', 'Devhaven'))
host = config.GetString('air-connect', '127.0.0.1')
port = 7199
if ':' in host:
    host, port = host.split(':', 1)
    port = int(port)
simbase.air.connect(host, port)
gc.enable()
gc.collect()
try:
    run()
except SystemExit:
    raise
except Exception:
    if not os.path.exists('logs/'):
        os.mkdir('logs/')
    info = describeException()
    simbase.air.writeServerEvent('ai-exception', avId=simbase.air.getAvatarIdFromSender(), accId=simbase.air.getAccountIdFromSender(), exception=info)
    with open(config.GetString('ai-crash-log-name', 'logs/ai-crash.log'), 'w+') as (file):
        file.write(info + '\n')
    raise