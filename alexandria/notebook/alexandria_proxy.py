"""
   Copyright 2017 Huygens ING

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from alexandria.client.alexandria import *
from alexandria.client.resource_prototype import ResourcePrototype

from alexandria.notebook.resource_proxy import ResourceProxy


class AlexandriaProxy:
    def __init__(self, server_url, admin_key="admin"):
        self.alexandria = Alexandria(server_url, admin_key=admin_key)

    def __dir__(self):
        return ['add_text', 'get_resource', 'aql2']

    def add_text(self, path):
        uuid = self.alexandria.resources.add(ResourcePrototype(path)).uuid
        rp = ResourceProxy(path, uuid, self.alexandria)
        with open(path, 'r') as f:
            xml = f.read()
        self.alexandria.resources.set_text(uuid, xml)
        return rp

    def get_resource(self, resource_id):
        uuid = ''
        rp = ResourceProxy(resource_id, uuid, self.alexandria)
        return rp

    def aql2(self, aql2_command):
        return self.alexandria.aql2(aql2_command)

    def xpath(self, ids, xpath):
        return self.commands.xpath()
