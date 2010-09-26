'''
'''

import logging, os

import zc.recipe.egg


class Recipe(zc.recipe.egg.Scripts):
    
    def __init__(self, buildout, name, options):
        self.name, self.options = name, options
        
        # Set a logger with the section name.
        self.logger = logging.getLogger(name)
        
        self.eggs_dir = buildout['buildout']['eggs-directory']
        self.parts_dir = buildout['buildout']['parts-directory']
        self.temp_dir = os.path.join(self.parts_dir, 'temp')
        self.buildout_dir = buildout['buildout']['directory']
        
        features_dir = options.get('features-dir', 'app/features')
        self.features_dir = os.path.abspath(features_dir)
        
        # Set default values.
        defaults = {
            'sdk-directory':os.path.join(self.parts_dir, 'google_appengine'),
            'extra-paths':'',
            'eatures-directory':os.path.join(self.buildout_dir,
                                             'app', 'features'),
        }
        
        defaults.update(options)
        options = defaults
        
        # Set normalized paths.
        self.sdk_dir = os.path.abspath(options['sdk-directory'])
        
        # Set the scripts to be generated. (function, name)
        self.scripts = [
            ('freshen_tipfy', 'freshen_tipfy',)
        ]
        
        super(Recipe, self).__init__(buildout, name, options)

    def install(self):
        # Create the script entrypoints
        entry_points = []
        for function, name in self.scripts:
            entry_points.append(
                '%s=freshentipfy.scripts:%s' %  (function, name))
        
        self.options.update({'entry-points':' '.join(entry_points),})
        
        return super(Recipe, self).install()
    
    def update(self):
        return super(Recipe, self).update()
