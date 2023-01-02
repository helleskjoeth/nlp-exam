# NLP Exam

In this repository all code and data used for the pop-song generator NLP exam can be found. 

**Data folder:**

**lyrics_25** contains the 100 songs used to fine-tune the model. 25 successful pop artists were chosen with their four most popular songs at that time in December 2022.

**pro_com_25_py** contains the data in a csv format with the first two lines of each song in the "prompt" column and the rest of the song in the "completion" column. 

**pro_com_to_jsonl** is the jsonl format fed to the fine-tuning function on OpenAIs web page.

**clean_df** contains a cleaned version of our data collected from the survey.


<BR>
        
**Content:**

**lyrics_from_genius** contains the script used to scrape the 100 songs from genius

**lyrics_clean_25** contains the R markdown where the lyrics from the 100 songs are cleaned. 

**prompt_and_completion_script** contains the script used to create the two columns "prompt" and "completion", which are needed to convert to a jsonl format.

**NLP_survey_clean** contains an R Markdown with the initial cleaning of the survey data.

**nlp-exam-data-analysis** contains the code for cleaning the survey data and the data analysis. 
