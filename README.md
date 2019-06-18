# indigo-scribe
Indigo Scribe is a crowd-funding platform for content writers.
Each user gets remunerated in proportion with the net lines of content contributed to the 
master story.
Indie publishing tools are provided, as well as interface with publishing houses.

Indigo, also indi-co (independent collaboration)  + scribe (writer)

## Concept 1 ** continue exploring this option (don't see this working)
All users collaborate on the same master document via. Google Docs 
with real-time lines added/subtracted per user through the Google Drive API.
- extra code is needed here to convert document changes into lines added or subtracted.
- a time history of lines added or subtracted will need to be maintained in case of
dispute.

## Concept 2 (offline mode)
Use Sparkle Share to allow users to set-up local docs that sync with the GitHub Repo.
Metrics calculated on GitHub repo using Kubernetes web app.
* problem - can't capture Lisa's diff from Sparkle input.
* Git conflict causes unexpected behavior.

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