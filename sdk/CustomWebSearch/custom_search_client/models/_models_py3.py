# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6320, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._custom_search_client_enums import *


class ResponseBase(msrest.serialization.Model):
    """ResponseBase.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: Identifiable.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'Identifiable': 'Identifiable'}
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResponseBase, self).__init__(**kwargs)
        self.type = None  # type: Optional[str]


class Identifiable(ResponseBase):
    """Defines the identity of a resource.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: Response.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    """

    _validation = {
        'type': {'required': True},
        'id': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'Response': 'Response'}
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Identifiable, self).__init__(**kwargs)
        self.type = 'Identifiable'  # type: str
        self.id = None


class Response(Identifiable):
    """Defines a response. All schemas that could be returned at the root of a response should inherit from this.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: Answer, ErrorResponse, SearchResponse, Thing.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    """

    _validation = {
        'type': {'required': True},
        'id': {'readonly': True},
        'web_search_url': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'Answer': 'Answer', 'ErrorResponse': 'ErrorResponse', 'SearchResponse': 'SearchResponse', 'Thing': 'Thing'}
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Response, self).__init__(**kwargs)
        self.type = 'Response'  # type: str
        self.web_search_url = None


class Answer(Response):
    """Answer.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: SearchResultsAnswer.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar follow_up_queries:
    :vartype follow_up_queries: list[~custom_search_client.models.Query]
    """

    _validation = {
        'type': {'required': True},
        'id': {'readonly': True},
        'web_search_url': {'readonly': True},
        'follow_up_queries': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'follow_up_queries': {'key': 'followUpQueries', 'type': '[Query]'},
    }

    _subtype_map = {
        'type': {'SearchResultsAnswer': 'SearchResultsAnswer'}
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Answer, self).__init__(**kwargs)
        self.type = 'Answer'  # type: str
        self.follow_up_queries = None


class Thing(Response):
    """Thing.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: CreativeWork.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar name: The name of the thing represented by this object.
    :vartype name: str
    :ivar url: The URL to get more information about the thing represented by this object.
    :vartype url: str
    :ivar description: A short description of the item.
    :vartype description: str
    :ivar bing_id: An ID that uniquely identifies this item.
    :vartype bing_id: str
    """

    _validation = {
        'type': {'required': True},
        'id': {'readonly': True},
        'web_search_url': {'readonly': True},
        'name': {'readonly': True},
        'url': {'readonly': True},
        'description': {'readonly': True},
        'bing_id': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'bing_id': {'key': 'bingId', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'CreativeWork': 'CreativeWork'}
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Thing, self).__init__(**kwargs)
        self.type = 'Thing'  # type: str
        self.name = None
        self.url = None
        self.description = None
        self.bing_id = None


class CreativeWork(Thing):
    """CreativeWork.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: WebPage.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :param type: Required. Constant filled by server.
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar name: The name of the thing represented by this object.
    :vartype name: str
    :ivar url: The URL to get more information about the thing represented by this object.
    :vartype url: str
    :ivar description: A short description of the item.
    :vartype description: str
    :ivar bing_id: An ID that uniquely identifies this item.
    :vartype bing_id: str
    :ivar thumbnail_url: The URL to a thumbnail of the item.
    :vartype thumbnail_url: str
    :ivar provider: The source of the creative work.
    :vartype provider: list[~custom_search_client.models.Thing]
    :ivar text:
    :vartype text: str
    """

    _validation = {
        'type': {'required': True},
        'id': {'readonly': True},
        'type': {'required': True},
        'id': {'readonly': True},
        'web_search_url': {'readonly': True},
        'name': {'readonly': True},
        'url': {'readonly': True},
        'description': {'readonly': True},
        'bing_id': {'readonly': True},
        'thumbnail_url': {'readonly': True},
        'provider': {'readonly': True},
        'text': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'bing_id': {'key': 'bingId', 'type': 'str'},
        'thumbnail_url': {'key': 'thumbnailUrl', 'type': 'str'},
        'provider': {'key': 'provider', 'type': '[Thing]'},
        'text': {'key': 'text', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'WebPage': 'WebPage'}
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CreativeWork, self).__init__(**kwargs)
        self.type = 'CreativeWork'  # type: str
        self.type = 'CreativeWork'  # type: str
        self.thumbnail_url = None
        self.provider = None
        self.text = None


class Error(msrest.serialization.Model):
    """Defines the error that occurred.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. The error code that identifies the category of error. Possible values
     include: "None", "ServerError", "InvalidRequest", "RateLimitExceeded", "InvalidAuthorization",
     "InsufficientAuthorization". Default value: "None".
    :type code: str or ~custom_search_client.models.ErrorCode
    :ivar sub_code: The error code that further helps to identify the error. Possible values
     include: "UnexpectedError", "ResourceError", "NotImplemented", "ParameterMissing",
     "ParameterInvalidValue", "HttpNotAllowed", "Blocked", "AuthorizationMissing",
     "AuthorizationRedundancy", "AuthorizationDisabled", "AuthorizationExpired".
    :vartype sub_code: str or ~custom_search_client.models.ErrorSubCode
    :param message: Required. A description of the error.
    :type message: str
    :ivar more_details: A description that provides additional information about the error.
    :vartype more_details: str
    :ivar parameter: The parameter in the request that caused the error.
    :vartype parameter: str
    :ivar value: The parameter's value in the request that was not valid.
    :vartype value: str
    """

    _validation = {
        'code': {'required': True},
        'sub_code': {'readonly': True},
        'message': {'required': True},
        'more_details': {'readonly': True},
        'parameter': {'readonly': True},
        'value': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'sub_code': {'key': 'subCode', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'more_details': {'key': 'moreDetails', 'type': 'str'},
        'parameter': {'key': 'parameter', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Union[str, "ErrorCode"] = "None",
        message: str,
        **kwargs
    ):
        super(Error, self).__init__(**kwargs)
        self.code = code
        self.sub_code = None
        self.message = message
        self.more_details = None
        self.parameter = None
        self.value = None


class ErrorResponse(Response):
    """The top-level response that represents a failed request.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :param errors: Required. A list of errors that describe the reasons why the request failed.
    :type errors: list[~custom_search_client.models.Error]
    """

    _validation = {
        'type': {'required': True},
        'id': {'readonly': True},
        'web_search_url': {'readonly': True},
        'errors': {'required': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'errors': {'key': 'errors', 'type': '[Error]'},
    }

    def __init__(
        self,
        *,
        errors: List["Error"],
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.type = 'ErrorResponse'  # type: str
        self.errors = errors


class Query(msrest.serialization.Model):
    """Defines a search query.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param text: Required. The query string. Use this string as the query term in a new search
     request.
    :type text: str
    :ivar display_text: The display version of the query term. This version of the query term may
     contain special characters that highlight the search term found in the query string. The string
     contains the highlighting characters only if the query enabled hit highlighting.
    :vartype display_text: str
    :ivar web_search_url: The URL that takes the user to the Bing search results page for the
     query.Only related search results include this field.
    :vartype web_search_url: str
    :ivar search_link:
    :vartype search_link: str
    """

    _validation = {
        'text': {'required': True},
        'display_text': {'readonly': True},
        'web_search_url': {'readonly': True},
        'search_link': {'readonly': True},
    }

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'},
        'display_text': {'key': 'displayText', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'search_link': {'key': 'searchLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        text: str,
        **kwargs
    ):
        super(Query, self).__init__(**kwargs)
        self.text = text
        self.display_text = None
        self.web_search_url = None
        self.search_link = None


class QueryContext(msrest.serialization.Model):
    """Defines the query context that Bing used for the request.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param original_query: Required. The query string as specified in the request.
    :type original_query: str
    :ivar altered_query: The query string used by Bing to perform the query. Bing uses the altered
     query string if the original query string contained spelling mistakes. For example, if the
     query string is "saling downwind", the altered query string will be "sailing downwind". This
     field is included only if the original query string contains a spelling mistake.
    :vartype altered_query: str
    :ivar alteration_override_query: The query string to use to force Bing to use the original
     string. For example, if the query string is "saling downwind", the override query string will
     be "+saling downwind". Remember to encode the query string which results in
     "%2Bsaling+downwind". This field is included only if the original query string contains a
     spelling mistake.
    :vartype alteration_override_query: str
    :ivar adult_intent: A Boolean value that indicates whether the specified query has adult
     intent. The value is true if the query has adult intent; otherwise, false.
    :vartype adult_intent: bool
    """

    _validation = {
        'original_query': {'required': True},
        'altered_query': {'readonly': True},
        'alteration_override_query': {'readonly': True},
        'adult_intent': {'readonly': True},
    }

    _attribute_map = {
        'original_query': {'key': 'originalQuery', 'type': 'str'},
        'altered_query': {'key': 'alteredQuery', 'type': 'str'},
        'alteration_override_query': {'key': 'alterationOverrideQuery', 'type': 'str'},
        'adult_intent': {'key': 'adultIntent', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        original_query: str,
        **kwargs
    ):
        super(QueryContext, self).__init__(**kwargs)
        self.original_query = original_query
        self.altered_query = None
        self.alteration_override_query = None
        self.adult_intent = None


class SearchResponse(Response):
    """Defines the top-level object that the response includes when the request succeeds.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar query_context: An object that contains the query string that Bing used for the request.
     This object contains the query string as entered by the user. It may also contain an altered
     query string that Bing used for the query if the query string contained a spelling mistake.
    :vartype query_context: ~custom_search_client.models.QueryContext
    :ivar web_pages: A list of webpages that are relevant to the search query.
    :vartype web_pages: ~custom_search_client.models.WebAnswer
    """

    _validation = {
        'type': {'required': True},
        'id': {'readonly': True},
        'web_search_url': {'readonly': True},
        'query_context': {'readonly': True},
        'web_pages': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'query_context': {'key': 'queryContext', 'type': 'QueryContext'},
        'web_pages': {'key': 'webPages', 'type': 'WebAnswer'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SearchResponse, self).__init__(**kwargs)
        self.type = 'SearchResponse'  # type: str
        self.query_context = None
        self.web_pages = None


class SearchResultsAnswer(Answer):
    """SearchResultsAnswer.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: WebAnswer.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar follow_up_queries:
    :vartype follow_up_queries: list[~custom_search_client.models.Query]
    :ivar query_context: Defines the query context that Bing used for the request.
    :vartype query_context: ~custom_search_client.models.QueryContext
    :ivar total_estimated_matches: The estimated number of webpages that are relevant to the query.
     Use this number along with the count and offset query parameters to page the results.
    :vartype total_estimated_matches: long
    :ivar is_family_friendly:
    :vartype is_family_friendly: bool
    """

    _validation = {
        'type': {'required': True},
        'id': {'readonly': True},
        'web_search_url': {'readonly': True},
        'follow_up_queries': {'readonly': True},
        'query_context': {'readonly': True},
        'total_estimated_matches': {'readonly': True},
        'is_family_friendly': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'follow_up_queries': {'key': 'followUpQueries', 'type': '[Query]'},
        'query_context': {'key': 'queryContext', 'type': 'QueryContext'},
        'total_estimated_matches': {'key': 'totalEstimatedMatches', 'type': 'long'},
        'is_family_friendly': {'key': 'isFamilyFriendly', 'type': 'bool'},
    }

    _subtype_map = {
        'type': {'Web/WebAnswer': 'WebAnswer'}
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SearchResultsAnswer, self).__init__(**kwargs)
        self.type = 'SearchResultsAnswer'  # type: str
        self.query_context = None
        self.total_estimated_matches = None
        self.is_family_friendly = None


class WebAnswer(SearchResultsAnswer):
    """Defines a list of relevant webpage links.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar follow_up_queries:
    :vartype follow_up_queries: list[~custom_search_client.models.Query]
    :ivar query_context: Defines the query context that Bing used for the request.
    :vartype query_context: ~custom_search_client.models.QueryContext
    :ivar total_estimated_matches: The estimated number of webpages that are relevant to the query.
     Use this number along with the count and offset query parameters to page the results.
    :vartype total_estimated_matches: long
    :ivar is_family_friendly:
    :vartype is_family_friendly: bool
    :param value: Required. A list of webpages that are relevant to the query.
    :type value: list[~custom_search_client.models.WebPage]
    :ivar some_results_removed: A Boolean value that indicates whether the response excluded some
     results from the answer. If Bing excluded some results, the value is true.
    :vartype some_results_removed: bool
    """

    _validation = {
        'type': {'required': True},
        'id': {'readonly': True},
        'web_search_url': {'readonly': True},
        'follow_up_queries': {'readonly': True},
        'query_context': {'readonly': True},
        'total_estimated_matches': {'readonly': True},
        'is_family_friendly': {'readonly': True},
        'value': {'required': True},
        'some_results_removed': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'follow_up_queries': {'key': 'followUpQueries', 'type': '[Query]'},
        'query_context': {'key': 'queryContext', 'type': 'QueryContext'},
        'total_estimated_matches': {'key': 'totalEstimatedMatches', 'type': 'long'},
        'is_family_friendly': {'key': 'isFamilyFriendly', 'type': 'bool'},
        'value': {'key': 'value', 'type': '[WebPage]'},
        'some_results_removed': {'key': 'someResultsRemoved', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        value: List["WebPage"],
        **kwargs
    ):
        super(WebAnswer, self).__init__(**kwargs)
        self.type = 'Web/WebAnswer'  # type: str
        self.value = value
        self.some_results_removed = None


class WebMetaTag(msrest.serialization.Model):
    """Defines a webpage's metadata.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: The metadata.
    :vartype name: str
    :ivar content: The name of the metadata.
    :vartype content: str
    """

    _validation = {
        'name': {'readonly': True},
        'content': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'content': {'key': 'content', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(WebMetaTag, self).__init__(**kwargs)
        self.name = None
        self.content = None


class WebPage(CreativeWork):
    """Defines a webpage that is relevant to the query.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar name: The name of the thing represented by this object.
    :vartype name: str
    :ivar url: The URL to get more information about the thing represented by this object.
    :vartype url: str
    :ivar description: A short description of the item.
    :vartype description: str
    :ivar bing_id: An ID that uniquely identifies this item.
    :vartype bing_id: str
    :ivar thumbnail_url: The URL to a thumbnail of the item.
    :vartype thumbnail_url: str
    :ivar provider: The source of the creative work.
    :vartype provider: list[~custom_search_client.models.Thing]
    :ivar text:
    :vartype text: str
    :ivar display_url: The display URL of the webpage. The URL is meant for display purposes only
     and is not well formed.
    :vartype display_url: str
    :ivar snippet: A snippet of text from the webpage that describes its contents.
    :vartype snippet: str
    :ivar deep_links: A list of links to related content that Bing found in the website that
     contains this webpage. The Webpage object in this context includes only the name, url,
     urlPingSuffix, and snippet fields.
    :vartype deep_links: list[~custom_search_client.models.WebPage]
    :ivar date_last_crawled: The last time that Bing crawled the webpage. The date is in the form,
     YYYY-MM-DDTHH:MM:SS. For example, 2015-04-13T05:23:39.
    :vartype date_last_crawled: str
    :ivar search_tags: A list of search tags that the webpage owner specified on the webpage. The
     API returns only indexed search tags. The name field of the MetaTag object contains the indexed
     search tag. Search tags begin with search.* (for example, search.assetId). The content field
     contains the tag's value.
    :vartype search_tags: list[~custom_search_client.models.WebMetaTag]
    """

    _validation = {
        'type': {'required': True},
        'id': {'readonly': True},
        'web_search_url': {'readonly': True},
        'name': {'readonly': True},
        'url': {'readonly': True},
        'description': {'readonly': True},
        'bing_id': {'readonly': True},
        'thumbnail_url': {'readonly': True},
        'provider': {'readonly': True},
        'text': {'readonly': True},
        'display_url': {'readonly': True},
        'snippet': {'readonly': True},
        'deep_links': {'readonly': True},
        'date_last_crawled': {'readonly': True},
        'search_tags': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'bing_id': {'key': 'bingId', 'type': 'str'},
        'thumbnail_url': {'key': 'thumbnailUrl', 'type': 'str'},
        'provider': {'key': 'provider', 'type': '[Thing]'},
        'text': {'key': 'text', 'type': 'str'},
        'display_url': {'key': 'displayUrl', 'type': 'str'},
        'snippet': {'key': 'snippet', 'type': 'str'},
        'deep_links': {'key': 'deepLinks', 'type': '[WebPage]'},
        'date_last_crawled': {'key': 'dateLastCrawled', 'type': 'str'},
        'search_tags': {'key': 'searchTags', 'type': '[WebMetaTag]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(WebPage, self).__init__(**kwargs)
        self.type = 'WebPage'  # type: str
        self.display_url = None
        self.snippet = None
        self.deep_links = None
        self.date_last_crawled = None
        self.search_tags = None
