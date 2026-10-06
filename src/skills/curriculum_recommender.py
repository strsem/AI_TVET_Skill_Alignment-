from __future__ import annotations

import json
from pathlib import Path


class CurriculumRecommender:
    """
    Convert curriculum gap analysis into recommended curriculum areas.

    This component is intentionally rule-based and deterministic.
    """

    NOT_DIRECT_GAP_TYPES = {
        "MODEL",
        "FRAMEWORK"
    }

    def __init__(self, recommendation_map: dict):
        self.recommendation_map = recommendation_map

    @staticmethod
    def _normalize(text: str) -> str:
        return " ".join(text.strip().lower().split())

    def _build_normalized_map(self) -> dict:
        return {
            self._normalize(skill): recommendation
            for skill, recommendation
            in self.recommendation_map.items()
        }

    @staticmethod
    def _extract_skill(item: dict) -> str | None:
        return (
            item.get("skill")
            or item.get("name")
            or item.get("skill_name")
        )

    @staticmethod
    def _get_gap_items(
        gap_report: dict,
        key: str
    ) -> list[dict]:

        aliases = {
            "high_gap": [
                "high_gap",
                "high_gaps"
            ],
            "medium_gap": [
                "medium_gap",
                "medium_gaps"
            ]
        }

        for alias in aliases.get(key, [key]):
            value = gap_report.get(alias)

            if isinstance(value, list):
                return value

        return []

    def recommend(self, gap_report: dict) -> dict:

        normalized_map = self._build_normalized_map()

        recommendations = []
        unmapped_gaps = []

        for gap_level in ["high_gap", "medium_gap"]:

            gap_items = self._get_gap_items(
                gap_report,
                gap_level
            )

            for item in gap_items:

                skill = self._extract_skill(item)

                if not skill:
                    continue

                skill_type = (
                    item.get("skill_type")
                    or item.get("type")
                    or "UNKNOWN"
                )

                if skill_type in self.NOT_DIRECT_GAP_TYPES:
                    continue

                recommendation = normalized_map.get(
                    self._normalize(skill)
                )

                if recommendation is None:

                    unmapped_gaps.append({
                        "skill": skill,
                        "gap_level": (
                            "HIGH"
                            if gap_level == "high_gap"
                            else "MEDIUM"
                        ),
                        "skill_type": skill_type
                    })

                    continue

                recommendations.append({
                    "skill": skill,
                    "gap_level": (
                        "HIGH"
                        if gap_level == "high_gap"
                        else "MEDIUM"
                    ),
                    "coverage": item.get("coverage"),
                    "job_count": item.get("job_count"),
                    "total_jobs": item.get("total_jobs"),
                    "skill_type": skill_type,
                    "curriculum_area": recommendation[
                        "curriculum_area"
                    ],
                    "recommended_topics": recommendation[
                        "recommended_topics"
                    ],
                    "reason": recommendation["reason"]
                })

        curriculum_areas = {}

        priority_rank = {
            "HIGH": 2,
            "MEDIUM": 1
        }

        for item in recommendations:

            area = item["curriculum_area"]

            if area not in curriculum_areas:

                curriculum_areas[area] = {
                    "curriculum_area": area,
                    "priority": item["gap_level"],
                    "skills": [],
                    "recommended_topics": [],
                    "reasons": []
                }

            group = curriculum_areas[area]

            if (
                priority_rank[item["gap_level"]]
                > priority_rank[group["priority"]]
            ):
                group["priority"] = item["gap_level"]

            if item["skill"] not in group["skills"]:
                group["skills"].append(item["skill"])

            for topic in item["recommended_topics"]:

                if topic not in group["recommended_topics"]:
                    group["recommended_topics"].append(topic)

            if item["reason"] not in group["reasons"]:
                group["reasons"].append(item["reason"])

        return {
            "recommendations": recommendations,
            "curriculum_areas": list(
                curriculum_areas.values()
            ),
            "unmapped_gaps": unmapped_gaps,
            "summary": {
                "recommended_skills": len(
                    recommendations
                ),
                "curriculum_areas": len(
                    curriculum_areas
                ),
                "unmapped_gaps": len(
                    unmapped_gaps
                )
            }
        }


def load_json(path: str | Path) -> dict:

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
