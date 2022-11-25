# MFIN7033

Hi! Grader!

This is the collection of MFIN7033 final project. Each individual task is wrapped in a folder. Each folder contains an `.ipynb` file  and a `.py` file. Both files contain the same code, I recommend you to read and execute the `.ipynb` file since it shows output in a step-by-step way.


For the Web-scrapping projects, I initially finished the reddit and weather, but forgot to register the googlesheet. So I chose the ScienceDirect website and Hong Kong SFC website.

- The ScienceDirect

This code is to get the list of published articles from journals of ScienceDirect. I take the Journal of Financial Economics as the example. This code can be applied to all the journals released by ScienceDirect.

You can input the list volumes and issues you want to crawl, then the code will feedback a `.csv` file contains the authors, titles, and urls to the article.

- SFC unlisted funds

This code is a part of my own project. It crawl all the issued unlisted fund products(mutual funds & unit trusts) on SFC website, and get all the available **KEY FACTS STATEMENT**s. Please note that you need to change your selenium chrome download dir manually to download the statement `.pdf` files. This code is supposed to provide a `.csv` file contains all the information about unlisted funds and a folder contains all the all the available **KEY FACTS STATEMENT**s. However, to save your disk space, I restricted the crawling of **KEY FACTS STATEMENT**s to only several files.



For the Gephi project, I analyzed the passengers in-and-out of USA airports and draw a directed graph to show the relationship between different airports.





For any question related to my code. You can contact me by email(yanjinn@connect.hku.hk, respond in <2hrs, recommended) or mobile (5481 7172, I may turn-off the ring sometimes). 

