import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to classify F&B
def classify_fnb(soup):
    full_text = soup.get_text().lower()
    return any(term in full_text for term in ["beverage", "cereal", "milk", "fortified", "fortification"])

# Function to classify Brands
def classify_brand(soup):
    full_text = soup.get_text().lower()
    has_products = "product" in full_text or "price" in full_text
    mentions_health_segments = any(
        term in full_text for term in ["oral suspension", "capsule", "tablet", "sachet", "women's health", "gut health", "cognitive health"]
    )
    return has_products or mentions_health_segments

# Function to classify Manufacturers
def classify_manufacturer(soup):
    full_text = soup.get_text().lower()
    mentions_plant = "production capacity" in full_text or "plant" in full_text
    mentions_certifications = "certification" in full_text or "quality" in full_text
    mentions_dosage_forms = any(
        term in full_text for term in ["oral suspension", "capsule", "tablet", "sachet"]
    )
    return mentions_plant or mentions_certifications or mentions_dosage_forms

# Function to classify Distributors
def classify_distributor(soup):
    full_text = soup.get_text().lower()
    sells_raw_materials = "raw materials" in full_text or "supply chain" in full_text
    into_nutraceuticals_probiotics = "nutraceuticals" in full_text or "probiotics" in full_text
    irrelevant_materials = any(
        term in full_text for term in ["herbal extracts", "algae", "chemical excipients"]
    )
    return sells_raw_materials and into_nutraceuticals_probiotics and not irrelevant_materials

# Function to classify probiotics and health segments
def classify_health_segments(full_text):
    return {
        "Probiotics": "Yes" if "probiotic" in full_text else "No",
        "Fortification": "Yes" if "fortified" in full_text or "fortification" in full_text else "No",
        "Gut Health": "Yes" if "gut health" in full_text else "No",
        "Women's Health": "Yes" if "women's health" in full_text else "No",
        "Cognitive Health": "Yes" if "cognitive health" in full_text else "No"
    }

# Function to classify the website
def classify_website(url):
    try:
        # Send a GET request
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        full_text = soup.get_text().lower()

        # Initialize classification results
        classification = {
            "Manufacturer": classify_manufacturer(soup),
            "Brand": classify_brand(soup),
            "Distributor": classify_distributor(soup),
            "F&B": classify_fnb(soup)
        }

        # Add health segment classifications
        health_segments = classify_health_segments(full_text)
        classification.update(health_segments)

        return classification

    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return None

