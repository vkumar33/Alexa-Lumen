import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import (
AbstractRequestHandler, AbstractExceptionHandler,
AbstractRequestInterceptor, AbstractResponseInterceptor)
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model.ui import SimpleCard
from ask_sdk_model.dialog import (
    ElicitSlotDirective, DelegateDirective)
from ask_sdk_model import (
    Response, IntentRequest, DialogState, SlotConfirmationStatus, Slot)
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
        
        
        speak_output = ('Hi - I am Lumen, your health coach. Before we get started, Can I please have your name. Start by saying my name is ')
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class GetnameIntentHandler(AbstractRequestHandler):
    """Handler for Getting User Name Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GetnameIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        slots = handler_input.request_envelope.request.intent.slots
        user = slots["UserName"].value
        
        speak_output = (' Hello {user}. Welcome to your first counseling session.<break time="1s"/>'
                        'Before we get started with our session, I need you to complete your PHQ-9 and GAD-7 surveys. '
                        'I texted you the link earlier today. Please complete them now, then restart our session.<break time="1s"/> '
                        'If you have completed the survey then say Survey Completed'
                        ).format(user = user)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .add_directive(DelegateDirective(updated_intent = 'S1M1UthreeaIntent'))
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response)



"""
class PhqcheckIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        #return ask_utils.is_intent_name("PhqcheckIntent")(handler_input)
        return True

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        speak_output = ('Before we get started with our session, I need you to complete your PHQ-9 and GAD-7 surveys. '
                        'I texted you the link earlier today. Please complete them now, then restart our session. ')

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response)



"""


class SlMltwoIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SlMltwoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        speak_output = ('Thank you for completing your PHQ-9 and GAD-7 surveys! I want to introduce myself, I’m Lumen, your virtual coach. <break time="1s"/>' 
        'My role is to help you improve your emotional well-being. '
        'I will work with you on developing a positive approach to thinking about problems, building skills to effectively solve problems, and plan activities.<break time="1s"/> '
        'We will have 8 sessions together and will review your progress along the way.<break time="1s"/> If this sounds good say continue or if you want to hear the instructions again say repeat? ')
        
        
        reprompt = "Tell me if you want to continue or repeat."
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class SlMltwoaIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SlMltwoaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        slots = handler_input.request_envelope.request.intent.slots
        resp = slots["Result"].value
        
        if resp.lower() == "continue":
            speak_output = "I’m looking forward to working together. On a scale from 1 (not at all) – 10 (completely), how ready are you to get started? Start by saying my score is"
            reprompt = "Say a number between 1 (not at all) – 10 (completely) indicating how ready you are to get started. Start by saying my score is "
            
            return (handler_input.response_builder.speak(speak_output).ask(reprompt).response)
        
        else:
            speak_output = ('My role is to help you improve your emotional well-being. '
            'I will work with you on developing a positive approach to thinking about problems, building skills to effectively solve problems, and plan activities.<break time="1s"/> '
            'We will have 8 sessions together and will review your progress along the way.<break time="1s"/>'
            'Say a number between 1 (not at all) – 10 (completely) indicating how ready you are to get started. Start by saying my score is ')
            return (handler_input.response_builder.speak(speak_output).response)
            
            
        

class SlMlthreeaIntentHandler(AbstractRequestHandler):
    """Handler for S1M1U3 Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SlMlthreeaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        #speak_output = "I’m looking forward to working together. On a scale from 1 (not at all) – 10 (completely), how ready are you to get started? Start by saying my score is"
        #reprompt = "Say a number between 1 (not at all) – 10 (completely) indicating how ready you are to get started. Start by saying my score is "
        
        slots = handler_input.request_envelope.request.intent.slots
        score = slots["score"].value
        
        score = int(score)
        
        if score <= 5:
            speak_output = ("That’s okay, we’re going to work through this together! <break time='1s'/>"
            "Now that we’ve gotten to meet each other, I want to give you an overview of the program.")
            
            
        elif score > 5:
            speak_output = ("I’m glad to hear that! <break time='1s'/>"
            "Now that we’ve gotten to meet each other, I want to give you an overview of the program.")
            
        
        return (
            handler_input.response_builder
                .speak(speak_output).set_should_end_session(True)
                .response
        )

"""
class S1M1UthreebIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("threebIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        slots = handler_input.request_envelope.request.intent.slots
        score = slots["score"].value
        
        
        if score <= 5:
            speak_output = ("That’s okay, we’re going to work through this together!")
            
        elif score >= 5:
            speak_output = ("I’m glad to hear that!")
            

        return (
            handler_input.response_builder
                .speak(speak_output)
                #.ask(speak_output)
                .response
        )



class S1M1U4IntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("S1M1U4Intent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        speak_output = ('Now that we’ve gotten to meet each other, I want to give you an overview of the program.')

        return (
            handler_input.response_builder
                .speak(speak_output).set_should_end_session(True)
                .response
        )
"""



class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


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

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

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
sb.add_request_handler(GetnameIntentHandler())
sb.add_request_handler(SlMltwoIntentHandler())
sb.add_request_handler(SlMltwoaIntentHandler())
sb.add_request_handler(SlMlthreeaIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()