''''''

import sys
import os

import nose
from nosegae import NoseGAE
from freshen.noseplugin import FreshenNosePlugin


def freshen_tipfy():
    # Until nosegae is patched, it seems we need to chdir into app
    # for some things to work properly. (Template lookups, etc.)
    os.chdir('app')
    
    # This is a hacky way to set the default arguments. It's only temporary.
    arguments = sys.argv
    arguments.extend([
        '--with-freshen',
        
        '--with-gae',
        '--gae-lib-root=../etc/parts/google_appengine',
        
        'features',])
    
    # Run nose.
    nose.run(argv=arguments)
