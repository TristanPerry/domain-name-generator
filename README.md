# Domain Name Generator (and availability checker)

A simple Python command line domain name generator which I wrote after finding quite a lot of the web-based tools lacking for my purposes, which was:

 * generate a simple 2+ word domain (based on keyword 'groups' - e.g. "smart,smarter,clever,intelligent" is a single group)
 * only look at .com.
 * don't report registered (or 'premium') domains.

This tool generates keywords based on the provided arguments and then checks if they are registered or not (and by default only outputs available ones).
 
Usage is command line:

```
$ python generatedomain.py
usage: generatedomain.py [-h] [--skip-whois] [--show-taken]
                         [--starts-with STARTS_WITH] [--ends-with ENDS_WITH]
                         --kws KWS [KWS ...]


$ python generatedomain.py --kws keyword1 keyword2 a,few,different,options
keyword1keyword2a.com is available
keyword1keyword2few.com is available
keyword1keyword2different.com is available
keyword1keyword2options.com is available


$ python generatedomain.py --show-taken --kws demo,demonstration,example,exhibit tool,software,program
demotool.com is NOT available; expiry date is 2020-09-22T18:32:37Z
demosoftware.com is NOT available; expiry date is 2020-06-11T12:43:47Z
demoprogram.com is NOT available; expiry date is 2020-01-16T20:10:59Z
demonstrationtool.com is available
demonstrationsoftware.com is NOT available; expiry date is 2020-08-02T18:16:09Z
demonstrationprogram.com is available
exampletool.com is available
examplesoftware.com is NOT available; expiry date is 2025-10-16T19:45:49Z
exampleprogram.com is NOT available; expiry date is 2021-02-15T07:21:18Z
exhibittool.com is available
exhibitsoftware.com is NOT available; expiry date is 2020-09-11T13:37:07Z
exhibitprogram.com is NOT available; expiry date is 2020-06-02T15:34:20Z

python generatedomain.py --starts-with pre --ends-with post --kws keyword1 keyword2 a,few,different,options
prekeyword1keyword2apost.com is available
prekeyword1keyword2fewpost.com is available
prekeyword1keyword2differentpost.com is available
prekeyword1keyword2optionspost.com is available
```

This tool creates all possible combinations from the provided keywords.
