# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6320, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import Action
    from ._models_py3 import AggregateOffer
    from ._models_py3 import AggregateRating
    from ._models_py3 import CreativeWork
    from ._models_py3 import CropArea
    from ._models_py3 import Error
    from ._models_py3 import ErrorResponse
    from ._models_py3 import Filters
    from ._models_py3 import Identifiable
    from ._models_py3 import ImageAction
    from ._models_py3 import ImageEntityAction
    from ._models_py3 import ImageInfo
    from ._models_py3 import ImageKnowledge
    from ._models_py3 import ImageModuleAction
    from ._models_py3 import ImageObject
    from ._models_py3 import ImageRecipesAction
    from ._models_py3 import ImageRelatedSearchesAction
    from ._models_py3 import ImageShoppingSourcesAction
    from ._models_py3 import ImageTag
    from ._models_py3 import ImageTagRegion
    from ._models_py3 import ImagesImageMetadata
    from ._models_py3 import ImagesModule
    from ._models_py3 import Intangible
    from ._models_py3 import KnowledgeRequest
    from ._models_py3 import MediaObject
    from ._models_py3 import NormalizedQuadrilateral
    from ._models_py3 import Offer
    from ._models_py3 import Organization
    from ._models_py3 import PathsPsg33EImagesVisualsearchPostRequestbodyContentMultipartFormDataSchema
    from ._models_py3 import Person
    from ._models_py3 import Point2D
    from ._models_py3 import PropertiesItem
    from ._models_py3 import Query
    from ._models_py3 import Rating
    from ._models_py3 import Recipe
    from ._models_py3 import RecipesModule
    from ._models_py3 import RelatedSearchesModule
    from ._models_py3 import Response
    from ._models_py3 import ResponseBase
    from ._models_py3 import StructuredValue
    from ._models_py3 import Thing
    from ._models_py3 import VisualSearchRequest
except (SyntaxError, ImportError):
    from ._models import Action  # type: ignore
    from ._models import AggregateOffer  # type: ignore
    from ._models import AggregateRating  # type: ignore
    from ._models import CreativeWork  # type: ignore
    from ._models import CropArea  # type: ignore
    from ._models import Error  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import Filters  # type: ignore
    from ._models import Identifiable  # type: ignore
    from ._models import ImageAction  # type: ignore
    from ._models import ImageEntityAction  # type: ignore
    from ._models import ImageInfo  # type: ignore
    from ._models import ImageKnowledge  # type: ignore
    from ._models import ImageModuleAction  # type: ignore
    from ._models import ImageObject  # type: ignore
    from ._models import ImageRecipesAction  # type: ignore
    from ._models import ImageRelatedSearchesAction  # type: ignore
    from ._models import ImageShoppingSourcesAction  # type: ignore
    from ._models import ImageTag  # type: ignore
    from ._models import ImageTagRegion  # type: ignore
    from ._models import ImagesImageMetadata  # type: ignore
    from ._models import ImagesModule  # type: ignore
    from ._models import Intangible  # type: ignore
    from ._models import KnowledgeRequest  # type: ignore
    from ._models import MediaObject  # type: ignore
    from ._models import NormalizedQuadrilateral  # type: ignore
    from ._models import Offer  # type: ignore
    from ._models import Organization  # type: ignore
    from ._models import PathsPsg33EImagesVisualsearchPostRequestbodyContentMultipartFormDataSchema  # type: ignore
    from ._models import Person  # type: ignore
    from ._models import Point2D  # type: ignore
    from ._models import PropertiesItem  # type: ignore
    from ._models import Query  # type: ignore
    from ._models import Rating  # type: ignore
    from ._models import Recipe  # type: ignore
    from ._models import RecipesModule  # type: ignore
    from ._models import RelatedSearchesModule  # type: ignore
    from ._models import Response  # type: ignore
    from ._models import ResponseBase  # type: ignore
    from ._models import StructuredValue  # type: ignore
    from ._models import Thing  # type: ignore
    from ._models import VisualSearchRequest  # type: ignore

from ._visual_search_client_enums import (
    Currency,
    ErrorCode,
    ErrorSubCode,
    ItemAvailability,
    SafeSearch,
    XBingApisSDK,
)

__all__ = [
    'Action',
    'AggregateOffer',
    'AggregateRating',
    'CreativeWork',
    'CropArea',
    'Error',
    'ErrorResponse',
    'Filters',
    'Identifiable',
    'ImageAction',
    'ImageEntityAction',
    'ImageInfo',
    'ImageKnowledge',
    'ImageModuleAction',
    'ImageObject',
    'ImageRecipesAction',
    'ImageRelatedSearchesAction',
    'ImageShoppingSourcesAction',
    'ImageTag',
    'ImageTagRegion',
    'ImagesImageMetadata',
    'ImagesModule',
    'Intangible',
    'KnowledgeRequest',
    'MediaObject',
    'NormalizedQuadrilateral',
    'Offer',
    'Organization',
    'PathsPsg33EImagesVisualsearchPostRequestbodyContentMultipartFormDataSchema',
    'Person',
    'Point2D',
    'PropertiesItem',
    'Query',
    'Rating',
    'Recipe',
    'RecipesModule',
    'RelatedSearchesModule',
    'Response',
    'ResponseBase',
    'StructuredValue',
    'Thing',
    'VisualSearchRequest',
    'Currency',
    'ErrorCode',
    'ErrorSubCode',
    'ItemAvailability',
    'SafeSearch',
    'XBingApisSDK',
]
