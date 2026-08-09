import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


URL = "https://realpython.github.io/fake-jobs/"


def scrape_jobs():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    for job in soup.select("div.card-content"):
        title_element = job.select_one("h2.title")
        company_element = job.select_one("h3.company")
        location_element = job.select_one("p.location")
        link_element = job.select_one("a.card-footer-item")

        title = title_element.get_text(strip=True) if title_element else ""
        company = company_element.get_text(strip=True) if company_element else ""
        location = location_element.get_text(strip=True) if location_element else ""

        if link_element and link_element.get("href"):
            job_url = urljoin(URL, link_element["href"])
        else:
            job_url = ""

        jobs.append({
            "Job Title": title,
            "Company Name": company,
            "Location": location,
            "Job URL": job_url
        })

    return jobs


def save_to_csv(jobs, filename="jobs.csv"):
    fieldnames = [
        "Job Title",
        "Company Name",
        "Location",
        "Job URL"
    ]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(jobs)


if __name__ == "__main__":
    jobs = scrape_jobs()
    save_to_csv(jobs)

    print(f"Successfully scraped {len(jobs)} jobs.")
    print("Results saved to jobs.csv")
