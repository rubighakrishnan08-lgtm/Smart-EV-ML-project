def priority_score(ev):
    return (100 - ev["SoC"]) * 0.5 + ev["distance"] * 0.3 + (3 - ev["profession"]) * 0.2

def allocate(ev_df):
    ev_df["priority"] = ev_df.apply(priority_score, axis=1)
    ev_df = ev_df.sort_values(by="priority", ascending=False)
    return ev_df