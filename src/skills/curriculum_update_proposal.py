from __future__ import annotations

import json
from pathlib import Path


class CurriculumUpdateProposer:
    """Create deterministic curriculum update proposals without an LLM."""

    def propose(self, alignment_report: dict) -> dict:
        proposals = []

        for area in alignment_report.get("areas", []):
            status = area.get("status")
            missing_core_skills = list(area.get("missing_core_skills", []))
            missing_prerequisite_skills = list(
                area.get("missing_prerequisite_skills", [])
            )

            if not missing_core_skills and not missing_prerequisite_skills:
                continue

            if missing_core_skills and missing_prerequisite_skills:
                action = "ADD_CORE_AND_PREREQUISITE_SKILLS"
            elif missing_core_skills:
                action = (
                    "EXTEND_CORE_SKILLS"
                    if status == "PARTIAL"
                    else "ADD_CORE_SKILLS"
                )
            else:
                action = "ADD_PREREQUISITE_SKILLS"

            proposals.append({
                "curriculum_area": area["curriculum_area"],
                "sequence": area.get("sequence"),
                "phase": area.get("phase"),
                "priority": area.get("priority", "MEDIUM"),
                "status": status,
                "action": action,
                "core_skills_to_add": missing_core_skills,
                "prerequisite_skills_to_add": missing_prerequisite_skills,
                "prerequisite_curriculum_areas": area.get(
                    "prerequisite_curriculum_areas", []
                ),
                "reason": self._build_reason(
                    status,
                    missing_core_skills,
                    missing_prerequisite_skills,
                ),
            })

        unmapped_review_items = [
            {
                "skill": skill,
                "action": "REVIEW_UNMAPPED_SKILL",
                "reason": (
                    "This curriculum skill is not currently mapped to "
                    "any roadmap core or prerequisite skill."
                ),
            }
            for skill in alignment_report.get("unmapped_curriculum_skills", [])
        ]

        core_count = sum(
            len(item["core_skills_to_add"]) for item in proposals
        )
        prerequisite_count = sum(
            len(item["prerequisite_skills_to_add"]) for item in proposals
        )

        return {
            "proposals": proposals,
            "unmapped_curriculum_skills": unmapped_review_items,
            "summary": {
                "area_proposals": len(proposals),
                "core_skills_to_add": core_count,
                "prerequisite_skills_to_add": prerequisite_count,
                "total_skills_to_add": core_count + prerequisite_count,
                "unmapped_review_items": len(unmapped_review_items),
            },
        }

    @staticmethod
    def _build_reason(
        status: str | None,
        missing_core_skills: list[str],
        missing_prerequisite_skills: list[str],
    ) -> str:
        if missing_core_skills and missing_prerequisite_skills:
            return (
                "The curriculum area has missing core skills and "
                "missing prerequisite skills."
            )
        if missing_core_skills:
            if status == "PARTIAL":
                return (
                    "The curriculum area is partially covered and "
                    "requires the missing core skills."
                )
            return (
                "The curriculum area is not covered and requires "
                "its missing core skills."
            )
        return "The curriculum area has missing prerequisite skills."


def load_json(path: str | Path) -> dict:
    path = Path(path)
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_json(data: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
