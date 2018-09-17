from mycroft import MycroftSkill, intent_file_handler


class SonosTmp(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tmp.sonos.intent')
    def handle_tmp_sonos(self, message):
        self.speak_dialog('tmp.sonos')


def create_skill():
    return SonosTmp()

