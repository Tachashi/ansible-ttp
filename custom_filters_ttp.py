from ansible.errors import AnsibleError

try:
    from ttp import ttp
    HAS_TTP = True
except ImportError:
    HAS_TTP = False

try:
    import json
    HAS_JSON = True
except ImportError:
    HAS_JSON = False


class FilterModule(object):

    def parse_cli_ttp(self, cli_output, template_file):
        if not HAS_TTP:
            raise AnsibleError('parse_cli_ttp filter requires TTP library to be installed')

        if not HAS_JSON:
            raise AnsibleError('parse_cli_ttp filter requires JSON library to be installed')

        with open(template_file, 'rt') as ft:
            ttp_template = ft.read()

        # create parser object and parse data using template
        parser = ttp(data=cli_output, template=ttp_template)
        parser.parse()

        # return result in JSON format
        results = parser.result(format='json')[0]
        return results

    def filters(self):
        return {
            'parse_cli_ttp': self.parse_cli_ttp,
        }

