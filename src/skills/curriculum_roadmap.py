from __future__ import annotations

import json
from pathlib import Path


AREA_ALIASES = {
    "Prompt Engineering and LLM Applications":
        "Prompt Engineering",

    "Large Language Models and LLM Applications":
        "LLM Fundamentals and Application Engineering",

    "LLM Application Engineering":
        "LLM Fundamentals and Application Engineering",

    "Retrieval-Augmented Generation":
        "RAG and Vector Search",

    "Vector Databases and Semantic Search":
        "RAG and Vector Search",

    "RAG and Vector Search":
        "RAG and Vector Search",

    "AI Infrastructure and Cloud Deployment":
        "AI Infrastructure, Deployment and Cloud",

    "AI Infrastructure and Deployment":
        "AI Infrastructure, Deployment and Cloud",

    "AI Deployment and DevOps":
        "AI Infrastructure, Deployment and Cloud"
}


AREA_PREREQUISITE_AREAS = {
    "LLM Fundamentals and Application Engineering": [],

    "Prompt Engineering": [
        "LLM Fundamentals and Application Engineering"
    ],

    "RAG and Vector Search": [
        "LLM Fundamentals and Application Engineering"
    ],

    "Agentic AI Development": [
        "LLM Fundamentals and Application Engineering"
    ],

    "AI Backend and API Development": [],

    "AI Workflow Automation": [
        "AI Backend and API Development"
    ],

    "AI Data Infrastructure": [],

    "AI Infrastructure, Deployment and Cloud": [
        "AI Backend and API Development"
    ],

    "AI Observability and Evaluation": [
        "AI Infrastructure, Deployment and Cloud"
    ]
}


AREA_PREREQUISITE_SKILLS = {
    "LLM Fundamentals and Application Engineering": [
        "Python"
    ],

    "Prompt Engineering": [],

    "RAG and Vector Search": [],

    "Agentic AI Development": [],

    "AI Backend and API Development": [
        "Python",
        "REST API"
    ],

    "AI Workflow Automation": [],

    "AI Data Infrastructure": [
        "Python",
        "REST API"
    ],

    "AI Infrastructure, Deployment and Cloud": [],

    "AI Observability and Evaluation": []
}


AREA_RELATED_AREAS = {
    "LLM Fundamentals and Application Engineering": [],

    "Prompt Engineering": [
        "LLM Fundamentals and Application Engineering"
    ],

    "RAG and Vector Search": [
        "Agentic AI Development"
    ],

    "Agentic AI Development": [
        "RAG and Vector Search"
    ],

    "AI Backend and API Development": [
        "Agentic AI Development"
    ],

    "AI Workflow Automation": [
        "Agentic AI Development"
    ],

    "AI Data Infrastructure": [
        "RAG and Vector Search",
        "Agentic AI Development"
    ],

    "AI Infrastructure, Deployment and Cloud": [],

    "AI Observability and Evaluation": [
        "Agentic AI Development"
    ]
}


