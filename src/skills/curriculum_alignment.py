from __future__ import annotations

import json
from pathlib import Path


class CurriculumAligner:
    """
    Compare the current TVET curriculum with the
    recommended curriculum roadmap.

    Matching is deterministic and alias-based.
    """

    def __init__(
        self,
        alias_map: dict[str, str]
    ):
        self.alias_map = {
            self._normalize(key): value
            for key, value in alias_map.items()
        }

    @staticmethod
    def _normalize(
        text: str
    ) -> str:

        return " ".join(
            text.strip().lower().split()
        )

    def canonicalize(
        self,
        skill: str
    ) -> str:

        normalized = self._normalize(
            skill
        )

        return self.alias_map.get(
            normalized,
            skill
        )

    def _canonical_set(
        self,
        skills: list[str]
    ) -> set[str]:

        return {
            self.canonicalize(skill)
            for skill in skills
        }

    def _area_status(
        self,
        covered_core: list[str],
        missing_core: list[str]
    ) -> str:

        if not missing_core:
            return "COVERED"

        if covered_core:
            return "PARTIAL"

        return "GAP"

    def align(
        self,
        roadmap: dict,
        curriculum: list[str]
    ) -> dict:

        curriculum_canonical = (
            self._canonical_set(
                curriculum
            )
        )

        area_results = []

        roadmap_core_skills = set()
        roadmap_prerequisite_skills = set()

        for area in roadmap.get(
            "roadmap",
            []
        ):

            core_skills = area.get(
                "skills",
                []
            )

            prerequisite_skills = area.get(
                "prerequisite_skills",
                []
            )

            roadmap_core_skills.update(
                self.canonicalize(skill)
                for skill in core_skills
            )

            roadmap_prerequisite_skills.update(
                self.canonicalize(skill)
                for skill in prerequisite_skills
            )

            covered_core = [
                skill
                for skill in core_skills
                if self.canonicalize(skill)
                in curriculum_canonical
            ]

            missing_core = [
                skill
                for skill in core_skills
                if self.canonicalize(skill)
                not in curriculum_canonical
            ]

            covered_prerequisites = [
                skill
                for skill in prerequisite_skills
                if self.canonicalize(skill)
                in curriculum_canonical
            ]

            missing_prerequisites = [
                skill
                for skill in prerequisite_skills
                if self.canonicalize(skill)
                not in curriculum_canonical
            ]

            status = self._area_status(
                covered_core,
                missing_core
            )

            area_results.append({
                "sequence": area.get(
                    "sequence"
                ),
                "phase": area.get(
                    "phase"
                ),
                "curriculum_area": area[
                    "curriculum_area"
                ],
                "priority": area.get(
                    "priority"
                ),
                "status": status,
                "covered_core_skills":
                    covered_core,
                "missing_core_skills":
                    missing_core,
                "covered_prerequisite_skills":
                    covered_prerequisites,
                "missing_prerequisite_skills":
                    missing_prerequisites,
                "prerequisite_curriculum_areas":
                    area.get(
                        "prerequisite_curriculum_areas",
                        []
                    ),
                "related_areas":
                    area.get(
                        "related_areas",
                        []
                    )
            })

        mapped_curriculum_skills = (
            roadmap_core_skills
            | roadmap_prerequisite_skills
        )

        unmapped_curriculum_skills = [
            skill
            for skill in curriculum_canonical
            if skill not in mapped_curriculum_skills
        ]

        return {
            "current_curriculum": curriculum,
            "areas": area_results,
            "unmapped_curriculum_skills":
                sorted(
                    unmapped_curriculum_skills
                ),
            "summary": {
                "curriculum_skills":
                    len(curriculum),

                "roadmap_areas":
                    len(area_results),

                "covered_areas":
                    sum(
                        area["status"] == "COVERED"
                        for area in area_results
                    ),

                "partial_areas":
                    sum(
                        area["status"] == "PARTIAL"
                        for area in area_results
                    ),

                "gap_areas":
                    sum(
                        area["status"] == "GAP"
                        for area in area_results
                    ),

                "unmapped_curriculum_skills":
                    len(
                        unmapped_curriculum_skills
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
