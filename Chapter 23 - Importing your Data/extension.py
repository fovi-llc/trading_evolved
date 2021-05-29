from zipline.data.bundles import register, random_stock_data, random_futures_data

register("random_stock_data", random_stock_data.random_stock_data, calendar_name="NYSE")

register(
    "random_futures_data",
    random_futures_data.random_futures_data,
    calendar_name="us_futures",
)
