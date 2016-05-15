train_df = final_df
df = pd.read_sql('select * from dbo.lineitem_sales where TripType is null order by VisitNumber, FinelineNumberID', conn)


# Run pivot_data.py

print("Make predictions on the test set")
test_probs = gbm.predict(xgb.DMatrix(eval_df))
#indices = test_probs < 0
#test_probs[indices] = 0

s1 = agg_df["VisitNumber"]
s2 = pd.DataFrame(test_probs)

s2["VisitNumber"] = s1.tolist()

cols = s2.columns.tolist()
cols = cols[-1:] + cols[:-1]
s2 = s2[cols]

s2['VisitNumber'] = s2['VisitNumber'].astype(int)

s2.to_csv("output\\base_submission.csv", index=False)