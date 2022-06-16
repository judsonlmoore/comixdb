# Tutorial https://www.youtube.com/watch?v=UaPeWyo6ejo
import json
import pypandoc


class Convert_Json():

    def __init__(self, json_fp, h1):
        self.fp = json_fp
        self.h1 = h1
        self.jdata = self.get_json()
        self.mddata = self.format_json_to_md()

    def get_json(self):
        with open(self.fp) as f:
            res = json.load(f)
        return res

    def format_json_to_md(self):
        text = f'# {self.h1}\n'
        dct = self.jdata
        for header, data in dct.items():
            if "link" not in header:
                text += f'## {header}\n'
                if len(data) >= 0:
                    for content in data:
                        if type(content) == dict:
                            for k, v in content.items():
                                text += f'**{k}**: {v}\n\n'
                            text += '\n'
                        # case of object properties as single string, not list
                        elif type(content) != dict:
                            text += f'{content}'
        return text

    def convert_dict_to_md(self, output_fn):
        with open(output_fn, 'w') as writer:
            writer.writelines(self.mddata)
        print('Dict successfully converted to md')


# # driver code - uncomment and fill out
fn = 'products.json'
title = "TITLE"
converter = Convert_Json(fn, title)

# uncomment for markdown output
converter.convert_dict_to_md(output_fn='dict-to-md.md')
