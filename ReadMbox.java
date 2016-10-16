import java.io.*;
import java.util.*;
import javax.mail.*;

public class ReadMbox {

  public static void main(String[] args) throws Exception {
    Session session = Session.getDefaultInstance(new Properties());
    Store store = session.getStore(new URLName("mbox:"));
    store.connect();

    Folder inbox = store.getFolder(args[0]);
    inbox.open(Folder.READ_ONLY);
    Message[] messages = inbox.getMessages();
    System.out.println("Number of messages: " + messages.length);

    for (int i=0, n=messages.length; i<n; i++){
      System.out.println(i + ": " + messages[i].getSubject());
    }

    inbox.close(false);
    store.close();
  }
}
