# Converting the Enron Email Dataset to mbox Format

The [Enron Email Dataset](https://www.cs.cmu.edu/~./enron/) is distributed in [maildir](https://en.wikipedia.org/wiki/Maildir) format, which means that each message is stored in a separate file. This is unwieldy to work with. Here's how you can convert maildir into [mbox](https://en.wikipedia.org/wiki/Mbox), where all messages in a folder are stored in a single mbox file.

Go fetch the dataset and then unpack:

```
$ tar xvfz enron_mail_20150507.tgz
```

The dataset should unpack into a directory called `maildir`. Use the script `count_messages.sh` to gather an inventory of the messages in each folder:

```
$ ./count_messages.sh
```

Verify the total number of messages in the dataset:

```
$ ./count_messages.sh | cut -d' ' -f1 | awk '{s+=$1} END {print s}'
517401
```

Now run the conversion script:

```
$ ./convert_enron_to_mbox.py
```

It might take a bit, so go grab a cup of coffee...

After the script completes, the resulting mbox files are stored in the `enron/` directory:

```
$ ls enron | wc
    3311    3311   93804
```

The repo includes `ReadMbox.java`, a very simple Java program that uses the [JavaMail API](https://java.net/projects/javamail/pages/Home) to read the mbox files. The dependent jars are checked into the repo for convenience, so you can compile directly:

```
$ javac -cp lib/javax.mail-1.5.6.jar:lib/mbox.jar ReadMbox.java
```

You can now examine a particular mbox file:

```
$ java -cp .:lib/javax.mail-1.5.6.jar:lib/mbox.jar ReadMbox enron/enron.allen-p._sent_mail
```

The program prints out the subject line of each email.

To verify the integrity of the entire dataset in mbox format, run:

```
$ ./verify_mbox.sh > mbox.log &
```

Confirm that the number of messages is exactly the same:

```
$ cut -d' ' -f3 mbox.log | awk '{s+=$1} END {print s}'
517401
```
