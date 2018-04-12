import json
from jinja2 import Environment, PackageLoader, select_autoescape

jinja_env = Environment(
    loader=PackageLoader('creator', 'template')
)

class Answer:

    def __init__(self, label, advice):
        self.label = label
        self.advice = advice

    @staticmethod
    def create(dct):
        return Answer(
            dct.get('label'),
            dct.get('advice', None)
        )


class Reference:

    def __init__(self, url, anchor):
        self.url = url
        self.anchor = anchor

    @staticmethod
    def create(dct):
        return Reference(
            dct.get('url'),
            dct.get('anchor', dct.get('url'))
        )


class Question:

    def __init__(self):
        self.title = None
        self.shortuid = None
        self.text = None
        self.type = None
        self.answers = []
        self.references = []

    @staticmethod
    def create(dct):
        q = Question()
        q.title = dct.get('title')
        q.shortuid = dct.get('shortuid')
        q.text = dct.get('text', None)
        q.type = dct.get('type')
        if q.type == 'option':
            q.answers = [Answer.create(a) for a in dct.get('answers')]
        q.references = [
            Reference.create(r) for r in dct.get('references', []) if r['type'] == 'url'
        ]
        return q


def load_from_json(json_fp):
    return [Question.create(q) for q in json.load(json_fp)]


def render(template, question, owner, reponame):
    return jinja_env.get_template(template).render(question=question,
                                                   owner=owner,
                                                   reponame=reponame)
