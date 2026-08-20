package oops.librarymanagement;

public class Book {
    private int bookId;
    private String author;
    private String title;
    private int availableCopies;

    public Book(int bookId, String author, String title, int availableCopies){
        super();
        this.bookId = bookId;
        this.author = author;
        this.title = title;
        this.availableCopies = availableCopies;
    }

    public void setAuthor(String author){
        this.author = author;
    }
}
