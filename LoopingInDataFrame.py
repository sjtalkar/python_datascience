def get_recession_start():
    """Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3"""

    #  A recession is defined as starting with two consecutive quarters of GDP decline, and ending with two consecutive quarters of GDP growth.

    #     From Bureau of Economic Analysis, US Department of Commerce, the GDP over time of the United States in current dollars
    # (use the chained value in 2009 dollars), in quarterly intervals, in the file gdplev.xls.
    #     For this assignment, only look at GDP data from the first quarter of 2000 onward.
    for i, row in GDP_qtr.iterrows():

        #         print (i+2, i+ 1, i)
        #         print ( GDP_qtr.loc[i+2, 'GDP(in Billions of chained 2009)'])

        if (
            GDP_qtr.loc[i + 2, "GDP(in Billions of chained 2009)"]
            < GDP_qtr.loc[i + 1, "GDP(in Billions of chained 2009)"]
        ) & (
            GDP_qtr.loc[i + 1, "GDP(in Billions of chained 2009)"]
            < GDP_qtr.loc[i, "GDP(in Billions of chained 2009)"]
        ):
            return GDP_qtr.loc[i + 1, "YearQuarters"]

    return "No recession"


get_recession_start()


def get_recession_end():
    """Returns the year and quarter of the recession end time as a 
    string value in a format such as 2005q3"""

    recessionStart = get_recession_start()
    startIter = GDP_qtr[GDP_qtr["YearQuarters"] == recessionStart].index.item()

    # Find the index of the start of the recession and start iterating from that onwards to check rise of GDP

    for i, row in GDP_qtr.iterrows():
        if i < startIter:
            continue
        else:
            if (
                GDP_qtr.loc[i + 2, "GDP(in Billions of chained 2009)"]
                > GDP_qtr.loc[i + 1, "GDP(in Billions of chained 2009)"]
            ) & (
                GDP_qtr.loc[i + 1, "GDP(in Billions of chained 2009)"]
                > GDP_qtr.loc[i, "GDP(in Billions of chained 2009)"]
            ):
                return GDP_qtr.loc[i + 1, "YearQuarters"]

    return "No recession end"


get_recession_end()


def get_recession_bottom():
    """Returns the year and quarter of the recession bottom time as a 
    string value in a format such as 2005q3"""

    #     A recession bottom is the quarter within a recession which had the lowest GDP.

    recessionStart = get_recession_start()
    recessionEnd = get_recession_end()

    startIter = GDP_qtr[GDP_qtr["YearQuarters"] == recessionStart].index.item()
    endIter = GDP_qtr[GDP_qtr["YearQuarters"] == recessionEnd].index.item()

    # print(startIter, endIter)
    #     for i in range(startIter, endIter):
    #         print(i)

    #     GDP_recession = GDP_qtr.loc[startIter:endIter, ]

    GDP_recession = GDP_qtr.loc[
        startIter:endIter, "GDP(in Billions of chained 2009)"
    ].min()

    return GDP_recession

get_recession_bottom()

