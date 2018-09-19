import soco

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

class SonosTmpSkill(MycroftSkill):
    """
    Control Sonos speaker devices
    
    Use play/pause to control sonos device. 
    """
    
    def __init__(self):
        super(SonosTmpSkill, self).__init__(name="SonosTmpSkill")
        
        # Initialize working variables used within the skill.
        self.zone_list = list(soco.discover())
    
        # Create log info
        LOG.info("Sonos devices found: ")
        LOG.info(self.zone_list)

    @intent_handler_intent(IntentBuilder("PlaySonos").require("Play").require("Sonos"))
    def handle_play_sonos(self, message):
        LOG.debug("Starting play sonos action.")
        self.zone_list[0].play()
        self.speak_dialog('play.sonos')

        
    @intent_handler(IntentBuilder("PauseSonos").require("Pause").require("Sonos"))
    def handle_pause_sonos(self, message):
        LOG.debug("Starting pause sonos action.")
        self.zone_list[0].pause()
        self.speak_dialog('pause.sonos')

def create_skill():
    return SonosTmpSkill()

