from dataclasses import dataclass, field
from typing import Any, List, Union


@dataclass
class Case:
    #     # plan on extending to include the required and then allow subclassing or mixin for extending
    #     # these: https://www.gurock.com/testrail/docs/api/reference/cases#addcase
    title: str
    id: Union[None, int] = None
    type_id: int = 7  # 7 is Other by default, see get_case_types
    priority_id: int = 1
    section_id: Union[None, int] = None
    suite_id: Union[None, int] = None
    estimate: Union[None, str] = None
    milestone_id: Union[
        None, int
    ] = None  # The ID of the milestone to link to the test case
    refs: Union[None, str] = None  # A comma-separated list of references/requirements
    template_id: Union[
        None, int
    ] = None  # The ID of the template (field layout) (requires TestRail 5.2 or later)
    created_by: Union[None, int] = None  # The ID of the user who created the test case
    created_on: Union[None, str] = None
    estimate_forecast: Union[
        None, str
    ] = None  # The estimate forecast, e.g. “30s” or “1m 45s”
    updated_by: Union[
        None, int
    ] = None  # The ID of the user who last updated the test case
    updated_on: Union[
        None, int
    ] = None  # The date/time when the test case was last updated (as UNIX timestamp)
    custom_steps_separated: Union[None, List] = None
    custom_steps: Union[None, List] = None
    display_order: Union[None, List] = None
    title: Union[None, str] = None
    is_deleted: Union[None, bool] = None
    custom_automation_type: Union[None, str] = None

@dataclass
class Section:
    suite_id: int
    depth: int = 0
    parent_id: Union[None, int] = field(default=None)
    display_order: Union[None, int] = field(default=None)
    id: Union[None, int] = field(default=None, repr=False)
    name: str = "Test Cases"
    description: str = ""


@dataclass
class Suite:
    name: str
    description: str
    project_id: int
    url: str
    is_completed: bool = None
    id: int = None
    is_baseline: bool = None
    is_master: bool = None
    completed_on: Any = None  # datetime?
    # sections: List[Section] = field(repr=False, default_factory=list)
