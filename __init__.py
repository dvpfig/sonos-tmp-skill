import soco
from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.audio import wait_while_speaking


class SonosTmp(MycroftSkill):
    """
    Control Sonos speaker devices
    
    Use play/pause to control sonos device. 
    """
    
    def __init__(self):
        super(SonosTmp, self).__init__(name="SonosTmp")
        self.zone_list = list(soco.discover())

    # original: @intent_file_handler('tmp.sonos.intent')
    @intent_handler(IntentBuilder("PlaySonos").require("Play").require("Sonos"))
    def handle_play_sonos(self, message):
        self.zone_list.play()
        self.speak_dialog('play.sonos')

        
    @intent_handler(IntentBuilder("PauseSonos").require("Pause").require("Sonos"))
    def handle_pause_sonos(self, message):
        self.zone_list.pause()
        self.speak_dialog('pause.sonos')

def create_skill():
    return SonosTmp()

