class Book {
    function getTitle() { }
    function getAuthor() { }
    function turnPage() { }
    function getCurrentPage() { }
}

class BookLocation {
    function getLocation(Book $book) { }
}

class BookRepository {
    function save(Book $book) { }
}
