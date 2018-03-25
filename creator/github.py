import base64
import requests


class GitHubError(Exception):

    def __init__(self, response):
        self.status_code = response.status_code
        self.message = response.json().get('message', 'No message provided')

    def __str__(self):
        return 'GitHub: ERROR {}'.format(self.code_message)

    @property
    def code_message(self, sep=' - '):
        return sep.join([str(self.status_code), self.message])


class GitHubCreator:
    GH_API_ENDPOINT = 'https://api.github.com'

    def __init__(self, token, session=None):
        self.token = token
        self.set_session(session)

    def set_session(self, session):
        self.session = session or requests.Session()
        self.session.auth = self._session_auth()

    def _session_auth(self):
        def github_auth(req):
            req.headers = {
                'Authorization': 'token ' + self.token,
                'User-Agent': 'Python/Labelord'
            }
            return req

        return github_auth

    def create_repository(self, owner, data):
        response = self.session.post(
            '{}/orgs/{}/repos'.format(self.GH_API_ENDPOINT, owner),
            json=data
        )
        if response.status_code != 201:
            raise GitHubError(response)
        return response

    def upload_file(self, owner, repo, path, data):
        response = self.session.put(
            '{}/repos/{}/{}/contents/{}'.format(self.GH_API_ENDPOINT, owner, repo, path),
            json=data
        )
        if response.status_code not in [200, 201]:
            raise GitHubError(response)
        return response

    @staticmethod
    def repodata(name, description, homepage, license_template):
        return {
            'name': name,
            'description': description,
            'homepage': homepage,
            'license_template': license_template
        }

    @staticmethod
    def filedata(content, message, committer, email, branch='master', encoding='utf-8'):
        return {
            'content': base64.b64encode(content.encode(encoding)).decode('ascii'),
            'message': message,
            'committer': {'name': committer, 'email': email},
            'branch': branch
        }
