


# My API

This is a simple API that provides access to news headlines and Olympic table data.

## Endpoints

### Hot News

- **GET** `/`
- Tags: `News`
- Parameters:
  - limit: The number of headlines to retrieve. (optional)
- Responses:
  - 200: A dictionary containing the headlines.

### Detail Journal

- **GET** `/detail`
- Tags: `News`
- Parameters:
  - link: The link to the journal article. (required)
  - journal_id: The ID of the journal. (required)
- Responses:
  - 200: A dictionary containing the journal information.

### International News

- **GET** `/international`
- Tags: `News`
- Parameters:
  - limit: The number of headlines to retrieve. (optional)
- Responses:
  - 200: A dictionary containing the headlines.

### Olympics

- **GET** `/olympics`
- Tags: `Olympics`
- Responses:
  - 200: A dictionary containing the table data.


