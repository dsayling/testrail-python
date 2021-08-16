# todo change to module imports
import time
from dataclasses import asdict, dataclass, fields
from typing import Any, List, Union

from extended.models import Case, Section, Suite
from testrail import APIClient


class TestRail(APIClient):
    # it would make a lot of sense to move these into their respective models and then have mixins to create apis,
    # this would allow you to see what the dependneices are between you and the other API calls you want o amke
    # todo, ensure all typing is done - this will only be python3 compatable.
    def __init__(self, user, password, url):
        super().__init__(user, password, url)

    def get_case(self, case_id):
        return Case(**self.send_get(f"get_case/{case_id}"))

    def get_case_types(self):
        return self.send_get("get_case_types")

    def get_priorities(self):
        return self.send_get("get_priorities")

    def get_case_fields(self):
        return self.send_get("get_case_fields")

    def get_cases(self, project_id, suite_id):
        if suite_id:
            cases = self.send_get(f"/get_cases/{project_id}&suite_id={suite_id}")
        else:
            cases = self.send_get(f"/get_cases/{project_id}")
        return [Case(**_) for _ in cases]

    def get_suite(self, suite_id):
        suite = Suite(**self.send_get(f"get_suite/{suite_id}"))
        sections = self.get_sections(suite.project_id, suite.id)
        return (
            suite,
            sections[0],
        )  # hopefully we can just have one setion for each suite for now, what is gonna be the best way to
        # eventually it would be nice to be able to setup

    def get_suites(self, project_id):
        suites = [Suite(**_) for _ in self.send_get(f"get_suites/{project_id}")]
        return suites

    def add_suite(self, name: str, description: str, project_id: int):
        suite = Suite(
            **self.send_post(
                f"/add_suite/{project_id}", {"name": name, "description": description}
            )
        )
        # next create the default section and then return the suite information
        section = self.add_section(suite.project_id, Section(suite.id))
        return suite, section

    def add_case(self, section_id: int, case: Case):
        response = self.send_post(f"/add_case/{section_id}", asdict(case))
        field_names = set(f.name for f in fields(Case))
        if response:
            return Case(**{k:v for k,v in response.items() if k in field_names})

    def add_section(self, project_id: int, section: Section):
        # new suites are created without cases or a section
        # in the UI, when you add a test case, it creates a default section called, "Test Cases"
        # so, if suites already have a section, get the sections in the suite, if the names match, just use that, otherwise, create a new one
        return Section(**self.send_post(f"/add_section/{project_id}", asdict(section)))

    def get_sections(self, project_id: int, suite_id: Union[int, None] = None):
        # suite id isn't required on projects that are operating as a "single suite"
        if suite_id:
            sections = self.send_get(f"/get_sections/{project_id}&suite_id={suite_id}")
        else:
            sections = self.send_get(f"/get_sections/{project_id}")
        return [Section(**_) for _ in sections]

    def delete_suite(self, suite_id: int):
        return self.send_post(f"/delete_suite/{suite_id}", {})

    def get_case_fields(self):
        return self.send_get("/get_case_fields")

    def update_case(self, case: Case):
        response = self.send_post(f"/update_case/{case.id}", asdict(case))
        field_names = set(f.name for f in fields(Case))
        if response:
            return Case(**{k:v for k,v in response.items() if k in field_names})
