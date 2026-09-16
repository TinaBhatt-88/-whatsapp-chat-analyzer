import re
import pandas as pd

def preprocess(data):

    pattern = r'\[(\d{1,2}/\d{1,2}/\d{2}),\s(\d{1,2}:\d{2}:\d{2}\s(?:AM|PM))\]\s'

    parts = re.split(pattern, data)

    dates = []
    messages = []

    for i in range(1, len(parts), 3):
        date = parts[i]
        time = parts[i + 1]
        message = parts[i + 2]

        dates.append(f"{date} {time}")
        messages.append(message.strip())

    df = pd.DataFrame({
        "message_date": dates,
        "user_message": messages
    })

    df["message_date"] = pd.to_datetime(
        df["message_date"],
        format="%m/%d/%y %I:%M:%S %p"
    )

    df.rename(columns={"message_date": "date"}, inplace=True)

    users = []
    msgs = []

    for message in df["user_message"]:
        entry = re.split(r"([^:]+):\s", message, maxsplit=1)

        if len(entry) > 2:
            users.append(entry[1].strip())
            msgs.append(entry[2].strip())
        else:
            users.append("group_notification")
            msgs.append(message.strip())

    df["user"] = users
    df["message"] = msgs

    df.drop(columns=["user_message"], inplace=True)

    # Date features
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month_name()
    df["month_num"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["day_name"] = df["date"].dt.day_name()
    df["hour"] = df["date"].dt.hour
    df["minute"] = df["date"].dt.minute

    return df