class CurriculumRoadmapBuilder:
    """
    Convert curriculum recommendations into a structured roadmap.

    The roadmap distinguishes between:
    - prerequisite curriculum areas
    - prerequisite skills
    - related curriculum areas

    Sequence is generated automatically using topological sorting.
    """

    def __init__(
        self,
        area_aliases: dict | None = None,
        area_prerequisite_areas: dict | None = None,
        area_prerequisite_skills: dict | None = None,
        area_related_areas: dict | None = None
    ):
        self.area_aliases = (
            area_aliases
            or AREA_ALIASES
        )

        self.area_prerequisite_areas = (
            area_prerequisite_areas
            or AREA_PREREQUISITE_AREAS
        )

        self.area_prerequisite_skills = (
            area_prerequisite_skills
            or AREA_PREREQUISITE_SKILLS
        )

        self.area_related_areas = (
            area_related_areas
            or AREA_RELATED_AREAS
        )

    def _canonical_area(
        self,
        area: str
    ) -> str:

        return self.area_aliases.get(
            area,
            area
        )

    @staticmethod
    def _priority_rank(
        priority: str
    ) -> int:

        return {
            "HIGH": 2,
            "MEDIUM": 1
        }.get(
            priority.upper(),
            0
        )

    @staticmethod
    def _normalize_skill(
        skill: str
    ) -> str:

        return " ".join(
            skill.strip().lower().split()
        )

    def _validate_prerequisite_skills(
        self,
        area_name: str,
        area_skills: list[str]
    ) -> list[str]:

        prerequisite_skills = (
            self.area_prerequisite_skills.get(
                area_name,
                []
            )
        )

        own_skills = {
            self._normalize_skill(skill)
            for skill in area_skills
        }

        invalid_skills = [
            skill
            for skill in prerequisite_skills
            if self._normalize_skill(skill)
            in own_skills
        ]

        if invalid_skills:
            raise ValueError(
                "A skill cannot be both part of a "
                "curriculum area and a prerequisite "
                f"skill for that same area: "
                f"{area_name}: {invalid_skills}"
            )

        return list(prerequisite_skills)

    def _build_area_index(
        self,
        consolidated: dict
    ) -> dict:

        return {
            area_name: index
            for index, area_name
            in enumerate(consolidated.keys())
        }

    def _topological_sort(
        self,
        area_names: list[str],
        priorities: dict[str, str]
    ) -> list[str]:

        area_set = set(area_names)

        dependencies = {}

        for area_name in area_names:

            raw_dependencies = (
                self.area_prerequisite_areas.get(
                    area_name,
                    []
                )
            )

            dependencies[area_name] = {
                dependency
                for dependency in raw_dependencies
                if dependency in area_set
            }

        indegree = {
            area_name: len(
                dependencies[area_name]
            )
            for area_name in area_names
        }

        dependents = {
            area_name: []
            for area_name in area_names
        }

        for area_name in area_names:

            for dependency in dependencies[
                area_name
            ]:
                dependents[
                    dependency
                ].append(area_name)

        original_index = {
            area_name: index
            for index, area_name
            in enumerate(area_names)
        }

        ready = [
            area_name
            for area_name in area_names
            if indegree[area_name] == 0
        ]

        ordered = []

        while ready:

            ready.sort(
                key=lambda area_name: (
                    -self._priority_rank(
                        priorities.get(
                            area_name,
                            "MEDIUM"
                        )
                    ),
                    original_index[
                        area_name
                    ]
                )
            )

            current = ready.pop(0)

            ordered.append(current)

            for dependent in dependents[
                current
            ]:

                indegree[dependent] -= 1

                if indegree[dependent] == 0:
                    ready.append(dependent)

        if len(ordered) != len(area_names):

            raise ValueError(
                "Curriculum area dependency graph "
                "contains a cycle."
            )

        return ordered

    def _calculate_phase(
        self,
        area_name: str,
        phase_cache: dict[str, int],
        area_set: set[str]
    ) -> int:

        if area_name in phase_cache:
            return phase_cache[area_name]

        dependencies = [
            dependency
            for dependency
            in self.area_prerequisite_areas.get(
                area_name,
                []
            )
            if dependency in area_set
        ]

        if not dependencies:
            phase_cache[area_name] = 1
            return 1

        phase = 1 + max(
            self._calculate_phase(
                dependency,
                phase_cache,
                area_set
            )
            for dependency in dependencies
        )

        phase_cache[area_name] = phase

        return phase

    def build(
        self,
        recommendation_report: dict
    ) -> dict:

        consolidated = {}

        areas = recommendation_report.get(
            "curriculum_areas",
            []
        )

        for area in areas:

            original_name = area[
                "curriculum_area"
            ]

            canonical_name = (
                self._canonical_area(
                    original_name
                )
            )

            if canonical_name not in consolidated:

                consolidated[canonical_name] = {
                    "curriculum_area":
                        canonical_name,

                    "priority":
                        area.get(
                            "priority",
                            "MEDIUM"
                        ),

                    "source_areas": [],
                    "skills": [],
                    "recommended_topics": [],
                    "reasons": []
                }

            target = consolidated[
                canonical_name
            ]

            target["source_areas"].append(
                original_name
            )

            if (
                self._priority_rank(
                    area.get(
                        "priority",
                        "MEDIUM"
                    )
                )
                >
                self._priority_rank(
                    target["priority"]
                )
            ):
                target["priority"] = area[
                    "priority"
                ]

            for skill in area.get(
                "skills",
                []
            ):
                if skill not in target["skills"]:
                    target["skills"].append(
                        skill
                    )

            for topic in area.get(
                "recommended_topics",
                []
            ):
                if topic not in target[
                    "recommended_topics"
                ]:
                    target[
                        "recommended_topics"
                    ].append(topic)

            for reason in area.get(
                "reasons",
                []
            ):
                if reason not in target[
                    "reasons"
                ]:
                    target["reasons"].append(
                        reason
                    )

        area_names = list(
            consolidated.keys()
        )

        priorities = {
            area_name:
                consolidated[area_name]["priority"]
            for area_name in area_names
        }

        ordered_area_names = (
            self._topological_sort(
                area_names,
                priorities
            )
        )

        area_set = set(area_names)

        phase_cache = {}

        roadmap = []

        for sequence, area_name in enumerate(
            ordered_area_names,
            start=1
        ):

            item = consolidated[
                area_name
            ].copy()

            prerequisite_areas = [
                dependency
                for dependency
                in self.area_prerequisite_areas.get(
                    area_name,
                    []
                )
                if dependency in area_set
            ]

            prerequisite_skills = (
                self._validate_prerequisite_skills(
                    area_name,
                    item["skills"]
                )
            )

            related_areas = [
                related
                for related
                in self.area_related_areas.get(
                    area_name,
                    []
                )
                if related in area_set
            ]

            item["sequence"] = sequence

            item["phase"] = (
                self._calculate_phase(
                    area_name,
                    phase_cache,
                    area_set
                )
            )

            item[
                "prerequisite_curriculum_areas"
            ] = prerequisite_areas

            item[
                "prerequisite_skills"
            ] = prerequisite_skills

            item["related_areas"] = (
                related_areas
            )

            roadmap.append(item)

        return {
            "roadmap": roadmap,
            "summary": {
                "original_areas": len(areas),
                "consolidated_areas": len(
                    roadmap
                ),
                "high_priority_areas": sum(
                    1
                    for area in roadmap
                    if area["priority"] == "HIGH"
                ),
                "medium_priority_areas": sum(
                    1
                    for area in roadmap
                    if area["priority"] == "MEDIUM"
                )
            }
        }


def load_json(
    path: str | Path
) -> dict | list:

    path = Path(path)

    with path.open(
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_json(
    data: dict,
    path: str | Path
) -> None:

    path = Path(path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with path.open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2
        )
