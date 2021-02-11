# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6320, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, IO, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ImagesOperations:
    """ImagesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~visual_search_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def visual_search(
        self,
        x_bing_apis_sdk: Union[str, "_models.XBingApisSDK"],
        accept: Optional[str] = None,
        accept_language: Optional[str] = None,
        content_type: Optional[str] = None,
        user_agent_parameter: Optional[str] = None,
        client_id: Optional[str] = None,
        client_ip: Optional[str] = None,
        location: Optional[str] = None,
        market: Optional[str] = None,
        safe_search: Optional[Union[str, "_models.SafeSearch"]] = None,
        set_lang: Optional[str] = None,
        knowledge_request: Optional[str] = None,
        image: Optional[IO] = None,
        **kwargs
    ) -> "_models.ImageKnowledge":
        """Visual Search API lets you discover insights about an image such as visually similar images, shopping sources, and related searches. The API can also perform text recognition, identify entities (people, places, things), return other topical content for the user to explore, and more. For more information, see `Visual Search Overview <https://docs.microsoft.com/en-us/bing/bing-visual-search/overview>`_.

        Visual Search API lets you discover insights about an image such as visually similar images,
        shopping sources, and related searches. The API can also perform text recognition, identify
        entities (people, places, things), return other topical content for the user to explore, and
        more. For more information, see `Visual Search Overview <https://docs.microsoft.com/en-
        us/bing/bing-visual-search/overview>`_.

        :param x_bing_apis_sdk: Activate swagger compliance.
        :type x_bing_apis_sdk: str or ~visual_search_client.models.XBingApisSDK
        :param accept: The default media type is application/json. To specify that the response use
         `JSON-LD <http://json-ld.org/>`_\ , set the Accept header to application/ld+json.
        :type accept: str
        :param accept_language: A comma-delimited list of one or more languages to use for user
         interface strings. The list is in decreasing order of preference. For additional information,
         including expected format, see `RFC2616
         <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>`_. This header and the `setLang
         <https://docs.microsoft.com/en-us/bing/bing-visual-search/overview>`_ query parameter are
         mutually exclusive; do not specify both. If you set this header, you must also specify the `cc
         <https://docs.microsoft.com/en-us/bing/bing-visual-search/overview>`_ query parameter. To
         determine the market to return results for, Bing uses the first supported language it finds
         from the list and combines it with the cc parameter value. If the list does not include a
         supported language, Bing finds the closest language and market that supports the request or it
         uses an aggregated or default market for the results. To determine the market that Bing used,
         see the BingAPIs-Market header. Use this header and the cc query parameter only if you specify
         multiple languages. Otherwise, use the `mkt <https://docs.microsoft.com/en-us/bing/bing-visual-
         search/overview>`_ and `setLang <https://docs.microsoft.com/en-us/bing/bing-visual-
         search/overview>`_ query parameters. A user interface string is a string that's used as a label
         in a user interface. There are few user interface strings in the JSON response objects. Any
         links to Bing.com properties in the response objects apply the specified language.
        :type accept_language: str
        :param content_type: Must be set to multipart/form-data and include a boundary parameter (for
         example, multipart/form-data; boundary=:code:`<boundary string>`). For more details, see
         `Content form types <https://docs.microsoft.com/en-us/bing/bing-visual-search/overview>`_.
        :type content_type: str
        :param user_agent_parameter: The user agent originating the request. Bing uses the user agent
         to provide mobile users with an optimized experience. Although optional, you are encouraged to
         always specify this header. The user-agent should be the same string that any commonly used
         browser sends. For information about user agents, see `RFC 2616
         <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>`_. The following are examples of user-
         agent strings. Windows Phone: Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0;
         Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 822). Android: Mozilla / 5.0 (Linux; U;
         Android 2.3.5; en - us; SCH - I500 Build / GINGERBREAD) AppleWebKit / 533.1 (KHTML; like Gecko)
         Version / 4.0 Mobile Safari / 533.1. iPhone: Mozilla / 5.0 (iPhone; CPU iPhone OS 6_1 like Mac
         OS X) AppleWebKit / 536.26 (KHTML; like Gecko) Mobile / 10B142 iPhone4; 1 BingWeb /
         3.03.1428.20120423. PC: Mozilla / 5.0 (Windows NT 6.3; WOW64; Trident / 7.0; Touch; rv:11.0)
         like Gecko. iPad: Mozilla / 5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit / 537.51.1 (KHTML,
         like Gecko) Version / 7.0 Mobile / 11A465 Safari / 9537.53.
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
         requests for the user on that device. ATTENTION: You must ensure that this Client ID is not
         linkable to any authenticatable user account information. If you include the X-MSEdge-ClientID,
         you must not include cookies in the request.
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
         header and the X-MSEdge-ClientIP header, but at a minimum, you should include this header.
        :type location: str
        :param market: The market where the results come from. Typically, mkt is the country where the
         user is making the request from. However, it could be a different country if the user is not
         located in a country where Bing delivers results. The market must be in the form
         :code:`<language code>`-:code:`<country code>`. For example, en-US. The string is case
         insensitive. For a list of possible market values, see `Market Codes
         <https://docs.microsoft.com/en-us/bing/bing-visual-search/overview>`_. NOTE: If known, you are
         encouraged to always specify the market. Specifying the market helps Bing route the request and
         return an appropriate and optimal response. If you specify a market that is not listed in
         `Market Codes <https://docs.microsoft.com/en-us/bing/bing-visual-search/overview>`_\ , Bing
         uses a best fit market code based on an internal mapping that is subject to change.
        :type market: str
        :param safe_search: Filter the image results in actions with type 'VisualSearch' for adult
         content. The following are the possible filter values. Off: May return images with adult
         content. Moderate: Do not return images with adult content. Strict: Do not return images with
         adult content. The default is Moderate. If the request comes from a market that Bing's adult
         policy requires that safeSearch is set to Strict, Bing ignores the safeSearch value and uses
         Strict. If you use the site: filter in the knowledge request, there is the chance that the
         response may contain adult content regardless of what the safeSearch query parameter is set to.
         Use site: only if you are aware of the content on the site and your scenario supports the
         possibility of adult content.
        :type safe_search: str or ~visual_search_client.models.SafeSearch
        :param set_lang: The language to use for user interface strings. Specify the language using the
         ISO 639-1 2-letter language code. For example, the language code for English is EN. The default
         is EN (English). Although optional, you should always specify the language. Typically, you set
         setLang to the same language specified by mkt unless the user wants the user interface strings
         displayed in a different language. A user interface string is a string that's used as a label
         in a user interface. There are few user interface strings in the JSON response objects. Also,
         any links to Bing.com properties in the response objects apply the specified language.
        :type set_lang: str
        :param knowledge_request: The form data is a JSON object that identifies the image using an
         insights token or URL to the image. The object may also include an optional crop area that
         identifies an area of interest in the image. The insights token and URL are mutually exclusive
         – do not specify both. You may specify knowledgeRequest form data and image form data in the
         same request only if knowledgeRequest form data specifies the cropArea field only (it must not
         include an insights token or URL).
        :type knowledge_request: str
        :param image: The form data is an image binary. The Content-Disposition header's name parameter
         must be set to "image". You must specify an image binary if you do not use knowledgeRequest
         form data to specify the image; you may not use both forms to specify an image. You may specify
         knowledgeRequest form data and image form data in the same request only if knowledgeRequest
         form data specifies the cropArea field only  (it must not include an insights token or URL).
        :type image: IO
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ImageKnowledge, or the result of cls(response)
        :rtype: ~visual_search_client.models.ImageKnowledge
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ImageKnowledge"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "multipart/form-data")

        # Construct URL
        url = self.visual_search.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if market is not None:
            query_parameters['mkt'] = self._serialize.query("market", market, 'str')
        if safe_search is not None:
            query_parameters['safeSearch'] = self._serialize.query("safe_search", safe_search, 'str')
        if set_lang is not None:
            query_parameters['setLang'] = self._serialize.query("set_lang", set_lang, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['X-BingApis-SDK'] = self._serialize.header("x_bing_apis_sdk", x_bing_apis_sdk, 'str')
        if accept is not None:
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        if accept_language is not None:
            header_parameters['Accept-Language'] = self._serialize.header("accept_language", accept_language, 'str')
        if content_type is not None:
            header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        if user_agent_parameter is not None:
            header_parameters['User-Agent'] = self._serialize.header("user_agent_parameter", user_agent_parameter, 'str')
        if client_id is not None:
            header_parameters['X-MSEdge-ClientID'] = self._serialize.header("client_id", client_id, 'str')
        if client_ip is not None:
            header_parameters['X-MSEdge-ClientIP'] = self._serialize.header("client_ip", client_ip, 'str')
        if location is not None:
            header_parameters['X-Search-Location'] = self._serialize.header("location", location, 'str')
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        # Construct form data
        _form_content = {
            'knowledgeRequest': knowledge_request,
            'image': image,
        }
        request = self._client.post(url, query_parameters, header_parameters, form_content=_form_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('ImageKnowledge', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    visual_search.metadata = {'url': '/images/visualsearch'}  # type: ignore
