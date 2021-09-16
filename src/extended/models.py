from abc import abstractmethod
from dataclasses import asdict, dataclass, field
from dataclasses import dataclass, field
from typing import Any, List, Union


class TestRailBase:
    @classmethod
    def from_get(cls, raw):
        obj = cls(**raw)
        return obj

    def to_post(self):
        self.validate_request()
        return asdict(self)

    @abstractmethod
    def validate_request(self):
        pass


@dataclass
class Case(TestRailBase):
    # plan on extending to include the required and then allow subclassing or mixin for extending
    # these: https://www.gurock.com/testrail/docs/api/reference/cases#addcase
    # The estimate_forecast is a string time, e.g. “30s” or “1m 45s”
    # The template_id requires TestRail 5.2 or later
    # The type_id is 7, which is other by default.
    # created_by,updated_by is the ID of the user
    # created_on,updated_on is a UNIX timestamp
    # refs is a comma separated list of requirements, e.b. "JIRA-123,JIRA-124,JIRA-125"
    title: str

    created_by: Union[None, int] = None
    created_on: Union[None, str] = None
    estimate: Union[None, str] = None
    estimate_forecast: Union[None, str] = None
    id: Union[None, int] = None
    template_id: Union[None, int] = None
    type_id: int = 7
    priority_id: int = 1
    section_id: Union[None, int] = None
    suite_id: Union[None, int] = None
    refs: Union[None, str] = None
    updated_by: Union[None, int] = None
    updated_on: Union[None, int] = None

    custom_steps_separated: Union[None, List] = None
    custom_steps: Union[None, List] = None


@dataclass
class Section(TestRailBase):
    suite_id: int
    depth: int = 0
    parent_id: Union[None, int] = field(default=None)
    display_order: Union[None, int] = field(default=None)
    id: Union[None, int] = field(default=None, repr=False)
    name: str = "Test Cases"
    description: str = ""


@dataclass
class Suite(TestRailBase):
    name: str
    description: str
    project_id: int
    url: Union[str, None] = None
    is_completed: Union[bool, None] = None
    id: Union[int, None] = None
    is_baseline: Union[bool, None] = None
    is_master: Union[bool, None] = None
    completed_on: Union[Any, None] = None

    def to_post(self):
        self.validate_request()
        return {"name": self.name, "description": self.description}
