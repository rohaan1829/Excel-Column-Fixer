import pandas as pd

# Load Excel file
df = pd.read_excel("data.xlsx")

# Column jisme countries hain (apna actual column name yahan likhna)
col = "Region"

# List of countries (sample, tum isko extend kar sakte ho poori world list tak)
country_list = [
    # Extra
    "Global","Asia Pacific","Senegal","Uganda","Kenya","Nigeria","Israel","Philippines","Ohio","Missouri","",

    # USA + synonyms
    "USA","United States","US","United States of America",

    # UK variants
    "UK","United Kingdom","England","Scotland","Wales","Northern Ireland","Europe",

    # Canada + Australia
    "Canada","Australia",

    # Major countries
    "Germany","France","Italy","Spain","China","India","Pakistan","Brazil","Japan","Russia","Netherlands","Africa","Middle East","UAE",

    # --- US States ---
    "Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut",
    "Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa",
    "Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan",
    "Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire",
    "New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio",
    "Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota",
    "Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia",
    "Wisconsin","Wyoming"
]

def fix_countries(text):
    if pd.isna(text):
        return text
    
    text = str(text)
    found = []
    
    # Har country check karenge
    for country in country_list:
        if country in text:
            found.append(country)
            text = text.replace(country, "")  # remove to avoid duplicates
    
    return ", ".join(found)

# Apply function to column
df[col] = df[col].apply(fix_countries)

# Save back to Excel
df.to_excel("data_fixed.xlsx", index=False)
