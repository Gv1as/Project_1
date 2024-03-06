# Calculate percentage change for each column grouped by country

def edu_perc(df):
    df['yr_sch_%'] = df.groupby('country')['yr_sch'].pct_change() * 100
    df['yr_sch_pri_%'] = df.groupby('country')['yr_sch_pri'].pct_change() * 100
    df['yr_sch_sec_%'] = df.groupby('country')['yr_sch_sec'].pct_change() * 100
    df['yr_sch_ter_%'] = df.groupby('country')['yr_sch_ter'].pct_change() * 100
    df['lp_%'] = df.groupby('country')['lp'].pct_change() * 100
    df['lpc_%'] = df.groupby('country')['lpc'].pct_change() * 100
    df['lsc_%'] = df.groupby('country')['lsc'].pct_change() * 100
    df['lhc_%'] = df.groupby('country')['lhc'].pct_change() * 100
    df['pop_%'] = df.groupby('country')['pop'].pct_change() * 100

    desired_columns = ['year', 'country',  
                       'lu', 'lp', 'lp_%', 'lpc', 'lpc_%', 'ls', 'lsc', 'lsc_%', 
                       'lh', 'lhc', 'lhc_%', 'yr_sch', 'yr_sch_%', 'yr_sch_pri', 'yr_sch_pri_%', 
                       'yr_sch_sec', 'yr_sch_sec_%', 'yr_sch_ter', 'yr_sch_ter_%', 'pop', 'pop_%']

    return df[desired_columns]
