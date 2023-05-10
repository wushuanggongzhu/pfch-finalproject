# pfch-finalproject

**Project Title**

Visualizing the China Collection's Development at the MET, 1875 to 2023

**Project Description:**

Completed for the course INFO 664: Programming for Cultural Heritage in Spring 2023, this project produces a CSV with catalog information for a collection of objects at the Metropolitan Museum of Art. Three Python scripts are used:

 1.) Write a JSON file with the desired object IDs (chineseobjectIDs.py)
- Use Base URL from MET API with specific parameter conditions. In this case, I used "artistOrCulture" and "China." These fields are easily substituted    depending on your interests.
 
 2.) Create a CSV with the Object Data (objectdata.py)
- Use Base URL from MET API plugging in the object IDs captured in the previously created JSON file. This code will loop through these objects, capture the fields you request, and write them into a new CSV. If fields such as "dynansty" do not exist for your search, either delete or replace with others.
 
 3.) Created Cleaner CSV (cleanup_metcsv.py)
- In this code I created a new CSV with some small modifications aimed at formatting and tidying the data. Namely, I deleted an additional comma and space in the Artist Suffix field, copied over "Medium" data to "Classification" field when the latter was blank, and calculated an object date average in a new field based on "Earliest Date" and "Latest Date." 
 
**Instructions**

No API key is required to use the MET API. When updating the code, you may want to reference their Git: https://metmuseum.github.io/

The third script "cleanup_metcsv.py" is specific to this project and data set. You may wish to disregard based on your own data set. 

**View Visualization**

Part of the deliverables for this project is a visualization hosted on Tableau Public. View it here: https://public.tableau.com/shared/6S7Q34RWH?:display_count=n&:origin=viz_share_link

**Future States**

The data set would benefit from additional cleaning and standardization. In particular, inconsistencies in fields related to dynasty and historical data should be addressed. 


 

