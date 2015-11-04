docker build --tag carolynvs/github-release-proxy .
docker images -qf "dangling=true" | xargs docker rmi > /dev/null 2>&1
