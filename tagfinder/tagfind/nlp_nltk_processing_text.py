def tags(url):
    try:
        # library setup NLTK Library
        from lxml import html
        import re
        import requests
        import nltk
        import matplotlib
        import matplotlib.pyplot as plt
        from nltk import word_tokenize, sent_tokenize
        from nltk.probability import FreqDist
        from urllib import request
        from nltk.corpus import stopwords
        # Corpus Libraries Needed run once then comment out
        #nltk.download('averaged_perceptron_tagger')
        #nltk.download('punkt')
        #nltk.download('stopwords')
        #nltk.download('maxent_ne_chunker')
        #nltk.download('vader_lexicon')
        #nltk.download('wordnet')

        # "https://www.foxnews.com/politics/republicans-hunter-biden-ukraine-whisteleblower-impeachment-witness"

        test = requests.get(url)
        tree = html.fromstring(test.content)
        titlelist = tree.xpath('//title/text()')
        title = "".join(titlelist)
        if url.find("cnn.com") == -1:
            text = tree.xpath('//p/text()')
        else:
            text2 = tree.xpath('//div[@class="l-container"]')
            for x in text2:
                text = (x.xpath('//div/text()'))

        # tokenize words
        tokens = word_tokenize(" ".join(text))
        type(tokens)
        #tokenized_length = len(tokens)
        # lets remove stop=words
        # note: converting to string detokenizes the tokens, must retokenize
        sites = ["fox", "cnn", "msnbc", "news", "yahoo", "usa today", "new york times", "us weekly", "people", "share",
                "usa", "today", "us"]
        stop_words = set(stopwords.words('english'))
        tokens_stop_words_removed = [w for w in tokens if not w in stop_words]
        tokens_stop_words_removed = []
        for w in tokens:
            if w not in stop_words and w.isalpha() and w.lower() not in sites:
                tokens_stop_words_removed.append(w)
        tokens_stop_words_removed = re.sub(r'[^a-zA-Z0-9_\s]+', '', str(tokens_stop_words_removed))
        # retokenize after removing special chars
        tokens_stop_words_removed = word_tokenize(tokens_stop_words_removed)
        tokens_stop_words_removed2 = nltk.pos_tag(tokens_stop_words_removed)
        keyword = []
        for word in tokens_stop_words_removed2:
            if (word[1] == 'NNP') or word[1] == 'NN':
                keyword.append(word[0])

        fd = nltk.FreqDist(keyword)
        freq = []
        for word2, frequency in fd.most_common():
            freq.append(tuple((word2, frequency)))
        for x in range(len(freq)):
            for i in range(x):
                if freq[i][1] < freq[i + 1][1]:
                    temp = freq[i]
                    freq[i] = freq[i + 1]
                    freq[i + 1] = temp
        tags = [tuple((url, title))]
        if len(freq)>0:
            value = freq[0][1]
            x = 0
            for i in range(5):
                same = True
                while same:
                    tags.append(tuple((freq[x][0], 5 - i)))
                    if value != freq[x + 1][1]:
                        value = freq[x + 1][1]
                        same = False
                    x = x + 1
            return(tags)
    except IndexError:
        raise Exception(400)


#tags(input())
