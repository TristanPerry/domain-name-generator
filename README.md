# Domain Name Generator (and availability checker)

A simple Python command line domain name generator which I wrote after finding quite a lot of the web-based tools lacking for my purposes, which was:

 * generate a simple two word domain.
 * only look at .com.
 * don't report registered (or 'premium') domains.

This tool generates keywords based on the provided arguments and then checks if they are registered or not (and currently only outputs available ones).
 
Usage is command line:

```
$ python generatedomain.py
usage: generatedomain.py [-h] [--allow-duplicates]
                         [--number-words NUMBER_WORDS] --kws KWS [KWS ...]
generatedomain.py: error: the following arguments are required: --kws

$ python generatedomain.py --allow-duplicates --number-words 2 --kws some awesome keywords
somekeywords.com is available
awesomekeywords.com is available
keywordssome.com is available
keywordsawesome.com is available

```

This tool creates all possible non-repeating combinations from the provided keywords. As per the TODOs below, I will make this tool a bit more flexible shortly.

## TODOs

 * Allow for keyword variations (probably by allowing something like `python generatedomain.py tech,techno,techy kw2 kw3` - better than trying to be smart by adding "no", "ie", "y" onto the end of keywords and usually getting it wrong).
 * An option to skip the WHOIS check.
 * An option to also output taken domains (along with their expiry date).