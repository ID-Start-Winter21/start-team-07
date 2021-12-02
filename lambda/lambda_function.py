# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import json
import ask_sdk_core.utils as ask_utils
import random 
import requests

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model.interfaces.audioplayer import AudioItem, Stream, PlayDirective, PlayBehavior
from utils import create_presigned_url

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Guten Morgen, {name}. Oh je, du siehst verschlafen aus aber das kriegen wir schon hin. Wie geht es dir denn heute?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class antwort_positivHandler(AbstractRequestHandler):
    """Handler for antwort_positiv."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("antwort_positiv")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Das freut mich, Wie willst du deine Morgenroutine starten ? "

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class antwort_negativHandler(AbstractRequestHandler):
    """Handler for antwort_negativ."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("antwort_negativ")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = random.choice(["Atme tief durch. Es ist nur ein schlechter Tag, kein schlechtes Leben. Zwinkersmiley. Wie willst du deine Morgenroutine starten ?", 
                                    "Nach jeder dunklen Nacht, folgt ein heller Tag. Wie willst du deine Morgenroutine starten ?" , 
                                    "Es gibt Tage, an denen du denkst, dass du untergehst. Aber wie stark du wirklich bist, merkst du erst, wenn du es überstanden hast. Wie willst du deine Morgenroutine starten ?",
                                    "Es ist wie es ist. Aber es wird, was du darauf machst. Wie willst du deine Morgenroutine starten ?",
                                    "Halt den Kopf hoch, da oben ist die Luft besser! Wie willst du deine Morgenroutine starten ?",
                                    "Nutze den Tag und mache das beste daraus. Trübsal kannst du blasen, wenn du schläfst. Wie willst du deine Morgenroutine starten ?"])

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )        

class duschenHandler(AbstractRequestHandler):
    """Handler for duschen."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("duschen")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Gute Idee. Auch wenn ich keine Geruchssensoren habe, rieche ich dich bis ins Amazon Office. HA HA HA, Kleiner Spass. Möchtest du dass ich deine Duschplaylist abspiele oder willst du lieber eine ruhige, entspannte Dusche?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("Sage mir einfach ob du mit deiner Playlist duschen möchtest oder heute vielleicht in ruhe duschen möchtest")
                .response
        )        

class duschplaylistHandler(AbstractRequestHandler):
    """Handler for duschplaylist."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("duschplaylist")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Juhuuu! Deine Duschparty fängt jetzt an. Viel Spaß! Sage Ich bin fertig mit duschen, wenn du aus der Dusche raus bist." '<audio src="https://morgenroutine.s3.amazonaws.com/RPReplay_Final1638197530.mp3"/>' "Du hast jetzt aber schon ganz schön viel Wasser verbraucht gell? Möchtest du wirklich weiterduschen oder soll ich deine Playlist beenden?"


        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class weiter_duschenHandler(AbstractRequestHandler):
    """Handler for duschplaylist."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("weiter_duschen")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Alles klar. Die Wasserrechnung diesen Monat wird aber ganz schön teuer." '<audio src="https://morgenroutine.s3.amazonaws.com/RPReplay_Final1638197530.mp3"/>' "Super. Wir sind fertig geduscht. Wie möchtest du nun fortfahren?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class duschen_stoppenHandler(AbstractRequestHandler):
    """Handler for duschplaylist."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("duschen_stoppen")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Alles klar. Die Wasserrechnung diesen Monat wird aber ganz schön teuer." + '<audio src="https://morgenroutine.s3.amazonaws.com/RPReplay_Final1638197530.mp3"/>' 

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class ruhige_duscheHandler(AbstractRequestHandler):
    """Handler for ruhige_dusche."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ruhige_dusche")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Okay. Dann duschen wir heute wohl leise. Sage Ich bin fertig mit duschen, wenn du aus der Dusche raus bist. " 
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class zaehneputzenHandler(AbstractRequestHandler):
    """Handler for zaehneputzen."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("zaehneputzen")(handler_input)

    def handle(self, handler_input):
        
        speak_output = '<amazon:domain name="fun">Okey. Wir starten mit deinem drei minütigen Musik-Timer.</amazon:domain>' + '<audio src="https://morgenroutine.s3.amazonaws.com/RPReplay_Final1.mp3"/>' + '<amazon:domain name="long-form">Super gemacht! Jetzt sind deine Zähne blitze blanke sauber. Wie möchtest du nun fortfahren ?</amazon:domain>' # weiter duschen  wasserverbrauch
         
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class aufgabenHandler(AbstractRequestHandler):
    """Handler for aufgaben."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("aufgaben")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Deine Heutigen Aufgaben sind: Rasen mähen, Prüfungsanmeldung erledigen und du hast einen Termin beim Zahnarzt um 16 Uhr. Vergiss bloß keinen deiner Termine! Mit was möchtest du nun weitermachen?  " #break einfügen ?  

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class wetterHandler(AbstractRequestHandler):
    """Handler for Get Weather Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("wetter")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        api_url= "http://api.openweathermap.org/data/2.5/weather?q=München&appid=b9ad6b1c8e80f623ff23a53cdd8832a9&units=metric"
        json_data = requests.get(api_url).json()
        weather_json = json_data['weather'][0]['main']
        if weather_json == "Snow":
            weather_json = "am Schneien"
        if weather_json == "Rain":
            weather_json = "Regnerisch"
        if weather_json == "Clouds":
            weather_json = "Bewölkt"
        if weather_json == "Sun":
            weather_json = "Sonnig"
        if weather_json == "Wind":
            weather_json = "Windig"
        temp_json = round(json_data['main']['temp'] )
        city = "München"
        speak_output = "Aktuell ist es {} und die Temperatur beträgt {} °C in {}. " .format(weather_json, temp_json, city)
        reprompt = "Möchtest du nochmal das Wetter abfragen?"
        handler_input.response_builder
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt)
                .response
        )

