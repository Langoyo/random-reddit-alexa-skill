  # -*- coding: utf-8 -*-
"""Simple fact sample app."""

import random
import logging
import praw
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractExceptionHandler,
    AbstractRequestInterceptor, AbstractResponseInterceptor)
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response


# =========================================================================================================================================
# TODO: The items below this comment need your attention.
# =========================================================================================================================================
SKILL_NAME = "random Reddit"
WLLCOME_MESSAGE = "Welcome! I can search content from different reddit comminities like r/showerthoughts, r/jokes, r/poems, r/news or r/quotes. You can use me by saying: tell me a shower thought, tell me a joke, tell me a quote, headline or poem."
HELP_MESSAGE = "I can search content from different reddit comminities like r/showerthoughts, r/jokes, r/poems, r/news or r/quotes. You can use me by saying: tell me a shower thought, tell me a joke, tell me a quote, headline or poem."
HELP_REPROMPT = HELP_MESSAGE
STOP_MESSAGE = "Goodbye!"
FALLBACK_MESSAGE = "What can I help you with?"
FALLBACK_REPROMPT = 'What can I help you with?'
EXCEPTION_MESSAGE = "Sorry. I had some problems. Try again please"


sb = SkillBuilder()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def getTime():
    times = ["all","year","month","day"]
    return random.choice(times)
    
def getPromptTitle(sub):
    reddit = praw.Reddit(client_id="",
                client_secret="",
                user_agent="")
        
        
    prompts = []
        
    time = getTime()
        
    for submission in reddit.subreddit(sub).top(time):
        prompts.append(submission.title)
        
    return random.choice(prompts)

def getPromptTitleAndText(sub):
    reddit = praw.Reddit(client_id="",
                client_secret="",
                user_agent="")
        
        
    prompts = []
        
    time = getTime()
        
    for submission in reddit.subreddit(sub).top(time):
        prompts.append(submission.title + ". " + submission.selftext)
        
    return random.choice(prompts)





class GetQuoteHandler(AbstractRequestHandler):
    """Handler for Skill Launch and GetNewFact Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("quoteRequest")(handler_input) )

    def handle(self, handler_input):
       # type: (HandlerInput) -> Response
        logger.info("In quote")
        

        speech = getPromptTitle("quotes")
        attr = handler_input.attributes_manager.session_attributes
        attr["last_prompt"] = speech
        
        return (handler_input.response_builder
                .speak(speech)
                .ask(speech)
                .response
        )



class GetJokeHandler(AbstractRequestHandler):
    """Handler for Skill Launch and GetNewFact Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("jokeRequest")(handler_input) )

    def handle(self, handler_input):
       # type: (HandlerInput) -> Response
        logger.info("In joke")
        
        speech = getPromptTitleAndText("Jokes")
        attr = handler_input.attributes_manager.session_attributes
        attr["last_prompt"] = speech
        return (handler_input.response_builder
                .speak(speech)
                .ask(speech)
                .response
        )


class GetPoemHandler(AbstractRequestHandler):
    """Handler for Skill Launch and GetNewFact Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("poemRequest")(handler_input) )

    def handle(self, handler_input):
       # type: (HandlerInput) -> Response
        logger.info("In poem")
        
        speech = getPromptTitleAndText("poetry")
        attr = handler_input.attributes_manager.session_attributes
        attr["last_prompt"] = speech
        
        return (handler_input.response_builder
                .speak(speech)
                .ask(speech)
                .response
        )

class GetHeadlineHandler(AbstractRequestHandler):
    """Handler for Skill Launch and GetNewFact Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("headlinesRequest")(handler_input) )

    def handle(self, handler_input):
       # type: (HandlerInput) -> Response
        logger.info("In GetNewFactHandler")
        
        reddit = praw.Reddit(client_id="",
                client_secret="",
                user_agent="")
        
        
        prompts = []
        
        time = getTime()
        
        for submission in reddit.subreddit("news+worldnews").hot(limit = 50):
            prompts.append(submission.title)
        
        speech = random.choice(prompts)
        attr = handler_input.attributes_manager.session_attributes
        attr["last_prompt"] = speech
        
        return (handler_input.response_builder
                .speak(speech)
                .ask(speech)
                .response
        )



