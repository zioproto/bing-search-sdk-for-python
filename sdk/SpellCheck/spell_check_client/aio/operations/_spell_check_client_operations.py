# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6320, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class SpellCheckClientOperationsMixin:

    async def spell_checker(
        self,
        x_bing_apis_sdk: Union[str, "_models.XBingApisSDK"],
        text: str,
        accept: Optional[str] = None,
        accept_language: Optional[str] = None,
        pragma: Optional[str] = None,
        user_agent_parameter: Optional[str] = None,
        client_id: Optional[str] = None,
        client_ip: Optional[str] = None,
        location: Optional[str] = None,
        action_type: Optional[Union[str, "_models.ActionType"]] = None,
        app_name: Optional[str] = None,
        country_code: Optional[str] = None,
        client_machine_name: Optional[str] = None,
        doc_id: Optional[str] = None,
        market: Optional[str] = None,
        session_id: Optional[str] = None,
        set_lang: Optional[str] = None,
        user_id: Optional[str] = None,
        mode: Optional[Union[str, "_models.Mode"]] = None,
        pre_context_text: Optional[str] = None,
        post_context_text: Optional[str] = None,
        **kwargs
    ) -> "_models.SpellCheck":
        """The Bing Spell Check API lets you perform contextual grammar and spell checking. Bing has developed a web-based spell-checker that leverages machine learning and statistical machine translation to dynamically train a constantly evolving and highly contextual algorithm. The spell-checker is based on a massive corpus of web searches and documents.

        The Bing Spell Check API lets you perform contextual grammar and spell checking. Bing has
        developed a web-based spell-checker that leverages machine learning and statistical machine
        translation to dynamically train a constantly evolving and highly contextual algorithm. The
        spell-checker is based on a massive corpus of web searches and documents.

        :param x_bing_apis_sdk: Activate swagger compliance.
        :type x_bing_apis_sdk: str or ~spell_check_client.models.XBingApisSDK
        :param text: The text string to check for spelling and grammar errors. The combined length of
         the text string, preContextText string, and postContextText string may not exceed 10,000
         characters. You may specify this parameter in the query string of a GET request or in the body
         of a POST request. Because of the query string length limit, you'll typically use a POST
         request unless you're checking only short strings.
        :type text: str
        :param accept: The default media type is application/json. To specify that the response use
         `JSON-LD <http://json-ld.org/>`_\ , set the Accept header to application/ld+json.
        :type accept: str
        :param accept_language: A comma-delimited list of one or more languages to use for user
         interface strings. The list is in decreasing order of preference. For additional information,
         including expected format, see `RFC2616
         <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>`_. This header and the setLang query
         parameter are mutually exclusive; do not specify both. If you set this header, you must also
         specify the cc query parameter. Bing will use the first supported language it finds from the
         list, and combine that language with the cc parameter value to determine the market to return
         results for. If the list does not include a supported language, Bing will find the closest
         language and market that supports the request, and may use an aggregated or default market for
         the results instead of a specified one. You should use this header and the cc query parameter
         only if you specify multiple languages; otherwise, you should use the mkt and setLang query
         parameters. A user interface string is a string that's used as a label in a user interface.
         There are very few user interface strings in the JSON response objects. Any links in the
         response objects to Bing.com properties will apply the specified language.
        :type accept_language: str
        :param pragma: By default, Bing returns cached content, if available. To prevent Bing from
         returning cached content, set the Pragma header to no-cache (for example, Pragma: no-cache).
        :type pragma: str
        :param user_agent_parameter: The user agent originating the request. Bing uses the user agent
         to provide mobile users with an optimized experience. Although optional, you are strongly
         encouraged to always specify this header. The user-agent should be the same string that any
         commonly used browser would send. For information about user agents, see `RFC 2616
         <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>`_.
        :type user_agent_parameter: str
        :param client_id: Bing uses this header to provide users with consistent behavior across Bing
         API calls. Bing often flights new features and improvements, and it uses the client ID as a key
         for assigning traffic on different flights. If you do not use the same client ID for a user
         across multiple requests, then Bing may assign the user to multiple conflicting flights. Being
         assigned to multiple conflicting flights can lead to an inconsistent user experience. For
         example, if the second request has a different flight assignment than the first, the experience
         may be unexpected. Also, Bing can use the client ID to tailor web results to that client ID’s
         search history, providing a richer experience for the user. Bing also uses this header to help
         improve result rankings by analyzing the activity generated by a client ID. The relevance
         improvements help with better quality of results delivered by Bing APIs and in turn enables
         higher click-through rates for the API consumer. IMPORTANT: Although optional, you should
         consider this header required. Persisting the client ID across multiple requests for the same
         end user and device combination enables 1) the API consumer to receive a consistent user
         experience, and 2) higher click-through rates via better quality of results from the Bing APIs.
         Each user that uses your application on the device must have a unique, Bing generated client
         ID. If you do not include this header in the request, Bing generates an ID and returns it in
         the X-MSEdge-ClientID response header. The only time that you should NOT include this header in
         a request is the first time the user uses your app on that device. Use the client ID for each
         Bing API request that your app makes for this user on the device. Persist the client ID. To
         persist the ID in a browser app, use a persistent HTTP cookie to ensure the ID is used across
         all sessions. Do not use a session cookie. For other apps such as mobile apps, use the device's
         persistent storage to persist the ID. The next time the user uses your app on that device, get
         the client ID that you persisted. Bing responses may or may not include this header. If the
         response includes this header, capture the client ID and use it for all subsequent Bing
         requests for the user on that device. If you include the X-MSEdge-ClientID, you must not
         include cookies in the request.
        :type client_id: str
        :param client_ip: The IPv4 or IPv6 address of the client device. The IP address is used to
         discover the user's location. Bing uses the location information to determine safe search
         behavior. Although optional, you are encouraged to always specify this header and the X-Search-
         Location header. Do not obfuscate the address (for example, by changing the last octet to 0).
         Obfuscating the address results in the location not being anywhere near the device's actual
         location, which may result in Bing serving erroneous results.
        :type client_ip: str
        :param location: A semicolon-delimited list of key/value pairs that describe the client's
         geographical location. Bing uses the location information to determine safe search behavior and
         to return relevant local content. Specify the key/value pair as :code:`<key>`::code:`<value>`.
         The following are the keys that you use to specify the user's location. lat (required): The
         latitude of the client's location, in degrees. The latitude must be greater than or equal to
         -90.0 and less than or equal to +90.0. Negative values indicate southern latitudes and positive
         values indicate northern latitudes. long (required): The longitude of the client's location, in
         degrees. The longitude must be greater than or equal to -180.0 and less than or equal to
         +180.0. Negative values indicate western longitudes and positive values indicate eastern
         longitudes. re (required): The radius, in meters, which specifies the horizontal accuracy of
         the coordinates. Pass the value returned by the device's location service. Typical values might
         be 22m for GPS/Wi-Fi, 380m for cell tower triangulation, and 18,000m for reverse IP lookup. ts
         (optional): The UTC UNIX timestamp of when the client was at the location. (The UNIX timestamp
         is the number of seconds since January 1, 1970.) head (optional): The client's relative heading
         or direction of travel. Specify the direction of travel as degrees from 0 through 360, counting
         clockwise relative to true north. Specify this key only if the sp key is nonzero. sp
         (optional): The horizontal velocity (speed), in meters per second, that the client device is
         traveling. alt (optional): The altitude of the client device, in meters. are (optional): The
         radius, in meters, that specifies the vertical accuracy of the coordinates. Specify this key
         only if you specify the alt key. Although many of the keys are optional, the more information
         that you provide, the more accurate the location results are. Although optional, you are
         encouraged to always specify the user's geographical location. Providing the location is
         especially important if the client's IP address does not accurately reflect the user's physical
         location (for example, if the client uses VPN). For optimal results, you should include this
         header and the  X-Search-ClientIP header, but at a minimum, you should include this header.
        :type location: str
        :param action_type: A string that's used by logging to determine whether the request is coming
         from an interactive session or a page load. The following are the possible values. 1) Edit—The
         request is from an interactive session 2) Load—The request is from a page load.
        :type action_type: str or ~spell_check_client.models.ActionType
        :param app_name: The unique name of your app. The name must be known by Bing. Do not include
         this parameter unless you have previously contacted Bing to get a unique app name. To get a
         unique name, contact your Bing Business Development manager.
        :type app_name: str
        :param country_code: A 2-character country code of the country where the results come from.
         This API supports only the United States market. If you specify this query parameter, it must
         be set to us. If you set this parameter, you must also specify the Accept-Language header. Bing
         uses the first supported language it finds from the languages list, and combine that language
         with the country code that you specify to determine the market to return results for. If the
         languages list does not include a supported language, Bing finds the closest language and
         market that supports the request, or it may use an aggregated or default market for the results
         instead of a specified one. You should use this query parameter and the Accept-Language query
         parameter only if you specify multiple languages; otherwise, you should use the mkt and setLang
         query parameters. This parameter and the mkt query parameter are mutually exclusive—do not
         specify both.
        :type country_code: str
        :param client_machine_name: A unique name of the device that the request is being made from.
         Generate a unique value for each device (the value is unimportant). The service uses the ID to
         help debug issues and improve the quality of corrections.
        :type client_machine_name: str
        :param doc_id: A unique ID that identifies the document that the text belongs to. Generate a
         unique value for each document (the value is unimportant). The service uses the ID to help
         debug issues and improve the quality of corrections.
        :type doc_id: str
        :param market: The market where the results come from. You are strongly encouraged to always
         specify the market, if known. Specifying the market helps Bing route the request and return an
         appropriate and optimal response. This parameter and the cc query parameter are mutually
         exclusive—do not specify both.
        :type market: str
        :param session_id: A unique ID that identifies this user session. Generate a unique value for
         each user session (the value is unimportant). The service uses the ID to help debug issues and
         improve the quality of corrections.
        :type session_id: str
        :param set_lang: The language to use for user interface strings. Specify the language using the
         ISO 639-1 2-letter language code. For example, the language code for English is EN. The default
         is EN (English). Although optional, you should always specify the language. Typically, you set
         setLang to the same language specified by mkt unless the user wants the user interface strings
         displayed in a different language. This parameter and the Accept-Language header are mutually
         exclusive—do not specify both. A user interface string is a string that's used as a label in a
         user interface. There are few user interface strings in the JSON response objects. Also, any
         links to Bing.com properties in the response objects apply the specified language.
        :type set_lang: str
        :param user_id: A unique ID that identifies the user. Generate a unique value for each user
         (the value is unimportant). The service uses the ID to help debug issues and improve the
         quality of corrections.
        :type user_id: str
        :param mode: The type of spelling and grammar checks to perform. The following are the possible
         values (the values are case insensitive). The default is Proof. 1) Proof—Finds most spelling
         and grammar mistakes. 2) Spell—Finds most spelling mistakes but does not find some of the
         grammar errors that Proof catches (for example, capitalization and repeated words).
        :type mode: str or ~spell_check_client.models.Mode
        :param pre_context_text: A string that gives context to the text string. For example, the text
         string petal is valid. However, if you set preContextText to bike, the context changes and the
         text string becomes not valid. In this case, the API suggests that you change petal to pedal
         (as in bike pedal). This text is not checked for grammar or spelling errors. The combined
         length of the text string, preContextText string, and postContextText string may not exceed
         10,000 characters. You may specify this parameter in the query string of a GET request or in
         the body of a POST request.
        :type pre_context_text: str
        :param post_context_text: A string that gives context to the text string. For example, the text
         string read is valid. However, if you set postContextText to carpet, the context changes and
         the text string becomes not valid. In this case, the API suggests that you change read to red
         (as in red carpet). This text is not checked for grammar or spelling errors. The combined
         length of the text string, preContextText string, and postContextText string may not exceed
         10,000 characters. You may specify this parameter in the query string of a GET request or in
         the body of a POST request.
        :type post_context_text: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SpellCheck, or the result of cls(response)
        :rtype: ~spell_check_client.models.SpellCheck
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SpellCheck"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.spell_checker.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if action_type is not None:
            query_parameters['ActionType'] = self._serialize.query("action_type", action_type, 'str')
        if app_name is not None:
            query_parameters['AppName'] = self._serialize.query("app_name", app_name, 'str')
        if country_code is not None:
            query_parameters['cc'] = self._serialize.query("country_code", country_code, 'str')
        if client_machine_name is not None:
            query_parameters['ClientMachineName'] = self._serialize.query("client_machine_name", client_machine_name, 'str')
        if doc_id is not None:
            query_parameters['DocId'] = self._serialize.query("doc_id", doc_id, 'str')
        if market is not None:
            query_parameters['mkt'] = self._serialize.query("market", market, 'str')
        if session_id is not None:
            query_parameters['SessionId'] = self._serialize.query("session_id", session_id, 'str')
        if set_lang is not None:
            query_parameters['SetLang'] = self._serialize.query("set_lang", set_lang, 'str')
        if user_id is not None:
            query_parameters['UserId'] = self._serialize.query("user_id", user_id, 'str')
        if mode is not None:
            query_parameters['Mode'] = self._serialize.query("mode", mode, 'str')
        if pre_context_text is not None:
            query_parameters['PreContextText'] = self._serialize.query("pre_context_text", pre_context_text, 'str')
        if post_context_text is not None:
            query_parameters['PostContextText'] = self._serialize.query("post_context_text", post_context_text, 'str')
        query_parameters['Text'] = self._serialize.query("text", text, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['X-BingApis-SDK'] = self._serialize.header("x_bing_apis_sdk", x_bing_apis_sdk, 'str')
        if accept is not None:
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        if accept_language is not None:
            header_parameters['Accept-Language'] = self._serialize.header("accept_language", accept_language, 'str')
        if pragma is not None:
            header_parameters['Pragma'] = self._serialize.header("pragma", pragma, 'str')
        if user_agent_parameter is not None:
            header_parameters['User-Agent'] = self._serialize.header("user_agent_parameter", user_agent_parameter, 'str')
        if client_id is not None:
            header_parameters['X-MSEdge-ClientID'] = self._serialize.header("client_id", client_id, 'str')
        if client_ip is not None:
            header_parameters['X-MSEdge-ClientIP'] = self._serialize.header("client_ip", client_ip, 'str')
        if location is not None:
            header_parameters['X-Search-Location'] = self._serialize.header("location", location, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SpellCheck', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    spell_checker.metadata = {'url': '/spellcheck'}  # type: ignore