class nachrichtenHandler(AbstractRequestHandler):
    """Handler for nachrichten."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("nachrichten")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hier sind die Nachrichten von heute. Geimpft, genesen, getestet: In Kürze gilt 3G in Bus und Bahn. Was Fahrgäste jetzt wissen müssen. Mit was möchtest du jetzt weitermachen? " 

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class fun_factHandler(AbstractRequestHandler):
    """Handler for Hello funfact."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("fun_fact")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = random.choice(["Wusstest du, dass der Uranus 70 Jahre lang Georg hieß? Witzig oder?", 
                                    "Würde ein Baby jedes Jahr im selben Tempo weiterwachsen wie in seinem ersten Lebensjahr, wäre es an seinem 18. Geburtstag ungefähr 5 Meter groß." , 
                                    "Jeder sechste deutsche Arzt der inneren Medizin wurde schon mindestens einmal von einem Patienten verprügelt.", 
                                    "Otter legen sich zum Schlafen auf den Rücken und halten dabei Händchen. Damit sorgen sie dafür, dass sie im Wasser nicht voneinander wegtreiben,Wie niedlich, oder ",
                                    "Wusstest du, dass Hippopotamomonstrosesquipedaliophobie der offizielle Name für die Angst vor langen Wörtern ist?. Ironisch, oder nicht",
                                    "Wusstest du, dass Sommerloch, Katzenhirn und Langweiler echt Orte in Deutschland sich?",
                                    "Die Royals haben einige merkwürdige Regeln zu befolgen. Unter anderem ist es den Mitgliedern des britischen Königshauses nicht erlaubt, Monopoly zu spielen, da das Spiel zu viel Potenzial für Streit birgt.",
                                    "Koalas bekommen Schluckauf, wenn sie gestresst sind. Manchmal beginnen sie dann sogar, zusätzlich nervös mit den Ohren zu wackeln. Warum sie das tun, ist bisher nicht erforscht.",
                                    "Ein lustiges Gesetz: In der amerikanischen Stadt Daytona ist es verboten, Mülltonnen sexuell zu belästigen.",
                                    "Wusstest du, dass es in Frankreich verboten ist, Schweine Napoleon zu nennen?"])

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Eigentlich kann ich garnichts. Mit diesen Optionen kann ich dir behilflich sein: Ich kann dein Patner beim Zähne putzen oder auch beim Duschen sein. Außerdem kann ich dir die heutigen Nachrichten vorlesen, den Wetterbericht sagen, Funfacts erzählen oder dir deine Aufgaben für heute nennen. "
        reprompt_text = "Wie möchtest du deine Morgenroutine fortfahren?"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt_text)
                .response
        )


class StopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = random.choice(["Ciao Kakao. Ich wünsche dir noch einen wundervollen Tag. Bis morgen", 
                                    "Tschö mit ö. Ich wünsche dir noch einen wundervollen Tag. Bis morgen." , 
                                    "servus. Ich wünsche dir noch einen wundervollen Tag. Bis morgen.", 
                                    "Aufwiederschauen und reingehauen. Ich wünsche dir noch einen wundervollen Tag. Bis morgen."])

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class fertig_duschenHandler(AbstractRequestHandler):
    """Single handler for fertig_duschen."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("fertig_duschen")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = ""

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class CancelIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = ""

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class nachrichtenHandler(AbstractRequestHandler):
    """Handler for nachrichten."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("nachrichten")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hier sind die Nachrichten von heute. Geimpft, genesen, getestet: In Kürze gilt 3G in Bus und Bahn. Was Fahrgäste jetzt wissen müssen. Mit was möchtest du jetzt weitermachen? " 

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, ich habe Dich nicht verstanden."
        reprompt = "Wie bitte?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Entschuldige mich ich konnte nicht folgen. Kannst du dich bitte wiederholen"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(antwort_positivHandler())
sb.add_request_handler(antwort_negativHandler())
sb.add_request_handler(duschenHandler())
sb.add_request_handler(duschplaylistHandler())
sb.add_request_handler(weiter_duschenHandler())
sb.add_request_handler(duschen_stoppenHandler())
sb.add_request_handler(ruhige_duscheHandler())
sb.add_request_handler(zaehneputzenHandler())
sb.add_request_handler(fun_factHandler())
sb.add_request_handler(aufgabenHandler())
sb.add_request_handler(wetterHandler())
sb.add_request_handler(nachrichtenHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(StopIntentHandler())
sb.add_request_handler(CancelIntentHandler())
sb.add_request_handler(fertig_duschenHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()