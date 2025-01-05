import pandas as pd


def getvaluecounts(df):

    return dict(df['subject'].value_counts())


def getlevelcount(df):

    return dict(list(df.groupby(['level'])['num_subscribers'].count().items())[1:])


def getsubjectsperlevel(df):

    ans = list(dict(df.groupby(['subject'])['level'].value_counts()).keys())
    alllabels = [ans[i][0]+'_'+ans[i][1] for i in range(len(ans))]
    ansvalues = list(dict(df.groupby(['subject'])[
                     'level'].value_counts()).values())

    completedict = dict(zip(alllabels, ansvalues))

    return completedict


# def yearwiseprofit(df):

#     df['price'] = df['price'].str.replace('TRUE|Free', '0')
#     df['price'] = df['price'].astype('float')
#     df['profit'] = df['price'] * df['num_subscribers']

#     # Converting the time column to year,month,day and many more

#     df['published_date'] = df['published_timestamp'].apply(
#         lambda x: x.split('T')[0])

#     # dropping of that index which has '3 hours' as time

#     df = df.drop(df.index[2066])

#     # converting the published date to pandas datetime object

#     df['published_date'] = pd.to_datetime(
#         df['published_date'], format="%Y-%m-%d")

#     df['Year'] = df['published_date'].dt.year

#     df['Month'] = df['published_date'].dt.month

#     df['Day'] = df['published_date'].dt.day

#     df['Month_name'] = df['published_date'].dt.month_name()

#     profitmap = dict(df.groupby(['Year'])['profit'].sum())

#     subscribersmap = dict(df.groupby(['Year'])['num_subscribers'].sum())

#     profitmonthwise = dict(df.groupby(['Month_name'])['profit'].sum())

#     monthwisesub = dict(df.groupby(['Month_name'])['num_subscribers'].sum())

#     return profitmap, subscribersmap,profitmonthwise,monthwisesub

def yearwiseprofit(df):
    # Replace non-numeric 'price' values with 0 and convert to float
    df['price'] = df['price'].replace(['TRUE', 'Free', 'free'], '0')  # Ensure 'free' in lowercase is also handled
    df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0)

    # Calculate profit
    df['profit'] = df['price'] * df['num_subscribers']

    # Convert published_timestamp to date
    df['published_date'] = pd.to_datetime(df['published_timestamp'].str.split('T').str[0], format="%Y-%m-%d", errors='coerce')

    # Drop the specific index (ensure it exists)
    if 2066 in df.index:
        df = df.drop(df.index[2066])

    # Extract year, month, day, and month name
    df['Year'] = df['published_date'].dt.year
    df['Month'] = df['published_date'].dt.month
    df['Day'] = df['published_date'].dt.day
    df['Month_name'] = df['published_date'].dt.month_name()

    # Group by Year and Month_name to calculate profit and subscribers
    profitmap = dict(df.groupby(['Year'])['profit'].sum())
    subscribersmap = dict(df.groupby(['Year'])['num_subscribers'].sum())
    profitmonthwise = dict(df.groupby(['Month_name'])['profit'].sum())
    monthwisesub = dict(df.groupby(['Month_name'])['num_subscribers'].sum())

    return profitmap, subscribersmap, profitmonthwise, monthwisesub

# Example usage
data = {
    'published_timestamp': ['2020-01-01T00:00:00Z', '2020-02-01T00:00:00Z', '2021-01-01T00:00:00Z', '2021-02-01T00:00:00Z'],
    'price': ['100', 'Free', '150.5', '200'],
    'num_subscribers': [10, 20, 30, 40]
}

df = pd.DataFrame(data)
result = yearwiseprofit(df)
print(result)



