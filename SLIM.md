# Music Assistant 2.9.0 slim build

Unofficial ARM64 build. Smart Fades, Sonic Analysis and Sonic Similarity are unavailable. Loudness analysis and normal playback remain enabled. Service integrations requiring upstream app credentials need independently provisioned credentials: set MASS_APP_VAR_<index> environment variables. No upstream credentials are bundled in this build. This image is not an official Music Assistant build.

Changes are pinned to the 2.9.0 application version. Test with a copy of existing data and back up the original before switching. Docker host networking and the custom player provider mount are required for the existing deployment.
