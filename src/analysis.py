def analyze_segments(df):

    summary = df.groupby("Segment").agg(
        Customers=("CustomerID", "count"),
        AverageAge=("Age", "mean"),
        AverageIncome=("AnnualIncome", "mean"),
        AverageSpending=("SpendingScore", "mean")
    )

    return summary