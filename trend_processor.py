from pytrends.request import TrendReq


class TrendProcessor:
    # check https://pypi.org/project/pytrends/
    def __init__(self, keywords, timeframe):
        # geo and tz is not set for initial version, consider later
        """
        keywords : list of keywords you want to get information from
        timeframe : string input to the pytrends ex) 2023-06-01, 2023-06-05
        """
        self.keywords = keywords
        self.timeframe = timeframe # it comes from the web, valid format ensured
        # need to build N, total iteration we need to go through
        self.totals = {}
        
    
    def retrieve_data(self, queries):
        """
        get the data, api one by one
        think of ways to reflect the progress in real time
        1. writing the progress in the file shared with the server
        2. or other ways? like Event listener? If it exists
        """
        pytrends = TrendReq()

        keywords = queries
        pytrends.build_payload(keywords, timeframe=self.timeframe)

        data = pytrends.interest_over_time()
        rel_vol = list(data.iloc[0].values[:-1])
        head = keywords[rel_vol.index(100)]


    def compute_data(self):
        """
        use self.n and the 'level'
        trickle down computation of the relative frequency
        """
        ## Bottleneck Bottom Up process
        self.totals = {}
        max_level = 0

        current_keywords = self.keywords
        current_level = 1

        stop_flag = False

        while not stop_flag:
            ## initialization
            queries = []
            next_keywords = []
            for i, keyword in enumerate(current_keywords):
                queries.append(keyword)
                if len(queries) % 5 == 0 or i == len(current_keywords) - 1:
                    self.retrieve_data(queries)
                    reformat_trends_and_put()
                    ## totals[current_level][100_keyword] = {'kwd' : [in order], 'dist' : [in order]}
                    # totals[current_level][100_keyword]['kwd'] = queries
                    queries = []
                    #next_keywords.append(100_keyword)
                if len(current_keywords) != 1:
                    current_level += 1
                    current_keywords = next_keywords
                else:
                    max_level = current_level
                    stop_flag = True

pytrends = TrendReq()

keywords = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']
#pytrends.build_payload(keywords, timeframe='2023-01-01 2023-06-01')

#data = pytrends.interest_over_time()

data =pytrends.get_historical_interest(keywords, year_start=2023, month_start=6, day_start=1, hour_start=0, year_end=2023, month_end=6, day_end=2, hour_end=0, cat=0, geo='', gprop='', sleep=0)
print(data)
rel_vol = list(data.iloc[0].values[:-1])
print(rel_vol)
head = keywords[rel_vol.index(100)]
print(head)

