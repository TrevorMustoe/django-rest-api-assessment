# Retrieve details of a single artist with associated songs

## Description
This ticket requests the implementation of a route that retrieves the details of a single artist, including the songs associated with them.\

# TM NOTES:
+ I will have to create a custom model and include the following informatation: 
 - songs
 - song count * 

 * song count will have to refer to this optional assisment here: 
  https://github.com/nashville-software-school/server-side-python-curriculum/blob/evening-cohorts/book-3-levelup/chapters/EVENTS_PER_GAME.md

## Request
- **Method:** GET
- **Path:** /artists/{artistId}
- unnecessary

## Response
- **Body**
  ```json
  {
    "id": {artistId},
    "name": "Artist Name",
    "age": 25,
    "bio": "Artist Bio",
    "song_count": 9,
    "songs": [
      {
        "id": 123,
        "title": "Song 1",
        "album": "Album 1",
        "length": 180
      },
      {
        "id": 456,
        "title": "Song 2",
        "album": "Album 2",
        "length": 240
      }
    ]
  }
  ```