# List	
# Company Name	Website
# Nestle 	 https://https://www.nestle.com
# Dr. Reddy's Laboratories 	 https://https://www.drreddys.com
# Coca	colacompany.com
# Pfizer 	 https://https://www.pfizer.com
# PepsiCo 	 https://https://www.pepsico.com
# Johnson & Johnson 	 https://https://www.jnj.com
# Danone 	 https://https://www.danone.com
# Bayer 	 https://www.bayer.com
# General Mills 	 https://www.generalmills.com
# GlaxoSmithKline (GSK) 	 https://www.gsk.com
# Kellogg’s 	 https://www.kelloggs.com
# Merck & Co. 	 https://www.merck.com
# Unilever 	 https://www.unilever.com
# Roche 	 https://www.roche.com
# Nestle Waters 	 https://www.nestlewaters.com
# Sanofi 	 https://www.sanofi.com
# Mondelez International 	 https://www.mondelezinternational.com
# Novartis 	 https://www.novartis.com
# Kraft Heinz 	 https://www.kraftheinzcompany.com
# Eli Lilly and Company 	 https://www.lilly.com
# Tyson Foods 	 https://www.tysonfoods.com
# Teva Pharmaceuticals 	 https://www.tevapharm.com
# Mars, Incorporated 	 https://www.mars.com
# AbbVie 	 https://www.abbvie.com
# Campbell Soup Company 	 https://www.campbellsoupcompany.com
# Amgen 	 https://www.amgen.com
# Conagra Brands 	 https://www.conagrabrands.com
# AstraZeneca 	 https://www.astrazeneca.com
# Molson Coors 	 https://www.molsoncoors.com
# Boehringer Ingelheim 	 https://www.boehringeringelheim.com
# AB InBev 	 https://www.abinbev.com
# BASF 	 https://www.basf.com
# Diageo 	 https://www.diageo.com
# Procter & Gamble (P&G) 	 https://www.pg.com
# Heineken 	 https://www.theheinekencompany.com
# Medtronic 	 https://www.medtronic.com
# McKesson 	 https://www.mckesson.com
# AmerisourceBergen 	 https://www.amerisourcebergen.com
# Cardinal Health 	 https://www.cardinalhealth.com
# Medline Industries 	 https://www.medline.com
companies = [
    {"Company": "Nestle", "Website": "https://www.nestle.com"},
    {"Company": "Pfizer", "Website": "https://www.pfizer.com"},
    {"Company": "Coca Cola", "Website": "https://www.coca-colacompany.com"},
    {"Company":"Dr. Reddy's Laboratories","Website":"https://www.drreddys.com"},
    {"Company":"PepsiCo","Website":"https://www.pepsico.com"},
    {"Company":"Johnson & Johnson","Website":"https://www.jnj.com"},
    {"Company":"Danone","Website":"https://www.danone.com"},
    {"Company":"Bayer ","Website":"https://www.bayer.com"},
    {"Company":"General Mills","Website":"https://www.generalmills.com"},
    {"Company":"GlaxoSmithKline (GSK)","Website":"https://www.gsk.com"},
    {"Company":"Kellogg’s","Website":" https://www.kelloggs.com"},
    {"Company":"Merck & Co.","Website":"https://www.merck.com"},	 
    {"Company":"Unilever ","Website":"https://www.unilever.com"},
    {"Company":"Roche","Website":"https://www.roche.com"},
    {"Company":"Nestle Waters","Website":"https://www.nestlewaters.com"},
    {"Company":"Sanofi","Website":"https://www.sanofi.com"},
    {"Company":"Mondelez International","Website":"https://www.mondelezinternational.com"},
    {"Company":"Novartis","Website":"https://www.novartis.com"},
    {"Company":"Kraft Heinz","Website":"https://www.kraftheinzcompany.com"},
    {"Company":"Eli Lilly and Company","Website":" https://www.lilly.com"},
    {"Company":"Tyson Foods","Website":"https://www.tysonfoods.com"},
    {"Company":"Teva Pharmaceuticals","Website":"https://www.tevapharm.com"},
    {"Company":"Mars, Incorporated","Website":"https://www.mars.com"},
    {"Company":"AbbVie","Website":"https://www.abbvie.com"},
    {"Company":"Campbell Soup Company","Website":"https://www.campbellsoupcompany.com"},
    {"Company":"Amgen","Website":"https://www.amgen.com"},
    {"Company":"Conagra Brands","Website":"https://www.conagrabrands.com"},
    {"Company":"AstraZeneca","Website":"https://www.astrazeneca.com"},
    {"Company":"Molson Coors","Website":"https://www.molsoncoors.com"},
    {"Company":"Boehringer Ingelheim","Website":"https://www.boehringeringelheim.com"},
    {"Company":"AB InBev","Website":"https://www.abinbev.com"},
    {"Company":"BASF","Website":"https://www.basf.com"},   
    {"Company":"Diageo","Website":"https://www.diageo.com"},
    {"Company":"Procter & Gamble (P&G)","Website":"https://www.pg.com"},
    {"Company":"Heineken","Website":"https://www.theheinekencompany.com"},
    {"Company":"Medtronic","Website":"https://www.medtronic.com"},
    {"Company":"McKesson","Website":"https://www.mckesson.com"},
    {"Company":"AmerisourceBergen","Website":"https://www.amerisourcebergen.com"},
    {"Company":"Cardinal Health","Website":"https://www.cardinalhealth.com"},
    {"Company":"Medline Industries","Website":"https://www.medline.com"},
]

# Analyze 
results = []
for company in companies:
    print(f"Analyzing {company['Company']} ({company['Website']})...")
    classification = classify_website(company["Website"])
    if classification:
        results.append({
            "Company": company["Company"],
            "Website": company["Website"],
            **classification
        })

# Convert results to a DataFrame
df = pd.DataFrame(results)

# Save results to an Excel file
output_file = "C:\\Users\\User\\OneDrive\\Desktop\\Complete_Classifications.xlsx"
df.to_excel(output_file, index=False)
print(f"Results saved to {output_file}")

