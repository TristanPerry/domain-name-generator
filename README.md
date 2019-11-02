# Domain Name Generator

A simple Python command line domain name generator which I wrote after finding quite a lot of the web-based tools lacking for my purposes, which was:

 * generate a simple two word domain.
 * only look at .com.
 * don't report already registered (or 'premium') domains.
 
Usage is command line:

```
$ python generatedomain.py kw1 kw2 kw3
kw1kw2.com is available
kw1kw3.com is available
kw2kw1.com is available
kw2kw3.com is available
kw3kw1.com is available
kw3kw2.com is available
```

This tool creates all possible non-repeating combinations from the provided keywords. As per the TODOs below, I will make this tool a bit more flexible shortly.

## TODOs

 * Choose how many words can be chosen (i.e. so that 3+ word domains can be generated).
 * Allow for repeating words to be tested for availability (i.e. so that "kw1kw1.com" could be a candidate).
 * Allow for keyword variations (maybe by entering something like `python generatedomain.py tech,techno,techy kw2 kw3).