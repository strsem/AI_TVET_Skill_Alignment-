from abc import ABC, abstractmethod


class SkillExtractor(ABC):

    @abstractmethod
    def extract(self, job_description: str):
        raise NotImplementedError