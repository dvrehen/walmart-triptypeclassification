# Gather some features
def build_sales_features(features, data):
    # Use some properties directly
    features.extend(['Store'])
    
    features.append('SchoolHoliday')
    data['SchoolHoliday'] = data['SchoolHoliday'].astype(float)

    for x in ['a', 'b', 'c']:
        features.append('StateHoliday_' + x)
        data['StateHoliday_' + x] = data['StateHoliday'].map(lambda y: 1 if y == x else 0)
        
    features.append('DayOfWeek')
    features.append('month')
    features.append('day')
    features.append('year')
    data['year'] = data.Date.apply(lambda x: x.split('-')[0])
    data['year'] = data['year'].astype(float)
    data['month'] = data.Date.apply(lambda x: x.split('-')[1])
    data['month'] = data['month'].astype(float)
    data['day'] = data.Date.apply(lambda x: x.split('-')[2])
    data['day'] = data['day'].astype(float)
    
    data['datetime'] = data.Date.apply(lambda x: dt.datetime(int(x.split('-')[0]),int(x.split('-')[1]),int(x.split('-')[2]),23,59,59))

