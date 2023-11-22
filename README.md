# brave-api-search-client
Brave API Python Client - Asks for input query to search results using Brave Search API

### Requirements

```
  pip install -r requirements.txt
```

### Setup

Obtain a Brave API Token from [https://api.search.brave.com/app/keys] to create on your system an environment variable named `BRAVE_TOKEN`

```
export BRAVE_TOKEN="BSAwYu-......."
```

### Usage

Run the script to start interacting with the search API 

```
python3 main.py

Enter your query:  freebsd.4
[INFO] Submitting query...

[INFO] Using api.search.brave.com v1.0
[INFO] You can find documentation at: https://api.search.brave.com/app/documentation
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
ID: 1
Title: FreeBSD version history - Wikipedia
URL: https://en.wikipedia.org/wiki/FreeBSD_version_history
Description: <strong>FreeBSD</strong> <strong>4</strong> was lauded for its stability, was a favorite operating system for ISPs and web hosting providers during the first dot-com bubble, and is widely regarded as one of the most stable and high-performance operating systems of the whole Unix lineage. Among the new features of <strong>FreeBSD</strong> <strong>4</strong>, ...

--------------------------------------------------------------------------------
```

### Results

The search results will be printed to screen as well as written to a file that the script automatically creates for you that includes the query on the file path.

```
[INFO] Results saved to: /tmp/brave-api-client-_2023_11_22-10_53-freebsd_4.1.csv
```

### Version

1.0.0    Initial Version


### Contact

[Jaziel Lopez](https://github.com/jazlopez)
