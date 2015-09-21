from pathconfig import load_configuration, Factory

## this will make the application look for simple.yml
## in the current directory, then ~/.simple.yml, and
## then /etc/simple.yml (or .../my-virtualenv/etc/simple.yml)
app_config = load_configuration('simple')

class Beast(Factory):
    '''
    an example for the Factory superclass
    '''
    def load_monologue(self):
        '''
        retrieves the configured monologue file
        '''
        return self.open_by_pat('monologue').read()
    def load_noise(self):
        '''
        retrieves the configured noise
        '''
        return self.fname_by_pat('noise_val')

dog = Beast(beast_name='dog',
            monologue_pattern=app_config.config_value('example.$beast_name.monologue'),
            noise_val_pattern=app_config.config_value('example.$beast_name.noise'))

def display_animal(animal):
    print "The %s says %s"%(animal.beast_name, animal.get('noise'))
    print "The monologue of the %s:"%(animal.beast_name)
    print animal.get('monologue')


display_animal(dog)

# note how .bind() keeps the general configuration, but does not copy the
# cached values
cat = dog.bind(beast_name='cat')
display_animal(cat)
