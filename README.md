# GitHub Release Proxy
Ever want to download a file from the **latest** release of a github project?

Longing for https://github.com/me/stuff/releases/download/LATEST/mystuff?

_Look no further!_

## Setup
1. [Create a Carina cluster](https://getcarina.com/docs/tutorials/create-connect-cluster/).
2. Run the proxy. Replace `<token>` with a GitHub personal access token and `<whitelist>`
    with a comma separated list of GitHub organizations or users that your proxy should handle.

    ```bash
    $ docker run -e GITHUB_TOKEN=<token> -e WHITELIST=<whitelist> -d -P rackerlabs/github-release-proxy
    ```
3. Run the following command to get your proxy's address and port.

    ```bash
    $ docker port $(docker ps -lq) | cut -d ' ' -f3

    104.130.0.29:32813
    ```

## Configuration
`WHITELIST` is required. It prevents accidentally acting as a proxy for
all of GitHub. It is a comma separated list of users and organizations which
are allowed to use the proxy. For example: `myuser,myorg`.

`GITHUB_TOKEN` is optional but recommended. Without it requests to GitHub will be severely rate limited.

`CACHE_TIMEOUT` is optional and defaults to 60 seconds. Specifies how long requests
to both this proxy and GitHub should be cached.

## Usage
Build URLs using the following template. Replace `<proxy>` with the value from step 3.

```
http://<proxy>/<org>/<repo>/latest/<releaseFileName>
```

For example, if your release file is located at `https://github.com/getcarina/dvm/releases/download/0.1.3/install.sh`
then the proxy url would be `https://<proxy>/getcarina/dvm/latest/install.sh`.
