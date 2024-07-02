# Finder: A Book Search Engine

Finder is a book-focused search engine built from scratch. This project includes a backend (Python Flask), database (MySQL) and frontend (HTML/CSS/Bootstrap) components.

Hosted link: [Finder](https://finder-search-engine.onrender.com/)
## Project Structure

```
.
├── create_table.py
├── db_connection.py
├── main.py
├── requirements.txt
├── search_module.py
├── server.py
├── static
│   ├── index.css
│   └── results.css
├── templates
│   ├── index.html
│   └── results.html
└── Procfile
```

### Files and Directories

- **`create_table.py`**: Script to create the database table.
- **`db_connection.py`**: Manages the MySQL database connection logic.
- **`main.py`**: Run to crawl and index webpages and insert data into the table.
- **`Procfile`**: Used by platforms like Render or Heroku to declare the commands that helps to run the application.
- **`requirements.txt`**: Lists the dependencies needed for this project.
- **`search_module.py`**: Contains the logic for the searching and ranking the webpages.
- **`server.py`**: Sets up the Flask server for handling requests.
- **`templates`**: Contains the HTML files for the frontend.
  - **`index.html`**: The landing page for the search interface.
  - **`results.html`**: Displays the search results.
- **`static`**: Contains the CSS files for styling the frontend.
  - **`index.css`**: Styles for the landing page.
  - **`results.css`**: Styles for the results page.

## Project Overview

Finder is a search engine specifically focused on books. Users can search for books and view results through a simple web interface. 

### Backend

- **Database Handling**: Managed by `db_connection.py` and `create_table.py`.
- **Server Setup**: Managed by `server.py`.
- **Search Logic**: Implemented in `search_module.py`.

### Frontend

- **HTML Templates**: Located in the `templates` directory.
- **CSS Styles**: Located in the `static` directory.

## Deployment

This application is hosted live on [Render](https://render.com/) and can access this application on [Finder](https://finder-search-engine.onrender.com/).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Sample Screenshots

Landing page:
![Finder_landing_page](/screenshots/landing_page.png)

Results page:
![Finder_results_page](/screenshots/results_page.png)

---

Feel free to give feedback.