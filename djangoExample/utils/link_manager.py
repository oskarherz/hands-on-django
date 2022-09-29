from typing import List
from dataclasses import dataclass


class LinkManager:
    @dataclass
    class Link:
        url: str
        template_name: str
        label: str
        namespace: str = 'playground'
        active: bool = False

        @property
        def view_name(self):
            return f'{self.namespace}:{self.url}'

    links: List[Link]

    def __init__(self, links):
        self.links = links

    def get_links_for(self, template_name: str):
        for link in self.links:
            link.active = link.template_name == template_name

        return self.links