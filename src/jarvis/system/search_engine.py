from __future__ import annotations

import re
from difflib import SequenceMatcher


class SearchEngine:

    @staticmethod
    def normalize(
        text: str,
    ) -> str:

        text = text.lower()

        text = re.sub(
            r"[^a-z0-9\s]",
            " ",
            text,
        )

        text = " ".join(text.split())

        return text

    @classmethod
    def extract_tokens(
        cls,
        text: str,
    ) -> list[str]:

        text = cls.normalize(text)

        return text.split()

    @classmethod
    def acronym(
        cls,
        text: str,
    ) -> str:

        tokens = cls.extract_tokens(text)

        return "".join(token[0] for token in tokens if token)

    @classmethod
    def compressed(
        cls,
        text: str,
    ) -> str:

        return "".join(cls.extract_tokens(text))

    @classmethod
    def abbreviation(
        cls,
        text: str,
    ) -> str:

        tokens = cls.extract_tokens(text)

        if not tokens:
            return ""

        if len(tokens) == 1:
            return tokens[0]

        result = tokens[0][0]

        for token in tokens[1:]:

            if len(token) <= 4:
                result += token
            else:
                result += token[:4]

        return result

    @classmethod
    def score(
        cls,
        query: str,
        candidate: str,
    ) -> int:

        query = cls.normalize(query)
        candidate = cls.normalize(candidate)

        if not query or not candidate:
            return 0

        # Exact match
        if query == candidate:
            return 100

        # Substring
        # Token match
        tokens = cls.extract_tokens(candidate)

        if query in tokens:
            return 95

        # Substring match
        if query in candidate:
            return 90

        # Acronym
        if query == cls.acronym(candidate):
            return 85

        # Compressed
        if query in cls.compressed(candidate):
            return 80

        # Fuzzy
        ratio = SequenceMatcher(
            None,
            query,
            candidate,
        ).ratio()

        return max(50, int(ratio * 100))

    @classmethod
    def rank(
        cls,
        query: str,
        candidates: list[str],
    ) -> list[tuple[str, int]]:

        results = []

        for candidate in candidates:

            score = cls.score(
                query,
                candidate,
            )

            results.append(
            (
                candidate,
                score,
            )
        )

            results.sort(
            key=lambda item: item[1],
            reverse=True,
        )

        return results
