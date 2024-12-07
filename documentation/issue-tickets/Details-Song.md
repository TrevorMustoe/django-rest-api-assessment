# Retrieve details of a single song with associated genres and artist details

## Description
This ticket requests the implementation of a route that retrieves the details of a single song, including its associated genres and artist details.

# TM NOTES:
+ For this I will have to create my own custom models for songs to get the info
+ Need to add to Song model the following:
  - artists
  - genres

## Request
- **Method:** GET
- **Path:** /songs/{songId}

## Response
- **Body**
  ```json
  {
    "id": {songId},
    "title": "Song Title",
    "artist": {
      "id": 456,
      "name": "Artist Name",
      "age": 30,
      "bio": "Artist Bio"
    },
    "album": "Album Name",
    "length": 180,
    "genres": [
      {
        "id": 789,
        "description": "Genre 1"
      },
      {
        "id": 123,
        "description": "Genre 2"
      }
    ]
  }
  ```
