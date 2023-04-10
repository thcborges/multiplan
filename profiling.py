from ydata_profiling import ProfileReport

from multiplan.data import get_rent_the_runaway_data_frame


df = get_rent_the_runaway_data_frame()

profile = ProfileReport(df, title='Rent the runaway')
# profile.to_file('rent_the_runaway_profiling.json')
profile.to_file('new_rent_the_runaway_profiling.html')
