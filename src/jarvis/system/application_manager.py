from __future__ import annotations

from jarvis.system.application_indexer import ApplicationIndexer
from jarvis.system.launcher import ApplicationLauncher
from jarvis.system.process_manager import ProcessManager
from jarvis.system.search import ApplicationSearch


class ApplicationManager:

    def __init__(self):

        self.searcher = ApplicationSearch()
        self.launcher = ApplicationLauncher()
        self.processes = ProcessManager()
        self.indexer = ApplicationIndexer()

    def index(self):

        return self.indexer.build()

    def search(
        self,
        query: str,
    ):

        return self.searcher.search(query)

    def open(
        self,
        query: str,
    ):

        return self.launcher.open(query)

    def is_running(
        self,
        query: str,
    ):

        return self.processes.is_running(query)

    def close(
        self,
        query: str,
    ):

        return self.processes.close(query)
