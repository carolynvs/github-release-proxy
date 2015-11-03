./build.sh
docker rm -vf github-release-proxy
docker run --name github-release-proxy -d -P rackerlabs/github-release-proxy
open http://$(docker port github-release-proxy | cut -d ' ' -f3)/getcarina/dvm/latest/dvm-helper-windows-amd64.exe
