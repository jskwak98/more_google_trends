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
        self.n = compute(keywords)
    
    def retrieve_data(self):
        """
        get the data, api one by one
        think of ways to reflect the progress in real time
        1. writing the progress in the file shared with the server
        2. or other ways? like Event listener? If it exists
        """

    def compute_data(self):
        """
        use self.n and the 'level'
        trickle down computation of the relative frequency
        """

pytrends = TrendReq()

keywords = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']
pytrends.build_payload(keywords, timeframe='2023-06-01 2023-06-01')

data = pytrends.interest_over_time()
rel_vol = list(data.iloc[0].values[:-1])
head = keywords[rel_vol.index(100)]

print(data)