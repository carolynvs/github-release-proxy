from flask import Flask, redirect
import logging
import os
import requests

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)


@app.route('/<owner>/<repo>/<version>/<path:path>')
def github_redirect(owner, repo, version, path):
	if version == 'latest':
		version = get_latest_version(owner, repo)

		if version == None:
			return "Could not find the latest release for https://github.com/{}/{}".format(owner, repo), 404

	github_url = 'https://github.com/{}/{}/releases/download/{}/{}'.format(owner, repo, version, path)

	return redirect(github_url, code=307)


def get_latest_version(owner, repo):
	latest_release_url = 'https://api.github.com/repos/{}/{}/releases/latest'.format(owner, repo)
	response = requests.get(latest_release_url, auth=build_github_auth())

	if response.status_code != 200:
		logging.debug("GitHub Request Failed with %s %s", response.status_code, response.content)
		return None

	response_json = response.json()
	return response_json['tag_name']


def build_github_auth():
	token = os.getenv('GITHUB_TOKEN')
	if not token:
		return None

	return ('', token)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
