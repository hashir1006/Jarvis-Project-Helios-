from __future__ import annotations

from abc import ABC, abstractmethod


class Scanner(ABC):
    """Base interface for every resource scanner."""

    @abstractmethod
    def scan(self):
        """Return discovered resources."""
        raise NotImplementedError
