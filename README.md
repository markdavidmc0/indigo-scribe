# indigo-scribe
Indigo Scribe is a crowd-funding platform for content writers.
Each user gets remunerated in proportion with the net lines of content contributed to the 
master story.
Indie publishing tools are provided, as well as interface with publishing houses.

Indigo, also indi-co (independent collaboration)  + scribe (writer)

## Concept 1
All users collaborate on the same master document via. Google Docs 
with real-time lines added/subtracted per user through the Google Drive API.

## Concept 2 (offline mode)
Use Sparkle Share to allow users to set-up local docs that sync with the GitHub Repo.
Metrics calculated on GitHub repo using Kubernetes web app.

## Concept 3 (online mode)
Use Sparkle Share hosted in a container (persistent disk or GCS backup) to allow users 
to work on their own files in-sync with the GitHub Repo. Metrics calculated on GitHub repo
using Kubernetes web app.

## Concept 4 (online + offline mode)
Use Sparkle Share hosted in a container (persistent disk or GCS backup) to allow users 
to work on their own files in-sync with the GitHub Repo. Metrics calculated on GitHub repo
using Kubernetes web app. GitHub repo syncs to container and Desktop at the same time.

## Ideas

1) Different modes of operation:
    * Free writing - no agreed end-goal. Agreement by majority.
    * Goal-driven - agreed end goal up-front. Agreement by original author.
2) Link Indigo Scribe account to user GitHub account.