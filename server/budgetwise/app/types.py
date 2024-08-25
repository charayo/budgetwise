from typing import Any, Dict, List, Optional, Union, Literal

from pydantic import BaseModel, Field, ConfigDict
# from pydantic.alias_generators import to_camel
from uuid import UUID

import json


class ApiModel(BaseModel):
    model_config = ConfigDict(
        # alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
        # Need this to support output_raw or else we need
        # to manually define it as a type.
        # This generates a warning about "with no validation"
        # arbitrary_types_allowed=True
    )


# Stricter validation on incoming API requests
class ApiRequestModel(ApiModel):
    model_config = ConfigDict(
        extra="forbid",
    )

    
class ChatRequestModel(ApiRequestModel):
    message: str = Field(..., min_length=1)