class GetNewShowerthoughtHandler(AbstractRequestHandler):
    """Handler for Skill Launch and GetNewFact Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("showerThoughtRequest")(handler_input))
        
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetNewShowerthoughtHandler")
        

        speech = getPromptTitle("Showerthoughts")
        attr = handler_input.attributes_manager.session_attributes
        attr["last_prompt"] = speech
        
        return (handler_input.response_builder
                .speak(speech)
                .ask(speech)
                .response
        )
        
        
class GetPickupLineHandler(AbstractRequestHandler):
    """Handler for Skill Launch and GetNewFact Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("pickupLineRequest")(handler_input))
        
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GePixck")
        

        speech = getPromptTitleAndText("pickuplines")
        attr = handler_input.attributes_manager.session_attributes
        attr["last_prompt"] = speech
        
        return (handler_input.response_builder
                .speak(speech)
                .ask(speech)
                .response
        )

class repeatHandler(AbstractRequestHandler):
    """Handler for Skill Launch and GetNewFact Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("repeatRequest")(handler_input))
        
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In Repeat handler")
        
        attr = handler_input.attributes_manager.session_attributes
        speech = attr["last_prompt"]
        
        return (handler_input.response_builder
                .speak(speech)
                .ask(speech)
                .response
        )

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return  is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In HelpIntentHandler")
        attr = handler_input.attributes_manager.session_attributes
        attr["last_prompt"] = "Ask something first!"
        speech = WLLCOME_MESSAGE
        return (handler_input.response_builder
                .speak(speech)
                .ask(speech)
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return  is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In HelpIntentHandler")

        return (handler_input.response_builder
                .speak(HELP_MESSAGE)
                .ask(HELP_MESSAGE)
                .response
        )



class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In CancelOrStopIntentHandler")

        handler_input.response_builder.speak(STOP_MESSAGE)
        return handler_input.response_builder.response


class FallbackIntentHandler(AbstractRequestHandler):
    """Handler for Fallback Intent.

    AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")

        handler_input.response_builder.speak(FALLBACK_MESSAGE).ask(
            FALLBACK_REPROMPT)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SessionEndedRequestHandler")

        logger.info("Session ended reason: {}".format(
            handler_input.request_envelope.request.reason))
        return handler_input.response_builder.response


# Exception Handler
class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.info("In CatchAllExceptionHandler")
        logger.error(exception, exc_info=True)

        handler_input.response_builder.speak(EXCEPTION_MESSAGE).ask(
            HELP_REPROMPT)

        return handler_input.response_builder.response


# Request and Response loggers
class RequestLogger(AbstractRequestInterceptor):
    """Log the alexa requests."""
    def process(self, handler_input):
        # type: (HandlerInput) -> None
        logger.debug("Alexa Request: {}".format(
            handler_input.request_envelope.request))


class ResponseLogger(AbstractResponseInterceptor):
    """Log the alexa responses."""
    def process(self, handler_input, response):
        # type: (HandlerInput, Response) -> None
        logger.debug("Alexa Response: {}".format(response))


# Register intent handlers
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(GetQuoteHandler())
sb.add_request_handler(GetNewShowerthoughtHandler())
sb.add_request_handler(GetJokeHandler())
sb.add_request_handler(GetPoemHandler())
sb.add_request_handler(GetHeadlineHandler())
sb.add_request_handler(GetPickupLineHandler())
sb.add_request_handler(repeatHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

# Register exception handlers
sb.add_exception_handler(CatchAllExceptionHandler())

# TODO: Uncomment the following lines of code for request, response logs.
sb.add_global_request_interceptor(RequestLogger())
sb.add_global_response_interceptor(ResponseLogger())

# Handler name that is used on AWS lambda
lambda_handler = sb.lambda_handler()

