import pandas as pd

data = pd.read_csv("pro_com_25.csv", encoding="CP1252", sep=",")



def make_prompt_and_completion(string: str):
    # get rid of whitespace in the beginning of string
    string = string.strip()

    # split the string at every "\r\n" and make a list of strings
    list_of_strings = string.split("\r\n")

    # get rid of whitespace in beginning and end, and remove
    # string if "You might also like" is in string
    list_of_strings = [
        string.strip()
        for string in list_of_strings
        if not "You might also like" in string
    ]

    # take the first two sentences and join them with "\n"
    prompt = "\n".join(list_of_strings[0:2])

    # take all other sentences except the last and join them
    # NOTE: Last sentences is "produced by ..."
    completion = "\n".join(list_of_strings[2:-1])
    return prompt, completion


# apply the function to the text column of data, and return the two columns
data["prompt"], data["completion"] = zip(
    *data["completion"].apply(make_prompt_and_completion)
)

